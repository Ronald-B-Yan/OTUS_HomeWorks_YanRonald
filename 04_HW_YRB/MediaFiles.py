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
        save(): Сохраняет изменения файла в хранилище.
        delete(): Удаляет файл из хранилища.
        update_metadata(metadata: dict): Обновляет метаданные файла.
        extract_features(): Извлекает признаки/характеристики файла.
    """

    def __init__(
        self, 
        name: str, 
        size: int, 
        created_at: datetime, 
        owner: str,
        media_type: str,                    # 'image', 'audio', 'video'
        mime_type: str,                     # Например, 'image/jpeg', 'video/mp4'

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
        """Сохраняет изменения файла в хранилище."""
        pass

    def delete(self):
        """Удаляет файл из хранилища."""
        pass

    def update_metadata(self, metadata: dict):
        """Обновляет метаданные файла."""
        pass

    def extract_features(self):
        """Извлекает признаки/характеристики файла."""
        pass


class AudioFile(MediaFile):
    """Класс для работы с аудиофайлами."""

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
        self.duration = duration  # продолжительность в секундах
        self.bitrate = bitrate    # битрейт в кбит/с
        self.codec = codec        # кодек

    def play(self):
        """Воспроизводит аудио."""
        pass

    def pause(self):
        """Пауза воспроизведения."""
        pass

    def stop(self):
        """Останавливает воспроизведение."""
        pass

    def convert_to(self, target_format: str):
        """Конвертирует аудиофайл в другой формат."""
        pass

    def extract_features(self):
        """Извлекает признаки из аудио (например, спектр, темп и т.д.)."""
        pass


class VideoFile(MediaFile):
    """Класс для работы с видеофайлами."""

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
        self.duration = duration        # продолжительность в секундах
        self.resolution = resolution    # (ширина, высота)
        self.codec = codec              # кодек

    def play(self):
        """Воспроизводит видео."""
        pass

    def pause(self):
        """Пауза воспроизведения."""
        pass

    def stop(self):
        """Останавливает воспроизведение."""
        pass

    def convert_to(self, target_format: str):
        """Конвертирует видео в другой формат."""
        pass

    def extract_features(self):
        """Извлекает признаки из видео (например, кадры, цветовая палитра)."""
        pass

    def thumbnail(self):
        """Генерирует миниатюру видео."""
        pass


class ImageFile(MediaFile):
    """Класс для работы с изображениями."""

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
        """Извлекает признаки из изображения (например, цветовая схема, данные EXIF, текстуры)."""
        pass
