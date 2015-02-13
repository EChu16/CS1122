#Erich Chu
import requests 
from bs4 import BeautifulSoup

allURLs = []
r  = requests.get("https://github.com/trending")
soup = BeautifulSoup(r.text)
for link in soup.find_all("h3","repo-list-name"):	
    allURLs.append(link.find('a').get('href'))
for url in allURLs:
	print "https://github.com/" + url

