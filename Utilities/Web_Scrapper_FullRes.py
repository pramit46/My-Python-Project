'''
Web Scrapping
'''

import urllib.request as request
from bs4 import BeautifulSoup
import base64
import os
import re

##################################################Declare The Fields########################################################
#Define search term
searchTerm = 'Kate Winslet'

# Replace spaces ' ' in search term for '%20' in order to comply with request
searchTerm = searchTerm.replace(' ','%20')

url='https://www.google.com/search?q='+searchTerm+'&tbm=isch'
#url='https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India'
#url='http://www.cognizant.com/'
#url='http://www.500px.com'
#url='https://www.booking.com/'

proxy_user_id='585654'
proxy_password= 'TXljckB6ZTF1' #use an encoded password
proxy_server='proxy.cognizant.com'
proxy_port='6050'
encode='utf-8'
scheme='https'
header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'\
        ' Chrome/43.0.2357.134 Safari/537.36'}

links_to_store_filename='D:\\pramit.txt'
images_to_store_foldername='D:\\Medical\\'

html_tag='img' #'a'
ordinary_html_block='src' #'href'

google_html_block_thumbnail='data-src' #WARNING: this will fetch only the thumbnail pictures
google_html_block_full_res='ou'
google_html_class_full_res='rg_meta'

links_list=[]

############################################################################################################################
#####################################################Connect The URL########################################################

#Decode the password string on the runtime
proxy_url='https://'+proxy_user_id+':'+str(base64.b64decode(bytes(proxy_password, encode)))[2:-1]\
        +'@'+proxy_server+':'+proxy_port
    
root_domain= re.split('[/:.?=]+',url) ##separate the domain name

#Connect the URL and scrap the data
try:
    proxy = request.ProxyHandler({scheme:proxy_url})
    auth = request.HTTPBasicAuthHandler()
    opener = request.build_opener(auth, request.HTTPHandler,proxy) #also pass 'proxy' parameter if required.
    request.install_opener(opener)
    response = request.Request(url, headers=header) #set user agent in header to avoid 403 error

#    proxyDict = { 
#              'https' : proxy_url
#            }
#    response=requests.get(url, headers=header, proxies=proxyDict)
    scrapped_data = request.urlopen(response)
    soup=BeautifulSoup(scrapped_data,'lxml')
    print('##################################################################################################################')
    #print(soup.prettify())
    print('##################################################################################################################')
    
   

    #Put The Outputs Into A List 
    links=soup_format.find_all(html_tag)
    for img_link in links:
        if('google' in root_domain):
            #links_list.append(str(img_link.get(google_xml_block))) 
            #WARNING: the above line fetches only the thumbnail resolution, 
            #for the full resolution pictures, use the below block. 
            for img in soup.findAll('div', {'class': google_html_class_full_res}):
                links_list.append(json.loads(img.get_text())[google_html_block_full_res])            
        elif(xml_block in str(img_link)):    
            links_list.append(str(img_link.get(ordinary_html_block)))

except IOError as io:
    print('IO Error Occurred During Connecting To The given URL: '+url+'\n'+str(io))
    pass            
except Exception as ex:
    print('A Generic Error Occurred During Connecting To The given URL: '+url+'\n'+str(ex))
    pass
finally:
    #flush the variables & streams to make them ready for next time.
    #scrapped_data.close() #may not be necessary
    opener.close()
    links=None
    img_link=None
    
############################################################################################################################
####################################################Retrieve The Data#######################################################    

counter=0
try:
    file=open(links_to_store_filename, 'w', encoding=encode)    
    for link in links_list:
        
        counter+=1        
        finallink=link  # Assign link to linkew in case you do not need any customization
           
        file.write('Extraction Index: '+str(counter)+'\n')
        file.write('URL: '+url+'\n')
        file.write('Link extracted is: '+link+'\n')
                   
        #this is specific for google search links
        if(root_domain[2]=='google'):
            if(('http' in link) or ('https' in link)):
                finallink=link
            elif(link.startswith('//')):
                finallink=scheme+':'+link
            elif(link.startswith('/')):
                finallink=root_domain[0]+'://'+root_domain[1]+'.'+root_domain[2]+'.'+root_domain[3]+link 
        
        #for all other urls
        else:
            if(link.startswith('//')):
                finallink=scheme+':'+link
            elif(link.startswith('/')):
                if(url[-1]=='/'):
                    finallink=url[:-1]+link #-1 removes the trailing / from the field URL so as to remove the duplicates
                else:
                    finallink=url+link
            
        file.write('Finallink: '+finallink+'\n')
                
        #build directory from the url being passed so as to have unique directories for each url
        directory=images_to_store_foldername+root_domain[2]                        
        if not os.path.exists(directory):
            os.makedirs(directory)
        #extract the file name from the url and build the file path
        #file_path= 'D:\\Medical\\google\\'+finallink.split('/')[-1].split('?')[-1].split('=')[-1].split(':')[-1]
        file_path=directory+'\\'+(re.split('[/?=:]+',finallink)[-1])
        if('.' not in file_path):
            #counter is added to avoid any unneccessary removal of filenames 
            #in case they end with any of /?=: and also to avoid duplicates 
            print('created file path: '+file_path+str(counter)+'.jpg')
            file_path=file_path+str(counter)+'.jpg'             

        print('---------------------------------------------------------------------------')
        print('Extraction Index: '+str(counter)+'\nurl: '+url+'\nlink: '+link+'\nfinallink: '\
              +finallink+'\nExtracted Data is at: ' + file_path)
        print('---------------------------------------------------------------------------')
            
        #finally retrieve the file
        request.urlretrieve(finallink, file_path)
        
        file.write('Extracted Data is at: ' + file_path+'\n\n')

except IOError as io:
    print('IO Error Occurred:\n'+str(io))
    pass
except Exception as e:
    print('An Error Occurred:\n', str(e))
    pass
finally:
    #flush the variables & streams to make them ready for next time.
    link=None
    finallink=None    
    file.close()
    print('Done!!.. Closed All The Connections.. Good Bye!!! :)')

########################################################<<DONE>>#############################################################    
