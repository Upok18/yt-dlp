import os
from typing import Any
from yt_dlp import YoutubeDL

def download_audio():
    url = input("\nEnter audio url: ").strip()

    save_dir = os.path.join(os.path.expanduser("~"), "Downloads")
    os.makedirs(save_dir, exist_ok=True)

    ydl_opts: dict[str, Any] = {
        "format": "bestaudio/best",
        "outtmpl": os.path.join(save_dir, "%(tittle)s.%(ext)s"),
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "prferredquality": "192"
            }
        ]
    }

    print(f"Downloading Audio to: {save_dir}")
    try:
        with YoutubeDL (ydl_opts) as ydl:  # type: ignore
            ydl.download([url])
            print("Video download successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

    input("\nPress Enter to return to menu")