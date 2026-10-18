"""
Module:
Класс для управления медиафайлами. 
"""

from datetime import datetime
from core.media_file import AudioFile, VideoFile, ImageFile
from core.remote_storage import RemoteStorage

class MediaFileManager:
    """
    Класс MediaFileManager управляет медиафайлами, позволяя 
    создавать, сохранять и удалять аудио-, видео- и изображения.
    
    Атрибуты:
        storage (RemoteStorage): Объект для хранения файлов. По умолчанию None.
        files (list): Список созданных медиафайлов.
    
    Методы:
        create_audio_file(name: str, size: int, created_at: datetime, owner: str, **kwargs) -> AudioFile:
            Создаёт аудиофайл и добавляет его в список файлов.
    
        create_video_file(name: str, size: int, created_at: datetime, owner: str, **kwargs) -> VideoFile:
            Создаёт видеофайл и добавляет его в список файлов.
    
        create_image_file(name: str, size: int, created_at: datetime, owner: str, **kwargs) -> ImageFile:
            Создаёт изображение и добавляет его в список файлов.
    
        save_file(file):
            Сохраняет файл в хранилище, если оно задано.
    
        delete_file(file):
            Удаляет файл из хранилища, если оно задано.
    """

    def __init__(self, storage: RemoteStorage = None):
        self.storage = storage
        self.files = []

    def create_audio_file(self, name: str, size: int, created_at: datetime, 
                         owner: str, **kwargs) -> AudioFile:
        """Создает аудиофайл и добавляет его в список файлов.
        Аргументы:
            name (str): Название аудиофайла.
            size (int): Размер аудиофайла в байтах.
            created_at (datetime): Дата и время создания аудиофайла.
            owner (str): Владелец аудиофайла.
            **kwargs: Дополнительные параметры для создания аудиофайла.
        
        Возвращает:
            AudioFile: Созданный аудиофайл.
        """
        audio = AudioFile(name, size, created_at, owner, **kwargs)
        self.files.append(audio)
        return audio

    def create_video_file(self, name: str, size: int, created_at: datetime, 
                         owner: str, **kwargs) -> VideoFile:
        """Создает видеофайл и добавляет его в список файлов.
        Аргументы:
            name (str): Название видеофайла.
            size (int): Размер видеофайла в байтах.
            created_at (datetime): Дата и время создания видеофайла.
            owner (str): Владелец видеофайла.
            **kwargs: Дополнительные параметры для создания видеофайла.
        
        Возвращает:
            VideoFile: Созданный объект видеофайла.
        """
        video = VideoFile(name, size, created_at, owner, **kwargs)
        self.files.append(video)
        return video

    def create_image_file(self, name: str, size: int, created_at: datetime, 
                         owner: str, **kwargs) -> ImageFile:
        """Создает файл изображения и добавляет его в список файлов.
        Аргументы:
            name (str): Имя файла изображения.
            size (int): Размер файла изображения в байтах.
            created_at (datetime): Дата и время создания файла.
            owner (str): Владелец файла изображения.
            **kwargs: Дополнительные параметры для создания файла изображения.
        
        Возвращает:
            ImageFile: Созданный объект файла изображения.
        """
        image = ImageFile(name, size, created_at, owner, **kwargs)
        self.files.append(image)
        return image

    def save_file(self, file):
        """Сохраняет файл в хранилище.
        Аргументы:
            file: Объект файла, который необходимо сохранить.
        
        Возвращает:
            None
        
        Исключения:
            Может вызвать исключение, если хранилище недоступно или файл не может быть сохранен.
        """
        if self.storage:
            # Логика сохранения через storage
            pass

    def delete_file(self, file):
        """Удаляет указанный файл из хранилища.
        Аргументы:
            file (str): Имя файла, который необходимо удалить.
        
        Возвращает:
            None
        """
        if self.storage:
            # Логика удаления через storage
            pass
