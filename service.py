import time
from jnius import autoclass

# Подключение Android-классов для работы со звуком
MediaPlayer = autoclass('android.media.MediaPlayer')
AudioManager = autoclass('android.media.AudioManager')

def play_background_audio():
    # Пример инициализации системного плеера Android
    media_player = MediaPlayer()
    # Укажите путь к вашему файлу audio.mp3
    media_player.setDataSource("/sdcard/Download/audio.mp3") 
    media_player.setAudioStreamType(AudioManager.STREAM_MUSIC)
    media_player.prepare()
    media_player.start()

if __name__ == '__main__':
    while True:
        try:
            play_background_audio()
        except Exception as e:
            print(f"Ошибка воспроизведения: {e}")
        
        # Периодичность выполнения цикла (в секундах)
        time.sleep(60) 
