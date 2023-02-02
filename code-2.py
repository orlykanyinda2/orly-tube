import youtube_dl

def reset_ydl():
    global ydl
    ydl = youtube_dl.YoutubeDL({'format': 'bestaudio/best'})

reset_ydl()

def download_video(url):
    try:
        ydl.download([url])
    except Exception as e:
        print(e)
        reset_ydl()

while True:
    url = input("Enter the YouTube video URL: ")
    if url == "reset":
        reset_ydl()
        continue
    download_video(url)
