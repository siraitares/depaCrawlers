# -*- coding: utf-8 -*-

import urllib2
from bs4 import BeautifulSoup
import time

baseUrl = "https://www.vivanuncios.com.mx"
url = "https://www.vivanuncios.com.mx/s-renta-inmuebles/tijuana/v1c1098l10015p1"
pagesToCrawl = 10
counter = 1
f = open('listadoVA.csv', 'w')
f.write("Título,Precio,Link,Fecha de publicación\n")

while (counter <= pagesToCrawl):
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    listings = soup.find_all('div', attrs={'class': 'result-link'})
    nextButton = soup.find('a', attrs={'class': 'next'})
    url = baseUrl + nextButton['href']
    print 'iteration: ' + str(counter)

    for i in listings:
        price = i.find('span', attrs={'class': 'amount'})
        if price:
            price = i.find('span', attrs={'class': 'amount'}).text.encode('utf-8')
            price = int(price.replace('$', '').replace(',', ''))
            if ((price >= 50) and (price <= 350)) or ((price >= 1500) and (price <= 6000)):
                title = i.find('a').text.encode('utf-8')
                title = title.replace(',', '\'')
                date = i.find('div', attrs={'class': 'creation-date'}).text.encode('utf-8')
                date = date.replace('\n', '')
                link = i.find('a')['href'].encode('utf-8')
                f.write(title + ',' + str(price) + ',' + baseUrl + link + ',' + date + '\n')
                print title + ',' + str(price) + ',' + baseUrl + link + ',' + date
            else:
            	print "Fuera del if " + str(price)
        else:
        	print "No trae valor"
    counter += 1
f.close()
