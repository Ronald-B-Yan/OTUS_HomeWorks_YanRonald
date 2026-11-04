"""
Модуль предназначен для визуализации карт атрибутов и точек расположения скважин.
    
"""

import matplotlib.pyplot as plt
from functions_read_data import read_hr_slice

def plot_hr_slice_map(file_path, df_wells=None, save_path=None):
    """Функция для визуализации карты распределения параметра из файла с данными.
    
    Аргументы:
        file_path (str): Путь к файлу, содержащему данные для визуализации.
        df_wells (DataFrame, optional): DataFrame с координатами скважин. По умолчанию None.
        save_path (str, optional): Путь для сохранения карты. По умолчанию None.
    
    Возвращает:
        None: Функция не возвращает значения, но отображает карту и может сохранить её в файл.
    
    Примечания:
        Если файл не содержит валидных данных, будет выведено сообщение об ошибке.
    """
    # Читаем данные файла с помощью функции из functions_read_data
    df_slice, col_name = read_hr_slice(file_path)
    
    if df_slice.empty:
        print(f"Нечего визуализировать: файл {file_path} не содержит валидных данных.")
        return

    # Создаем фигуру для рисования
    plt.figure(figsize=(12, 10))
    
    # Строим карту распределения значений
    # tricontourf автоматически строит изолинии и закрашивает интервалы между ними
    # cmap='viridis' или 'jet', 'plasma', 'seismic' — можно выбрать любую палитру
    contour = plt.tricontourf(df_slice['X'], df_slice['Y'], df_slice['Value'], 
                              levels=50, cmap='jet')
    
    # Добавляем цветовую шкалу (легенду) справа
    cbar = plt.colorbar(contour)
    cbar.set_label(f"Значение атрибута ({col_name})", fontsize=12, labelpad=10)
    
    # Если переданы данные по скважинам, наносим их устья поверх карты
    if df_wells is not None and not df_wells.empty:
        # Рисуем точки скважин (черные кружки с белой обводкой)
        plt.scatter(df_wells['X'], df_wells['Y'], color='black', edgecolors='white', 
                    s=80, marker='o', zorder=5, label='Скважины')
        
        # Подписываем названия скважин чуть выше их точек
        for idx, row in df_wells.iterrows():
            # Если WellName в индексе, используем idx, если в колонке — row['WellName']
            well_label = idx if 'WellName' not in df_wells.columns else row['WellName']
            plt.text(row['X'], row['Y'] + 15, str(well_label), 
                     fontsize=9, fontweight='bold', color='black',
                     bbox=dict(facecolor='white', alpha=0.7, edgecolor='none', pad=1),
                     zorder=6)
        plt.legend(loc='upper right')


    # Оформление осей и заголовков
    plt.title(f"Карта распределения параметра: {col_name}", fontsize=12, fontweight='bold', pad=15)
    plt.xlabel("Координата X (м)", fontsize=10)
    plt.ylabel("Координата Y (м)", fontsize=10)
    
    # Делаем масштаб осей X и Y одинаковым, чтобы карта не искажалась (1 метр по X = 1 метру по Y)
    plt.gca().set_aspect('equal', adjustable='box')
    
    # Включаем сетку
    plt.grid(True, linestyle='--', alpha=0.5)
    
    # Корректируем поля вокруг карты
    plt.tight_layout()
    
    # Сохранение и/или вывод на экран
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Карта успешно сохранена в файл: {save_path}")
    
    plt.show()
