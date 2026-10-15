import os
from typing import Any
from yt_dlp import YoutubeDL


def download_video():
  url = input("\nEnter video URL: ").strip()

  save_dir = os.path.join(os.path.expanduser("~"), "Downloads")
  os.makedirs(save_dir, exist_ok=True)

  ydl_opts: dict[str, Any] = {
      "format": "best",
      "outtmpl": os.path.join(save_dir, "%(title)s.%(ext)s"),
      "extractor_args": {"youtube": {"player_client": ["android", "web"]}},
  }

  print(f"Downloading video to: {save_dir}")
  try:
    with YoutubeDL(ydl_opts) as ydl:  # type: ignore
      ydl.download([url])
    print("Video downloaded successfully!")
  except Exception as e:
    print(f"An error occurred: {e}")

  input("\nPress Enter to return to the menu...")