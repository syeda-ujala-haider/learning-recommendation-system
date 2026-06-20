#!/usr/bin/env python3
import subprocess
import sys

def download_playlist_audio(playlist_url, output_path="downloads"):
    """
    Download all audio from a YouTube playlist.
    
    Args:
        playlist_url: YouTube playlist URL
        output_path: Where to save files (default: 'downloads' folder)
    """
    
    command = [
        "yt-dlp",
        "-f", "bestaudio/best",
        "-x",  # Extract audio
        "--audio-format", "mp3",  # Change to wav, m4a, etc. if you prefer
        "--audio-quality", "192",
        "-o", f"{output_path}/%(playlist_title)s/%(title)s.%(ext)s",
        playlist_url
    ]
    
    try:
        subprocess.run(command, check=True)
        print(f"✓ Downloaded to {output_path}/")
    except FileNotFoundError:
        print("Error: yt-dlp not installed. Run: pip install yt-dlp")
        sys.exit(1)
    except subprocess.CalledProcessError as e:
        print(f"Download failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <playlist_url> [output_path]")
        print("Example: python script.py 'https://youtube.com/playlist?list=PLueeE1ra2WZOeyaBTu2MWMIjp4RxMG5lk&si=DePCd7_upF2I-I9r")
        sys.exit(1)
    
    url = sys.argv[1]
    path = sys.argv[2] if len(sys.argv) > 2 else "downloads"
    download_playlist_audio(url, path)