"""
    Запускает инициализацию компонентов медиа файлов и хранилищ.
    Cоздает экземпляры классов для работы с аудио, видео, изображениями, 
    а также для управления хранилищами в облаке и локальном хранилище. 
    После инициализации выводится сообщение о готовности медиа файлов и хранилищ к использованию.
"""

from _04_HW_MediaManager_YRB import AudioFile, VideoFile, ImageFile, S3Storage, CloudStorage, MediaFileManager

def main():

    print("--- Инициализация компонентов ---")
    
    # Создаем объекты медиафайлов
    audio = AudioFile()
    video = VideoFile()
    image = ImageFile()
    
    # Создаем объект хранилища
    storage = S3Storage()
    cloud = CloudStorage()
    
    # Передаем всё в менеджер файлов
    manager = MediaFileManager()
    
    print("Медиа файлы и хранилища готовы к использованию!")

if __name__ == "__main__":
    main()