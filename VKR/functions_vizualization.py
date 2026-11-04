"""
Модуль предназначен для визуализации карт атрибутов и точек расположения скважин.
    
"""
import os
import matplotlib.pyplot as plt
import seaborn as sns
from functions_read_data import read_hr_slice
import glob
import math


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
    plt.title(f"Карта распределения атрибута: {col_name}", fontsize=12, fontweight='bold', pad=15)
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




def plot_all_features_coverage(df_filtered, target_col='Heff', data_slices_dir='./DATA_SLICES/'):
    """Функция для визуализации покрытия всех признаков в заданном датафрейме.
    
    Аргументы:
        df_filtered (pd.DataFrame): Отфильтрованный датафрейм, содержащий данные для визуализации.
        target_col (str, optional): Название целевого столбца. По умолчанию 'Heff'.
        data_slices_dir (str, optional): Путь к директории, содержащей файлы данных. По умолчанию './DATA_SLICES/'.
    
    Возвращает:
        None: Функция не возвращает значения, но выводит графики и сохраняет их в файл.
    
    Примечания:
        - Если в датафрейме нет признаков для визуализации, функция выводит предупреждение и завершает выполнение.
        - Для каждого признака создается гистограмма, сравнивающая значения из полного куба и из датафрейма скважин.
        - Графики сохраняются в файл 'all_features_coverage_grid.png'.
    """

    # Отбираем только имена признаков (колонки с сейсмическими атрибутами)
    # Исключаем таргет и служебные колонки, если они присутствуют
    service_cols = [target_col, 'X', 'Y', 'Spatial_Group']
    feature_cols = [col for col in df_filtered.columns if col not in service_cols]
    
    num_features = len(feature_cols)
    if num_features == 0:
        print("В датасете df_filtered не найдено признаков для визуализации.")
        return

    cols_grid = 3
    rows_grid = math.ceil(num_features / cols_grid)
    
    sns.set_theme(style="whitegrid")
    fig, axes = plt.subplots(rows_grid, cols_grid, figsize=(18, 5 * rows_grid))
    
    axes = axes.flatten() if num_features > 1 else [axes]
    
    print(f"Строим графики сопоставления для {num_features} признаков.")

    for i, col_name in enumerate(feature_cols):
        ax = axes[i]
        
        possible_files = glob.glob(os.path.join(data_slices_dir, f"{col_name}.*"))
        
        if not possible_files:
            print(f"Предупреждение: Файл для признака '{col_name}' не найден в {data_slices_dir}. Пропускаем.")
            ax.set_title(f"{col_name} (Файл не найден)", color='red')
            continue
            
        file_path = possible_files[0]
        
        try:
            df_full_slice, _ = read_hr_slice(file_path)
            full_values = df_full_slice['Value'].dropna()
        except Exception as e:
            print(f"Ошибка при чтении файла {file_path}: {e}")
            continue
            
        well_values = df_filtered[col_name].dropna()
        
        sns.histplot(
            full_values, 
            stat="density",
            kde=True,
            color="steelblue",
            alpha=0.3, 
            linewidth=0,
            label="Весь куб (Сейсмика)",
            ax=ax
        )
        
        sns.histplot(
            well_values, 
            stat="density", 
            kde=True, 
            color="crimson",
            alpha=0.6, 
            linewidth=1,
            edgecolor="white",
            label="Скважины (ML)",
            ax=ax
        )
        
        ax.set_title(f"Признак: {col_name}", fontsize=12, weight='bold')
        ax.set_xlabel("Значение", fontsize=10)
        ax.set_ylabel("Плотность", fontsize=10)
        
        stats_text = (
            f"Сейсм. [min/max]: {full_values.min():.1f} / {full_values.max():.1f}\n"
            f"Скваж. [min/max]: {well_values.min():.1f} / {well_values.max():.1f}"
        )
        ax.text(
            0.03, 0.97, stats_text, 
            transform=ax.transAxes, 
            fontsize=8, 
            verticalalignment='top',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.8, edgecolor='lightgray')
        )
        
        if i == 0:
            ax.legend(loc="upper right", fontsize=9)
            
    for j in range(num_features, len(axes)):
        fig.delaxes(axes[j])
        
    # Сохраняем все графики в один файл
    plt.tight_layout()
    output_grid_path = "all_features_coverage_grid.png"
    plt.savefig(output_grid_path, dpi=300, bbox_inches='tight')
    
    print(f"\nСвод графиков сохранён в '{output_grid_path}'")
    plt.show()

