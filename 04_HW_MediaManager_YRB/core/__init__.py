"""
Модули для работы с медиа-файлами и хранилищами
"""

from .media_file import MediaFile, AudioFile, VideoFile, ImageFile
from .remote_storage import RemoteStorage, S3Storage

__all__ = [
    'MediaFile',
    'AudioFile',
    'VideoFile',
    'ImageFile',
    'RemoteStorage',
    'S3Storage'
]