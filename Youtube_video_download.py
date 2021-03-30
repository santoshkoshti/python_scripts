#pip install pytube

from pytube import YouTube

link = input("enter youtube url: ")

#link = "link paste here" without input method

url =YouTube(str(link))

video = url.streams.first()

video.download()