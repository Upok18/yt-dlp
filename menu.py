import os
import sys
import subprocess
import time

from download.audio import download_audio
from download.video import download_video

def update_ytdlp():
    print("Checking for yt-dlp update...")
    try:
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "--upgrade", "yt-dlp"],
            check=True,
        )
        print("yt-dlp is ready!\n")
        time.sleep(2)
    except Exception:
        print("Update skipped or failed, continuing...\n")
        time.sleep(2)

def yt():
    os.system("cls")
    print("\033[92m", end="")
    while True:
        print("Welcome to the yt-dlp GUI!")
        print("Please select the options you want to use:")
        print("[1] Download video")
        print("[2] Download audio")
        print("[3] Exit")

        opt = input("Please enter the options you want to use (1-3): ")

        if opt == "1":
            download_video()
        elif opt == "2":
            download_audio()
        elif opt == "3":
            print("Exiting the program...")
            time.sleep(1.4)
            print("\033[0m", end="")
            os.system("cls")
            sys.exit() 
        else:
            print("Invalid Option please try again")
