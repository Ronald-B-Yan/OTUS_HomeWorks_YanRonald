"""
Module:
Классы для работы с медиа-файлами в удалённом хранилище.
"""
from abc import ABC, abstractmethod

class RemoteStorage(ABC):
    """Базовый класс для работы с удалёнными хранилищами.
    
    Класс определяет интерфейс для работы с удалёнными хранилищами, включая методы для загрузки, скачивания, удаления файлов и получения списка файлов в каталоге.
    
    Атрибуты:
        connection_params (dict): Словарь с параметрами подключения к удалённому хранилищу.
    
    Методы:
        upload(local_path: str, remote_path: str):
            Загрузка файла в удалённое хранилище.
    
        download(remote_path: str, local_path: str):
            Скачивание файла из удалённого хранилища.
    
        delete(remote_path: str):
            Удаление файла из удалённого хранилища.
    
        list_files(path: str) -> list:
            Получение списка файлов в заданном каталоге.
    """

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


class S3Storage(RemoteStorage):
    """Класс для работы с удалённым хранилищем S3.
    
    Этот класс предоставляет методы для загрузки, скачивания, удаления и перечисления файлов в удалённом хранилище S3.
    
    Attributes:
        connection_params (dict): Параметры подключения к удалённому хранилищу.
    
    Methods:
        __init__(connection_params):
            Инициализация объекта с параметрами подключения.
        
        upload(local_path, remote_path):
            Загрузка файла в удалённое хранилище.
        
        download(remote_path, local_path):
            Скачивание файла из удалённого хранилища.
        
        delete(remote_path):
            Удаление файла или директории из удалённого хранилища.
        
        list_files(path):
            Получение списка файлов в заданном каталоге удалённого хранилища.
    """

    def __init__(self, connection_params: dict):
        """Инициализация объекта с параметрами подключения.
        Аргументы:
            connection_params (dict): Словарь с параметрами подключения.
        """
        super().__init__(connection_params)

    def upload(self, local_path: str, remote_path: str):
        """Загрузка файла.
        Аргументы:
            local_path (str): Путь к локальному файлу, который необходимо загрузить.
            remote_path (str): Путь в удалённом хранилище, куда файл будет загружен.
        """
        pass

    def download(self, remote_path: str, local_path: str):
        """Скачивание файла.
        Аргументы:
            remote_path (str): Путь к файлу в удалённом хранилище.
            local_path (str): Путь, по которому файл будет сохранён локально.
        """
        pass

    def delete(self, remote_path: str):
        """Удаление файла.
        Аргументы:
            remote_path (str): Путь к файлу или директории в удалённом хранилище.
        """
        pass

    def list_files(self, path: str) -> list:
        """Список файлов в заданном каталоге удалённого хранилища.
        Аргументы:
            path (str): Путь к каталогу в удалённом хранилище.
        Возвращает:
            list: Список файлов в указанном каталоге.
        """
        pass


class CloudStorage(RemoteStorage):
    """Класс CloudStorage для работы с облачным хранилищем.
    Этот класс наследует от RemoteStorage и предоставляет методы для загрузки, скачивания, удаления и получения списка файлов в облачном хранилище.
    
    Аргументы:
        connection_params (dict): Словарь с параметрами подключения к облачному хранилищу.
    
    Методы:
        upload(local_path: str, remote_path: str):
            Загрузка файла в облако.
    
        download(remote_path: str, local_path: str):
            Скачивание файла из облака.
    
        delete(remote_path: str):
            Удаление файла из облака.
    
        list_files(path: str) -> list:
            Получение списка файлов в указанном каталоге.
    """

    def __init__(self, connection_params: dict):
        """Инициализация объекта с параметрами подключения.
        Аргументы:
            connection_params (dict): Словарь с параметрами подключения.
        """
        super().__init__(connection_params)

    def upload(self, local_path: str, remote_path: str):
        """Загрузка файла в облако.
        Аргументы:
            local_path (str): Путь к локальному файлу, который необходимо загрузить.
            remote_path (str): Путь в облаке, куда файл будет загружен.
        """
        pass

    def download(self, remote_path: str, local_path: str):
        """Скачивание файла из облака.
        Аргументы:
            remote_path (str): Путь к файлу в облаке.
            local_path (str): Путь, по которому файл будет сохранён локально.
        """
        pass

    def delete(self, remote_path: str):
        """Удаление файла из облака.
        Аргументы:
            remote_path (str): Путь к удалённому файлу или директории в облаке.
        """
        pass

    def list_files(self, path: str) -> list:
        """Метод для получения списка файлов в указанном каталоге.
         Аргументы:
            path (str): Путь к каталогу, в котором необходимо получить список файлов.
        Возвращает:
            list: Список файлов в указанном каталоге.
        """
        pass
