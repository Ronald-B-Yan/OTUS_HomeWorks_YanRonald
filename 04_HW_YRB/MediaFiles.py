"""
Module:
Классы для работы с медиа-файлами, такими как 
аудио-, видеофайлы и растровые изображения.
"""

from datetime import datetime

class MediaFile:
    """Класс MediaFile представляет собой базовый класс для
    работы с медиа-файлами и методами для управления ими.
    
    Атрибуты:
        name (str): Имя файла.
        size (int): Размер файла в байтах.
        created_at (datetime): Дата и время создания файла.
        owner (str): Владелец файла.
        media_type (str): Тип медиа ('image', 'audio', 'video').
        mime_type (str): MIME-тип файла (например, 'image/jpeg', 'video/mp4').

    Методы:
        save(): Сохраняет изменения файла.
        delete(): Удаляет файл.
        update_metadata(metadata: dict): Обновляет метаданные файла.
        extract_features(): Извлекает признаки/характеристики файла.
    """

    def __init__(
        self, 
        name: str, 
        size: int, 
        created_at: datetime, 
        owner: str,
        media_type: str,
        mime_type: str,

    ):

        # Базовые атрибуты файла
        self.name = name
        self.size = size
        self.created_at = created_at
        self.owner = owner
        
        # Общие медиа-атрибуты
        self.media_type = media_type
        self.mime_type = mime_type
        
    def save(self):
        """Сохраняет изменения файла."""
        pass

    def delete(self):
        """Удаляет файл."""
        pass

    def update_metadata(self, metadata: dict):
        """Обновляет метаданные файла."""
        pass

    def extract_features(self):
        """Извлекает признаки/характеристики файла."""
        pass


class AudioFile(MediaFile):
    """Класс AudioFile для работы с аудиофайлами.
    
    Атрибуты:
        name (str): Имя аудиофайла.
        size (int): Размер аудиофайла в байтах.
        created_at (datetime): Дата и время создания аудиофайла.
        owner (str): Владелец аудиофайла.
        duration (int, optional): Продолжительность аудиофайла в секундах. По умолчанию None.
        bitrate (int, optional): Битрейт аудиофайла в кбит/с. По умолчанию None.
        codec (str, optional): Кодек аудиофайла. По умолчанию None.
    
    Методы:
        play(): Воспроизведение аудио.
        pause(): Пауза воспроизведения.
        stop(): Стоп воспроизведения.
        convert_to(target_format: str): Конвертация аудиофайла в другой формат.
        extract_features(): Извлечение признаков из аудио (например, спектр, темп и т.д.).
    """

    def __init__(
        self,
        name: str, 
        size: int, 
        created_at: datetime, 
        owner: str,
        duration: int = None, 
        bitrate: int = None, 
        codec: str = None):
        super().__init__(name, size, created_at, owner)
        
        # Атрибуты аудио файла
        self.duration = duration
        self.bitrate = bitrate
        self.codec = codec

    def play(self):
        """Воспроизведение аудио."""
        pass

    def pause(self):
        """Пауза воспроизведения."""
        pass

    def stop(self):
        """Стоп воспроизведения."""
        pass

    def convert_to(self, target_format: str):
        """Конвертация аудиофайла в другой формат."""
        pass

    def extract_features(self):
        """Извлечение признаков из аудио (например, спектр, темп и т.д.)."""
        pass


class VideoFile(MediaFile):
    """Класс для работы с видеофайлами.
    
    Атрибуты:
        name (str): Имя видеофайла.
        size (int): Размер видеофайла в байтах.
        created_at (datetime): Дата и время создания видеофайла.
        owner (str): Владелец видеофайла.
        duration (int, optional): Продолжительность видео в секундах. По умолчанию None.
        resolution (tuple, optional): Разрешение видео в формате (ширина, высота). По умолчанию None.
        codec (str, optional): Кодек, используемый для видео. По умолчанию None.
    
    Методы:
        play(): Воспроизведение видео.
        pause(): Пауза воспроизведения.
        stop(): Стоп воспроизведения.
        convert_to(target_format: str): Конвертация видео в другой формат.
        extract_features(): Извлечение признаков из видео (например, кадры, цветовая палитра).
        thumbnail(): Создание миниатюры видео.
    """

    def __init__(
        self, 
        name: str, 
        size: int, 
        created_at: datetime, 
        owner: str,
        duration: int = None, 
        resolution: tuple = None, 
        codec: str = None):
        super().__init__(name, size, created_at, owner)

        # Атрибуты видео файла        
        self.duration = duration
        self.resolution = resolution
        self.codec = codec

    def play(self):
        """Воспроизведение видео."""
        pass

    def pause(self):
        """Пауза воспроизведения."""
        pass

    def stop(self):
        """Стоп воспроизведения."""
        pass

    def convert_to(self, target_format: str):
        """Конвертация видео в другой формат."""
        pass

    def extract_features(self):
        """Извлечение признаков из видео (например, кадры, цветовая палитра)."""
        pass

    def thumbnail(self):
        """Создание миниатюры видео."""
        pass


class ImageFile(MediaFile):
    """Класс для работы с изображениями.
    
    Атрибуты:
        name (str): Имя файла.
        size (int): Размер файла в байтах.
        created_at (datetime): Дата и время создания файла.
        owner (str): Владелец файла.
        dimensions (tuple, optional): Размеры изображения в формате (ширина, высота). По умолчанию None.
        format (str, optional): Формат файла (например, jpg, png, bmp и т.д.). По умолчанию None.
    
    Методы:
        view(): Открывает изображение для просмотра.
        convert_to(target_format: str): Конвертирует изображение в другой формат.
        resize(width: int, height: int): Изменяет размер изображения.
        extract_features(): Извлекает признаки из файла (например, цветовая схема, данные EXIF, текстуры).
    """

    def __init__(
        self, 
        name: str, 
        size: int, 
        created_at: datetime, 
        owner: str,
        dimensions: tuple = None, format: str = None):
        super().__init__(name, size, created_at, owner)

        # Атрибуты растрового файла         
        self.dimensions = dimensions    # (ширина, высота)
        self.format = format            # Формат файла (jpg, png, bmp, etc.) 

    def view(self):
        """Открывает изображение для просмотра."""
        pass

    def convert_to(self, target_format: str):
        """Конвертирует изображение в другой формат."""
        pass

    def resize(self, width: int, height: int):
        """Изменяет размер изображения."""
        pass

    def extract_features(self):
        """Извлекает признаки из файла (например, цветовая схема, данные EXIF, текстуры)."""
        pass
