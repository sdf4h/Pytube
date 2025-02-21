from yt_dlp import YoutubeDL

def download_audio(url):
    # Параметры для загрузки только аудио
    options = {
        'format': 'bestaudio/best',  # Скачивает аудио в лучшем доступном качестве
        'outtmpl': '%(title)s.%(ext)s',  # Шаблон названия файла
        'postprocessors': [
            {  # Применение аудиопроцессора
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',  # Конвертирует аудио в MP3
                'preferredquality': '192',  # Качество аудио (битрейт 192 кбит/с)
            }
        ],
    }
    try:
        with YoutubeDL(options) as ydl:
            ydl.download([url])
            print("Аудио успешно загружено!")
    except Exception as e:
        print(f"Ошибка при загрузке: {e}")

# Ссылка на YouTube видео
video_url = "https://www.youtube.com/watch?v=<YOUR_VIDEO_ID>"

# Скачиваем аудио
download_audio(video_url)
