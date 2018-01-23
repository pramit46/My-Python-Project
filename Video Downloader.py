'''
Video Streaming
'''

import  pafy
import urllib.request as request
from bs4 import BeautifulSoup
import base64

#Declare the Global File Storing Location
FileStorageDirectory='D:\\tmp\\'


class downloader:
    def main(self):
        #Videos for Cats to Watch - Birds and Bird Sounds in October
        #url = "https://www.youtube.com/watch?v=aKX8uaoy9c8"
        #url = "https://www.youtube.com/watch?v=Aw1CQUMp-Gk" #????
        #url = 'https://www.youtube.com/watch?v=7Jojcy2siAo'
        #url = 'https://vimeo.com/channels/staffpicks/251083506'    
        url = 'https://fmovies.pe/watch/the-post.html'

        if('youtube' in url):
            print('into youtube')
            self.youtube(url,FileStorageDirectory)
        elif('fmovies' in url):
            print('into fmovies')
            self.fmovies(url,FileStorageDirectory)        


    def youtube(self,url,FileStorageDirectory):
        mediaStream = pafy.new(url)

        print(str(mediaStream.version), str(mediaStream.viewcount))
        print(mediaStream.author,str(mediaStream.length))
        print(str(mediaStream.duration),str(mediaStream.likes))
        print(str(mediaStream.dislikes))
        #print(mediaStream.description)
        #video=cv2.VideoCapture(best.url)

        videoStream = stream.streams
        for video in videoStream:
            print(video.resolution, video.extension, video.get_filesize(), video.url)

        videoBest = mediaStream.getbest() #use (preftype="mp4") as parameter to limit the search within the specified stream type
        print(videoBest.resolution, videoBest.extension)

        #download the video
        #you can use parameter quiet=False as well, but that does not work for me
        #filename = best.download(filepath="D:\\tmp\\Game." + best.extension) 
        filename = videoBest.download(filepath=FileStorageDirectory, quiet=False)


        audioStream=mediaStream.audiostreams
        for audio in audioStream:
            print(audio.bitrate, audio.extension, audio.get_filesize(), audio.url)

        audioBest=mediaStream.getbestaudio(preftype='m4a')
        file=audioBest.download(filepath=FileStorageDirectory,quiet=False)


    def fmovies(self,url,FileStorageDirectory):
        request = self.connect()
        response = request.Request(url, headers=header) #set user agent in header to avoid 403 error
        scrapped_data = request.urlopen(response)
        soup=BeautifulSoup(scrapped_data,'lxml')

        var=None

        links=soup.find_all('a')
        for img in soup.findAll('div', {'class': 'col3-btn'}):
            print(str(img))
            string1=(str(img.find('a').gettext('href')))
            print('####'+string1)

        if('seriesonline' in string1):
            #USE re package to read the id form the url

            links=soup.find_all('a')
            for img in soup.findAll('div', {'class': 'download'}):
                string2=(str(img.get('href')))

        #urllib.request.urlretrieve("http://statics.vidcdn.pro/1379/17/Molly_%23039%3Bs%20Game%202017%20Watch%20Online%20-%20Watch%20Movies%20for%20FREE%20-%20Seehd.Club.MP4",filename="D:\\tmp\\try")

    def connect(url):
        scheme='https'
        encode='utf-8'
        proxy_user_id= '<<ID To Connect Proxy Server>>'
        proxy_password= '<<PWD To Connect Proxy Server>>'
        proxy_server='<<Proxy Server IP>>'
        proxy_port='<<Proxy Server Port>>'     
        header={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
                   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                   'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                   'Accept-Encoding': 'none',
                   'Accept-Language': 'en-US,en;q=0.8',
                   'Connection': 'keep-alive'}


        #Decode the password string on the runtime
        proxy_url='https://'+proxy_user_id+':'+str(base64.b64decode(bytes(proxy_password, encode)))[2:-1]\
                    +'@'+proxy_server+':'+proxy_port

        proxy = request.ProxyHandler({scheme:proxy_url})
        auth = request.HTTPBasicAuthHandler()
        opener = request.build_opener(auth, request.HTTPHandler) #also pass 'proxy' parameter if required.
        opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
        request.install_opener(opener)

        return request

if(__name__=="__main__"):
    dl= downloader()
    dl.main()
