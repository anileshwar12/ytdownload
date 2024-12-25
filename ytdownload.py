import os
from yt_dlp import YoutubeDL

def download_youtube_video(video_url, output_folder="downloads"):
    
    os.makedirs(output_folder, exist_ok=True)
    
    ydl_opts = {
        'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),
        'format': 'best',
        'postprocessors': [
            {'key': 'FFmpegVideoConvertor', 'preferedformat': 'mp4'}
        ]
    }

    with YoutubeDL(ydl_opts) as ydl:
        print(f"Downloading video: {video_url}")
        ydl.download([video_url])
        print("Download completed!")

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ").strip()
    download_youtube_video(video_url)
