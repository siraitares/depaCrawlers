# -*- coding: utf-8 -*-

import urllib2
from bs4 import BeautifulSoup

baseUrl = "https://www.vivanuncios.com.mx"
url = "https://www.vivanuncios.com.mx/s-renta-inmuebles/tijuana/v1c1098l10015p1"
pagesToCrawl = 10
counter = 1
minPesos = 1500
maxPesos = 6000
minDls = 50
maxDls = 350
f = open('listadoVA.csv', 'w')
f.write("Título,Precio,Link\n")

while (counter <= pagesToCrawl):
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    listings = soup.find_all('div', attrs={'class': 'tile-item'})
    nextButton = soup.find('a', attrs={'class': 'icon-right-arrow'})
    url = baseUrl + nextButton['href']
    for i in listings:
        price = i.find(itemprop='price')
        if price:
            price = int(i.find(itemprop='price').get('content'))
            if ((minDls <= price <= maxDls) or (minPesos <= price <= maxPesos)):
                title = i.find('h2').text.encode('utf-8').replace(',', '\'')
                link = i.find('a')['href'].encode('utf-8')
                f.write(title + ',' + str(price) + ',' + baseUrl + link + ',' + '\n')
    counter += 1
f.close()
