from pytube import YouTube
from moviepy.editor import AudioFileClip
import os

def download_audio(youtube_url, output_path="downloads"):
    try:
        # Создаем папку для загрузок, если она не существует
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        # Загружаем видео с помощью pytube
        yt = YouTube(youtube_url)
        video_stream = yt.streams.filter(only_video=False, file_extension="mp4").first()
        
        print(f"Скачиваю видео: {yt.title}")
        video_file = video_stream.download(output_path)
        
        # Преобразуем видео в аудио
        audio_output = os.path.join(output_path, f"{yt.title}.mp3")
        with AudioFileClip(video_file) as audio:
            audio.write_audiofile(audio_output)
        
        # Удаляем исходное видео, оставив только аудио
        os.remove(video_file)
        
        print(f"Аудиофайл сохранен: {audio_output}")

    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    youtube_url = input("Введите ссылку на YouTube видео: ")
    download_audio(youtube_url)


