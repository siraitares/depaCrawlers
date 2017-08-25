# -*- coding: utf-8 -*-

import urllib2
from bs4 import BeautifulSoup

baseUrl = "https://tijuana.craigslist.com.mx"
url = "https://tijuana.craigslist.com.mx/search/apa"
pagesToCrawl = 5
counter = 1
minPesos = 1500
maxPesos = 6000
minDls = 50
maxDls = 350
f = open('listadoCL.csv', 'w')
f.write("Título,Precio,Link,Fecha de publicación\n")

while (counter <= pagesToCrawl):
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    listings = soup.find_all('p', attrs={'class': 'result-info'})
    nextButton = soup.find('a', attrs={'class': 'next'})
    url = baseUrl + nextButton['href']
    for i in listings:
        price = i.find('span', attrs={'class': 'result-price'})
        if price:
            price = i.find('span', attrs={'class': 'result-price'}).text.encode('utf-8')
            price = int(price.replace('$', ''))
            if ((minDls <= price <= maxDls) or (minPesos <= price <= maxPesos)):
                title = i.find('a').text.encode('utf-8')
                title = title.replace(',', '\'')
                date = i.find('time', attrs={'class': 'result-date'}).text.encode('utf-8')
                link = i.find('a')['href'].encode('utf-8')
                f.write(title + ',' + str(price) + ',' + baseUrl + link + ',' + date + '\n')
    counter += 1
f.close()
