from pytube import YouTube
import re

# Define a regular expression pattern for a valid YouTube video URL
youtube_url_pattern = re.compile(r'https?://(www\.)?youtube\.com/watch\?v=[A-Za-z0-9_-]{11}')

# Get the URL of the video from the user
url = input("Enter the URL of the video: ")

# Check if the URL is a valid YouTube video URL
if not youtube_url_pattern.match(url):
    print("Invalid URL. Please enter a valid YouTube video URL.")
    exit()

try:
    # Get the video from YouTube
    yt = YouTube(url)

    # Get the available file types for the video
    video_formats = yt.filter('mp4')
    audio_formats = yt.filter('mp4')

    # Get the available video qualities
    video_qualities = []
    for video in video_formats:
        if video.resolution not in video_qualities:
            video_qualities.append(video.resolution)

    # Prompt user to select the file type
    print("Select the file type:")
    print("1. Video")
    print("2. Audio")
    selected_type = input("Enter the option number: ")

    # Check if the selected type is a valid number
    if not selected_type.isdigit() or int(selected_type) not in range(1, 3):
        print("Invalid option. Please enter a valid option number.")
        exit()

    # Prompt user to select the video quality
    print("Select the video quality:")
    for i, quality in enumerate(video_qualities):
        print(f"{i+1}. {quality}")
    selected_quality = input("Enter the option number: ")

    # Check if the selected quality is a valid number
    if not selected_quality.isdigit() or int(selected_quality) not in range(1, len(video_qualities)+1):
        print("Invalid option. Please enter a valid option number.")
        exit()

    # Get the selected video quality
    selected_quality = video_qualities[int(selected_quality)-1]

    if selected_type == '1':
        # Get the selected file type
        selected_type = video_formats.filter(resolution=selected_quality).first()
        # Download the video
        selected_type.download(filepath=f'{yt.title}.{selected_type.extension}')
        print(f'{yt.title}.{selected_type.extension} downloaded!')
    else:
        # Get the selected file type
        selected_type = audio_formats.first()
        # Download the audio
        selected_type.download(filepath=f'{yt.title}.{selected_type.extension}')
        print(f'{yt.title}.{selected_type.extension} downloaded!')
except Exception as e:
    print(f"An error occurred: {e}")
