'''
Web Scrapping
'''

import urllib.request as request
from bs4 import BeautifulSoup
import base64
import os
import re
import json
from datetime import datetime



###############################################Declare/Build The Global Fields#####################################################
scheme='https'
encode='utf-8'
proxy_user_id='User ID To Connect To Proxy Server'
proxy_password= 'Base64 Encoded Password to Connect to Proxy Server'
proxy_server='Proxy Server Name'
proxy_port='Proxy Server Port'     
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
opener = request.build_opener(auth, request.HTTPHandler, proxy) #also pass 'proxy' parameter if required.
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
request.install_opener(opener)

#Define search term
searchTerm = 'Kate Winslet'

# Replace spaces ' ' in search term for '%20' in order to comply with request
searchTerm = searchTerm.replace(' ','%20')

url='https://www.google.com/search?q='+searchTerm+'&tbm=isch'
#url='https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India'
#url='http://www.500px.com'
#url='https://www.booking.com/'
    
root_domain= re.split('[/:.?=]+',url) ##separate the domain name

#####################################################Connect The URL########################################################

def connectToURL(url):
  
    #Connect the URL and scrap the data
    try:        
        response = request.Request(url, headers=header) #set user agent in header to avoid 403 error

#        proxyDict = {'https' : proxy_url}
#        response=requests.get(url, headers=header, proxies=proxyDict)
        scrapped_data = request.urlopen(response)
        
    except IOError as io:
        print('IO Error Occurred During Connecting To The given URL: '+url+'\n'+str(io))
        pass            
    except Exception as ex:
        print('A Generic Error Occurred During Connecting To The given URL: '+url+'\n'+str(ex))
        pass
    finally:
        #flush the variables & streams to make them ready for next time.        
        opener.close()
    
    return scrapped_data

############################################################################################################################
####################################################Retrieve The Data#######################################################        

def extractDataFromSoup(scrapped_data):
    links_list=[]
    
    html_tag='img' #'a'
    ordinary_html_block='src' #'href'

    google_html_block_thumbnail='data-src' #WARNING: this will fetch only the thumbnail pictures
    google_html_block_full_res='ou'
    google_html_class_full_res='rg_meta'

    try:
        soup=BeautifulSoup(scrapped_data,'lxml')
        #print('##############################################################################################################')
        #print(soup.prettify())
        #print('##############################################################################################################')
    
        #Put The Outputs Into A List 
        links=soup.find_all(html_tag)
        for img_link in links:
            if('google' in root_domain):
                #links_list.append(str(img_link.get(google_html_block_thumbnail))) 
                #WARNING: the above line fetches only the thumbnail resolution, 
                #for the full resolution pictures, use the below block. 
                for img in soup.findAll('div', {'class': google_html_class_full_res}):
                    links_list.append(json.loads(img.get_text())[google_html_block_full_res])            
            elif(ordinary_html_block in str(img_link)):    
                links_list.append(str(img_link.get(ordinary_html_block)))

    except IOError as io:
        print('IO Error Occurred During Connecting To The given URL: '+url+'\n'+str(io))
        pass            
    except Exception as ex:
        print('A Generic Error Occurred During Connecting To The given URL: '+url+'\n'+str(ex))
        pass
    finally:
        #flush the variables & streams to make them ready for next time.
        links=None
        img_link=None
    
    return links_list
    
############################################################################################################################
########################################Retrieve The Links & Images & Write to File#########################################

def retrieveImageLinks(links_list):
    
    counter=0
    parentFolderName='D:\\tmp\\'  
    #build directory from the url being passed so as to have unique directories for each url
    directory=parentFolderName+root_domain[2]
    #if the directory is for google images, then create separate directories for each search term
    if('google' in directory):
        directory=directory+'\\'+searchTerm
    #create a flat file to store the links. Put the links file into the respective link directory
    links_to_store_filename= directory+'\\'+'links_'+str(datetime.now().strftime('%Y-%m-%d'))+'.txt'
    
    if not os.path.exists(directory):
                os.makedirs(directory)
            
    file=open(links_to_store_filename, 'w', encoding=encode)
    try:
        #Run the loop based on your requirement. 
        #WARNING: each loop returns 10100 records.
        #for _ in range(1):
            file.write('URL: '+url+'\n\n')
            
            for link in links_list:
                if(counter<100):
                    counter+=1        
                    finallink=link  # Assign link to linkew in case you do not need any customization

                    file.write('\n'+str(counter)+' *** ')            
                    #file.write('Link extracted is: '+link+'\n')

                    #this is specific for google search links
                    if(root_domain[2]=='google'):
                        if(('http' in link) or ('https' in link) or ('ftp' in link)):
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
            
                    file.write(finallink)
                                                               
                    print('---------------------------------------------------------------------------')
                    print('Extraction Index: '+str(counter)+'\nlink: '+link+'\nfinallink: '+finallink)
                    print('---------------------------------------------------------------------------')
                else:
                    break

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
        
    return links_to_store_filename

#############################################################################################################################    
###################################################Fetch The Images##########################################################
    
def extractImages(links_to_store_filename):
    
    filenametokens=links_to_store_filename.split('\\')
    file_path='\\\\'.join(filenametokens[:-1])+'\\\\'
    file_path=file_path.strip() #remove any unnecessary characters    
              
    counter=0
    try:        
        with open(links_to_store_filename) as link_file:              
                for line in link_file:
                    counter+=1
                    
                    #extract the file name from the url and build the file path
                    #file_path= 'D:\\Medical\\google\\'+finallink.split('/')[-1].split('?')[-1].split('=')[-1].split(':')[-1]                    
                    records=re.split('[ *** ]+',line)
                    
                    if(records[0].isdigit()): 
                        finallink=records[1]
                        image_file_path=file_path+(re.split('[/?=:,!@%&]+',finallink)[-1])
                        image_file_path=image_file_path.strip() #remove any unnecessary characters
                        
                        if('.' not in image_file_path):
                            #counter is added to avoid any unneccessary removal of filenames 
                            #in case they end with any of /?=: and also to avoid duplicates 
                            #print('created file path: '+image_file_path+str(counter)+'.jpg')
                            image_file_path=image_file_path+str(counter)+'.jpg'                            
                                                 
                        print(str(counter)+' : '+image_file_path)

                        #finally retrieve the file 
                        #Ensure your request object has headers to pass in order to avoid the HTTP 403 error. 
                        #Here this has been done in the Global Section                        
                        request.urlretrieve(finallink.strip(), image_file_path.strip())
                        #file.write('Extracted Data is at: ' + file_path+'\n\n')
        
    except IOError as io:
        print('IO Error Occurr:\n'+str(io))
        pass
    except Exception as e:
        print('An Error Occurred:\n', str(e))
        pass
    finally:
        #flush the variables & streams to make them ready for next time.        
        #finallink=None    
        #file.close()
        print('Done!!.. Closed All The Connections.. Good Bye!!! :)')
            
########################################################<<DONE>>#############################################################    
###############################################Start Calling The Methods#####################################################

if(__name__=='__main__'):
    
    data=None
    linkfilename=None
    list=[]
    
    data=connectToURL(url)
    list=extractDataFromSoup(data)
    linkfilename=retrieveImageLinks(list)
    extractImages(linkfilename) #'D:\\tmp\\google\\links_2018-01-10.txt') 

############################################################################################################################
