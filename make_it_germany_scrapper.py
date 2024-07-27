from bs4 import BeautifulSoup
import re
import requests

allsite = ["https://www.make-it-in-germany.com/fr/travailler-en-allemagne/bourse-de-lemploi?tx_solr%5Bfilter%5D%5B0%5D=topjobs%3A4&tx_solr%5Bpage%5D=2&tx_solr%5Bq%5D=web#list45538",
           "https://www.systhen.com/contact/", "https://www.zeendoc.com"]
emails = []
tels = []
for l in allsite:
    print("----------------- le site " + l + " contient : ----------------------")
    r = requests.get(l)
    soup = BeautifulSoup(r.content, "html.parser")
    for link in soup.findAll('a', attrsclass={'btn btn--primary'}):
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