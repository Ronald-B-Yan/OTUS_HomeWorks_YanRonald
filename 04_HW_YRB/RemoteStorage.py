"""
Module:
Классы для работы с медиа-файлами в удалённом хранилище.
"""
from abc import ABC, abstractmethod

class RemoteStorage(ABC):
    """Базовый класс для работы с удалёнными хранилищами (S3, облако и т.д.)."""

    @abstractmethod
    def __init__(self, connection_params: dict):
        """Инициализация объекта с параметрами подключения.
        Аргументы:
            connection_params (dict): Словарь с параметрами подключения.
        """
        self.connection_params = connection_params

    @abstractmethod    
    def upload(self, local_path: str, remote_path: str):
        """Загрузка файла в удалённое хранилище.
         Аргументы:
            local_path (str): Путь к локальному файлу, который необходимо загрузить.
            remote_path (str): Путь к удалённому серверу, куда файл будет загружен.
        """
        pass

    @abstractmethod    
    def download(self, remote_path: str, local_path: str):
        """Скачивание файла из удалённого хранилища.
         Аргументы:
            remote_path (str): Путь к файлу на удалённом сервере.
            local_path (str): Путь, по которому файл будет сохранен локально.
        """
        pass

    @abstractmethod    
    def delete(self, remote_path: str):
        """Удаление файла из удалённого хранилища.
        Аргументы:
            remote_path (str): Путь к удалённому файлу или директории, которые необходимо удалить.
        """
        pass

    @abstractmethod    
    def list_files(self, path: str) -> list:
        """Список файлов в заданном каталоге.
        Аргументы:
            path (str): Путь к каталогу, из которого необходимо получить список файлов.
         Возвращает:
            list: Список файлов в указанном каталоге.
        """
        pass


