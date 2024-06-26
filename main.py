import os
from pytube import YouTube
from moviepy.editor import *

def download_and_convert_to_mp3(youtube_url):
    try:
        # Create a YouTube object
        yt_obj = YouTube(youtube_url)
        
        # Get the highest resolution video stream
        video = yt_obj.streams.get_highest_resolution()
        
        # Download the video
        print(f"Downloading: {yt_obj.title}")
        video_file = video.download()
        
        # Convert video to mp3
        print("Converting to MP3...")
        video_clip = VideoFileClip(video_file)
        audio_file = os.path.splitext(video_file)[0] + ".mp3"
        video_clip.audio.write_audiofile(audio_file)
        
        # Close the video clip
        video_clip.close()
        
        # Remove the original video file
        os.remove(video_file)
        
        print(f"Conversion complete. MP3 saved as: {audio_file}")
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage
youtube_link = input("Enter the YouTube video URL: ")
download_and_convert_to_mp3(youtube_link)
