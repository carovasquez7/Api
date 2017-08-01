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

soup = BeautifulSoup(page, 'html5lib')
soup_div = soup.find_all('div', class_='pub')
soup_a = soup_div.find_all('a')


#soup_li = [i['href'] for i in soup.find_all('a', href=True)]

#for i in soup.find_all('div', attrs={'class' : 'project-card-content'}):
  #  print i.a['href']


#f = open("ScrapingColombia.txt", 'w')

#f.write(soup_li)
#f.close()

print soup_a
