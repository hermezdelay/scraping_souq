from bs4 import BeautifulSoup
import re
import requests
import urllib.request
import time
import json
import csv


allsite = ["https://www.make-it-in-germany.com/fr/travailler-en-allemagne/bourse-de-lemploi?tx_solr%5Bfilter%5D%5B0%5D=topjobs%3A4&tx_solr%5Bpage%5D=",
           "&tx_solr%5Bq%5D=web#list45538"]
emails = []
tels = []

filecsv = open('make_it_in_germany.csv', 'w', encoding='utf8')
# Set the URL you want to webscrape from
url = 'https://saudi.souq.com/sa-ar/apple/new/a-c/s/?section=2&page='
file = open('SouqDataapple.json', 'w', encoding='utf8')
file.write('[\n')
data = {}
csv_columns = ['name', 'price', 'img']


for page in range(1000):
    print('---', page, '---')
    r = requests.get(allsite[0] + str(page) + allsite[1] )
    soup = BeautifulSoup(r.content, "html.parser")
    for link in soup.findAll('a', attrs={'class':'btn btn--primary'}):
        emails.append(link.get('href'))
        print(link.get('href'))
    for link in soup.findAll('a', attrs={'href': re.compile("^mailto:")}):
        emails.append(link.get('href'))
        print(link.get('href'))
    for tel in soup.findAll('a', attrs={'href': re.compile("^tel:")}):
        tels.append(tel.get('href'))
        print(tel.get('href'))

print("Toute la liste des emails est ici : ")
print(emails)
print(tels)