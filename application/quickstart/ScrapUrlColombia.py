import urllib2
from bs4 import BeautifulSoup
import requests
import sys
import webbrowser
#f = open("ScrapingColombia.txt", r)


URLBASE="https://www.superfinanciera.gov.co"
colombia = URLBASE +"/jsp/loader.jsf?lServicio=Publicaciones&lTipo=publicaciones&lFuncion=loadContenidoPublicacion&id=10427"

page = urllib2.urlopen(colombia)
soup = BeautifulSoup(page, 'lxml')

#Genera Diccionario con los datos
soup_a = soup.find_all('a')
list_elementos=[]
for links in soup.find_all('a'):
	
	url = str(links.get('href')).replace(URLBASE,"")
	
	if(url.split("?")[0]=="/descargas"):
		title =str(links.get('title'))
		if(title!="None"):
			title=title.replace(" de","").split(" ")
			elemento = {
				"moth": title[0],
				"year": title[1],
				"url": URLBASE + url
			}
			list_elementos.append(elemento)

print type(list_elementos)


''' CREAR ARCHIVO TXT DE LA LISTA, VERSION 1
sys.stdout = open('ListaUrl.txt','w')
print list_elementos


CREAR ARCHIVO TXT DE LA LISTA, VERSION 2
with open('ListaUrl2.txt','w') as output:
	output.write(str(list_elementos))

'''

#CREAR ARCHIVO TXT DE LA LISTA, VERSION 3 y ultima.
file = open('ListaUrl.txt','w')

for elemento in list_elementos:
	print >>file, elemento.get('url')

file.close()





###  Recorrer PAGINA
''' extrae el tag <a>
#soup_div = soup.find('div',{'class':'pub'}).find('ul')

for i in soup_div:

	#print i imprime li	
	soup_a = i.find('a')
	print soup_a
	
#print soup_div imprime ul
#print type(soup_div)
'''
