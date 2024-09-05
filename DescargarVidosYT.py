from pytube import YouTube

url = "https://www.youtube.com/watch?v=3F1aqvXGVQM"

yt = YouTube(url)

video = yt.streams.filter(progressive=True).order_by('resolution').desc().first()

output = r'.\Test'

print("La descarga ha comenzado")

video.download(output)

print("La descaga se ha completado")