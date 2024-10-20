import yt_dlp

def download_video(video_url, save_path):
    ydl_opts = {
        'outtmpl': f'{save_path}/%(title)s.%(ext)s',  # Output path with video title
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

# Example usage
video_url = "Place your link here in the form of http"  # Replace with the YouTube link
save_path = r"D:\\Youtube Video"  # Use raw string for the path,you can change the path but keep in this format only cause python uses \ as part of the code

download_video(video_url, save_path)
