import urllib
import requests
from xml.dom import minidom

collection = "bookmark_lookup"
baseurl = 'https://localhost:8089'
username = 'admin'
password = 'changeme'

servercontent = requests.post(baseurl + '/services/auth/login', verify=False,
  headers = {}, data = urllib.parse.urlencode({
    'username': username,
    'password': password
  }))
sessionkey = minidom.parseString(servercontent.text).getElementsByTagName('sessionKey')[0].childNodes[0].nodeValue
print("====> sessionkey:  %s  <====" % sessionkey)

#response = requests.get("https://localhost:8089/servicesNS/nobody/Splunk_Security_Essentials/storage/collections/config/"+collection,verify=False,
#  headers = {'Authorization': 'Splunk %s' % sessionkey})

#This part is not working for some reasons. Still working on it
response = requests.get("https://localhost:8089/servicesNS/nobody/Splunk_Security_Essentials/storage/collections/data/kvstorecoll?sort=name&skip=10&limit=10",verify=False,
  headers = {'Authorization': 'Splunk %s' % sessionkey})
print(response.text)