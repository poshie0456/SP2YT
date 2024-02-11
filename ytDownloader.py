from pytube import YouTube 
import os
def converter(url):
    if url != "x56":
        try:
            yt = YouTube(url) #init
            video = yt.streams.filter(only_audio=True).first() #only audio
            video.download(output_path=".") #CHANGE IF NEEDED
        except:
            print("Conversion Failure")
            
    else:
        print("Failure with Youtube API")
