"""
Модуль предназначен для:
Считывания скважинных данных в ASCII формате:
X  Y  WellName  Эффективная_Толщина_Пласта

Считывания карт атрибутов в ASCII формате:
X  Y  Parametr

Извлечения значений из файлов атрибутов в пределах заданного радиуса вокруг координат скважин
и формироания DataFrame, содержащего значения, извлеченные из файлов, добавленные к DataFrame скважин.
    
"""

import os
import io
import glob
import pandas as pd
import numpy as np
from scipy.spatial import KDTree

def read_well_data(well_file_path):
    """Читает данные о скважинах из указанного файла.
    
    Аргументы:
        well_file_path (str): Путь к файлу, содержащему данные о скважинах.
    
    Возвращает:
        pandas.DataFrame: DataFrame, содержащий данные о скважинах с колонками 'X', 'Y', 'WellName' и 'Heff'.
                         Значения в колонках 'X', 'Y' и 'Heff' преобразуются в числовой формат,
                         а строки с отсутствующими значениями в колонках 'X' и 'Y' удаляются.
    """
    
    # Читаем все колонки как текст
    df_wells = pd.read_csv(well_file_path, sep=r'\s+', names=['X', 'Y', 'WellName', 'Heff'], dtype=str)
    
    # Принудительно переводим координаты в числа. Заголовки (типа 'X', 'Y') превратятся в NaN
    df_wells['X'] = pd.to_numeric(df_wells['X'], errors='coerce')
    df_wells['Y'] = pd.to_numeric(df_wells['Y'], errors='coerce')
    df_wells['Heff'] = pd.to_numeric(df_wells['Heff'], errors='coerce')
    
    # Удаляем строки, где X или Y не стали числами (т.е. бывшие строки заголовков)
    df_wells = df_wells.dropna(subset=['X', 'Y'])
    
    return df_wells

def read_hr_slice(file_path):
    """Читает данные из файла и возвращает DataFrame и имя столбца значений.
    
    Аргументы:
        file_path (str): Путь к файлу, содержащему данные.
    
    Возвращает:
        tuple: Кортеж, содержащий:
            - pd.DataFrame: DataFrame, содержащий данные файла.
            - str: Имя столбца значений, извлеченное из файла.
    """
    # Имя колонки по умолчанию (имя файла без расширения)
    val_column_name = os.path.splitext(os.path.basename(file_path))[0]
    
    body_started = False
    data_lines = []
    
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            if '#{BODY}' in line:
                body_started = True
                continue
                
            if body_started:
                cleaned_line = line.strip()
                if not cleaned_line:
                    continue
                
                # Берём имя атрибута из строки
                if 'Value:' in cleaned_line:
                    parts = cleaned_line.split('Value:')
                    if len(parts) > 1:
                        # Убираем знак '>' в конце названия
                        val_column_name = parts[1].replace('>', '').strip()
                    continue
                
                data_lines.append(cleaned_line)
                    
    data_str = '\n'.join(data_lines)
    
    # Читаем всё как текст, чтобы Pandas не ругался на строки вида "<X> <Y>"
    df_slice = pd.read_csv(io.StringIO(data_str), sep=r'\s+', names=['X', 'Y', 'Value'], dtype=str)
    
    # Конвертируем в числа. Все не-числа станут NaN
    df_slice['X'] = pd.to_numeric(df_slice['X'], errors='coerce')
    df_slice['Y'] = pd.to_numeric(df_slice['Y'], errors='coerce')
    df_slice['Value'] = pd.to_numeric(df_slice['Value'], errors='coerce')
    
    # Очищаем от строк-заголовков (где X или Y превратились в NaN)
    df_slice = df_slice.dropna(subset=['X', 'Y'])
    
    # Исключаем Null Value (-1.0000e+30)
    df_slice = df_slice[df_slice['Value'] > -1e30] 
    
    return df_slice, val_column_name


def extract_values_by_radius(df_wells, hr_files_dir, radius_m):
    """Извлекает значения из файлов по заданному радиусу вокруг координат скважин.
    
    Аргументы:
        df_wells (pandas.DataFrame): DataFrame, содержащий координаты скважин с колонками 'X' и 'Y'.
        hr_files_dir (str): Путь к директории, содержащей файлы для обработки.
        radius_m (float): Радиус в метрах, в пределах которого будут извлекаться значения.
    
    Возвращает:
        pandas.DataFrame: Новый DataFrame, содержащий значения, извлеченные из файлов, добавленные к исходному DataFrame скважин.
    
    Исключения:
        Обрабатывает и выводит ошибки, возникающие при чтении файлов или обработке данных.
    """
    # Создаем копию таблицы скважин, куда будем добавлять новые колонки
    df_result = df_wells.copy()
    
    # Координаты скважин для поиска
    well_coords = df_result[['X', 'Y']].values
    
    # Ищем все файлы в папке (можно настроить маску, например '*.txt' или '*.dat')
    file_list = glob.glob(os.path.join(hr_files_dir, '*'))
    
    print(f"Найдено файлов для обработки: {len(file_list)}")
    
    for file_path in file_list:
        try:
            # Читаем файл HR
            df_slice, col_name = read_hr_slice(file_path)
            
            if df_slice.empty:
                print(f"Файл {os.path.basename(file_path)} пустой или содержит только Null Values.")
                df_result[col_name] = np.nan
                continue
                
            # Строим пространственное дерево по координатам из файла HR
            slice_coords = df_slice[['X', 'Y']].values
            tree = KDTree(slice_coords)
            
            # Ищем все точки грида в радиусе radius_m от каждой скважины
            indices_list = tree.query_ball_point(well_coords, r=radius_m)
            
            # Собираем значения
            extracted_values = []
            for i, indices in enumerate(indices_list):
                if indices:
                    # Если точки найдены в радиусе — усредняем их значения (Mean)
                    # При желании np.mean можно заменить на np.median
                    val = df_slice.iloc[indices]['Value'].mean()
                else:
                    # Если в радиусе пусто, ставим nan
                    val = np.nan
                    
                extracted_values.append(val)
            
            # Добавляем колонку в итоговый датафрейм
            df_result[col_name] = extracted_values
            print(f"Успешно обработан: {col_name}")
            
        except Exception as e:
            print(f"Ошибка при обработке файла {file_path}: {e}")
            
    return df_result