'''

from bs4 import BeautifulSoup

import requests

url = raw_input("Enter a website to extract the URL's from: ")

r  = requests.get("http://" +url)

data = r.text

soup = BeautifulSoup(data)

for link in soup.find_all('a'):
    print(link.get('href'))

'''

import urllib2
from bs4 import BeautifulSoup


#f = open("ScrapingColombia.txt", r)

colombia = "https://www.superfinanciera.gov.co/jsp/loader.jsf?lServicio=Publicaciones&lTipo=publicaciones&lFuncion=loadContenidoPublicacion&id=10427"
page = urllib2.urlopen(colombia)

soup = BeautifulSoup(page, 'html.parser')

#soup_div = soup.find('div', class_='pub').find('a')

soup_div = soup.find('div', class_='pub').find('ul')

for i in soup_div:
	#print i
	print i.find('a')
#print soup_div

