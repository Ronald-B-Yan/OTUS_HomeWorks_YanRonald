import os
import glob
import pandas as pd
import numpy as np
from scipy.spatial import KDTree

def read_well_data(well_file_path):
    """
    Считывает TXT файл со скважинными данными формата: X Y WellName Heff
    """
    # Предполагаем разделитель - пробелы или табуляция. 
    # Если формат строго фиксирован, можно настроить sep более точно.
    df_wells = pd.read_csv(well_file_path, sep=r'\s+', names=['X', 'Y', 'WellName', 'Heff'])
    return df_wells

def read_hr_slice(file_path):
    """
    Считывает файлы HampsonRussell формата {2D DATA} / {BODY}
    Пропускает заголовки и вытаскивает X, Y и само Значение.
    """
    # Автоматически находим имя колонки со значением из строки под #{BODY}
    val_column_name = os.path.basename(file_path) # дефолтное имя, если что-то пойдет не так
    
    body_started = False
    data_lines = []
    
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            if '#{BODY}' in line:
                body_started = True
                continue
            if body_started:
                # Пропускаем строку с именами колонок типа <X> <Y> <Value:...>
                if '<X>' in line or '<Y>' in line:
                    # Попробуем вытащить точное имя атрибута
                    parts = line.split('Value:')
                    if len(parts) > 1:
                        val_column_name = parts[1].replace('>', '').strip()
                    continue
                
                # Сохраняем строки с данными
                if line.strip():
                    data_lines.append(line)
                    
    # Превращаем строки в DataFrame
    # Будем использовать StringIO для быстрой загрузки
    from io import StringIO
    df_slice = pd.read_csv(StringIO(''.join(data_lines)), sep=r'\s+', names=['X', 'Y', 'Value'])
    
    # Исключаем Null Value (-1.0000e+36 из вашего заголовка)
    df_slice = df_slice[df_slice['Value'] > -1e30] 
    
    return df_slice, val_column_name

def extract_values_by_radius(df_wells, hr_files_dir, radius_m):
    """
    Пробегает по всем 60 файлам, строит KDTree и снимает значения для каждой скважины
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
            # 1. Читаем файл HR
            df_slice, col_name = read_hr_slice(file_path)
            
            if df_slice.empty:
                print(f"Файл {os.path.basename(file_path)} пустой или содержит только Null Values.")
                df_result[col_name] = np.nan
                continue
                
            # 2. Строим пространственное дерево по координатам из файла HR
            slice_coords = df_slice[['X', 'Y']].values
            tree = KDTree(slice_coords)
            
            # 3. Ищем все точки грида в радиусе radius_m от каждой скважины
            indices_list = tree.query_ball_point(well_coords, r=radius_m)
            
            # 4. Собираем значения
            extracted_values = []
            for i, indices in enumerate(indices_list):
                if indices:
                    # Если точки найдены в радиусе — усредняем их значения (Mean)
                    # При желании np.mean можно заменить на np.median или брать строго ближайшую
                    val = df_slice.iloc[indices]['Value'].mean()
                else:
                    # Если в радиусе пусто, ищем одну самую ближайшую точку без ограничения по радиусу,
                    # либо ставим np.nan (сейчас сделано: пишем NaN)
                    val = np.nan
                    
                extracted_values.append(val)
            
            # Добавляем колонку в итоговый датафрейм
            df_result[col_name] = extracted_values
            print(f"Успешно обработан: {col_name}")
            
        except Exception as e:
            print(f"Ошибка при обработке файла {file_path}: {e}")
            
    return df_result

# ==========================================
# ПРИМЕР ИСПОЛЬЗОВАНИЯ:
# ==========================================
if __name__ == '__main__':
    # Пути к вашим данным (замените на свои)
    WELLS_FILE = 'D:\NewEducation\OTUS\OTUS_HW_YRB\DATA_WELLS\Heff_Ju1.txt'
    HR_DIR = 'D:\NewEducation\OTUS\OTUS_HW_YRB\DATA_SLICES/'
    SEARCH_RADIUS = 100.0 # Радиус сбора данных в метрах
    
    # 1. Считываем скважины
    # df_wells = read_well_data(WELLS_FILE)
    
    # 2. Запуск расчета
    # Замените demo_wells на df_wells, когда пропишете реальные пути
    final_table = extract_values_by_radius(WELLS_FILE, HR_DIR, radius_m=SEARCH_RADIUS)
    
    # 3. Смотрим результат и сохраняем в Excel/CSV
    print("\nИтоговая таблица:")
    print(final_table.head())
    
    # final_table.to_excel('wells_with_attributes.xlsx', index=False)
