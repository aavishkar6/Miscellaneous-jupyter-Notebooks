
import pytube


link = input("Video URL plz: ")
video_download = pytube.YouTube(link)
video_download.streams.first().download()
print('Video Downloaded', link)






# print("Hello world")