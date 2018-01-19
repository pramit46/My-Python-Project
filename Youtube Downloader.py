'''
Youtube Video Stream Downloader
'''

import  pafy

#Videos for Cats to Watch - Birds and Bird Sounds in October
url = "https://www.youtube.com/watch?v=aKX8uaoy9c8"
video = pafy.new(url)

#print several parameters of the video
print(str(video.version), str(video.viewcount))
print(video.author,str(video.length))
print(str(video.duration),str(video.likes))
print(str(video.dislikes))
#print(video.description)
#video=cv2.VideoCapture(best.url)

#list down the available stream details
streams = video.streams
for s in streams:
    print(s.resolution, s.extension, s.get_filesize(), s.url)


#You can use (preftype="mp4") as parameter to limit the search within the specified stream type. 
#No params would fetch the best among all
best = video.getbest() 
print(best.resolution, best.extension)


#download the video
#you can use parameter quiet='false' as well, but that does not seem to work for me :-P
#filename = best.download(filepath="D:\\tmp\\Game." + best.extension) 
filename = best.download(filepath="D:\\tmp\\", quiet='false') 
