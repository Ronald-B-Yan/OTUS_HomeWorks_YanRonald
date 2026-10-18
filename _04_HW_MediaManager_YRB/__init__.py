"""
Media Manager - система управления медиа-файлами
"""

__version__ = "1.0.0"
__author__ = "YRB"

# Импорты для удобного использования
from core.media_file import MediaFile, AudioFile, VideoFile, ImageFile
from core.remote_storage import RemoteStorage, S3Storage, CloudStorage
from manager.file_manager import MediaFileManager

__all__ = [
    'MediaFile',
    'AudioFile', 
    'VideoFile',
    'ImageFile',
    'RemoteStorage',
    'S3Storage',
    'CloudStorage',
    'MediaFileManager'
]
