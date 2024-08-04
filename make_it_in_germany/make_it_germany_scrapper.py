from bs4 import BeautifulSoup
import re
import requests
import urllib.request
import time
import json
import csv
from urllib.parse import urlparse, parse_qs
from urllib.parse import unquote

allsite = ["https://www.make-it-in-germany.com/fr/travailler-en-allemagne/bourse-de-lemploi?tx_solr%5Bfilter%5D%5B0%5D=topjobs%3A4&tx_solr%5Bpage%5D=",
           "&tx_solr%5Bq%5D=web#list45538"]
sites = []
emails = []
email = []
tels = []

filecsv = open('make_it_in_germany/make_it_in_germany.csv', 'w', encoding='utf8')
file = open('make_it_in_germany/make_it_in_germany.json', 'w', encoding='utf8')
file.write('[\n')
data = {}
csv_columns = ['name', 'email']

# je recherche dans les pages tous les url qui contienent la description du job
for page in range(10):
    print('---', page, '---')
    # ici je regroupe les fractions de l'url pour former une seule
    r = requests.get(allsite[0] + str(page) + allsite[1] )
    soup = BeautifulSoup(r.content, "html.parser")
    #dans cette boucle je récupère les URL de description du job qui contiennent de deans le emails
    for link in soup.findAll('a', attrs={'class':'btn btn--primary', 'href': re.compile("^https:")}):
        sites.append(link.get('href'))
        print(link.get('href'))

#ici je parcours les sites precedement remplis par la boucle
i=0
j=0

writer = csv.DictWriter(filecsv, fieldnames=csv_columns)
writer.writeheader()
for l in sites:
    print("----------------- le site " + l + " contient : ----------------------")
    r = requests.get(l)
    soup = BeautifulSoup(r.content, "html.parser")


    for link in soup.findAll('a', attrs={'href': re.compile("^mailto:")}):
        j=j+1
        mon_mail= str(unquote(link.get('href')))
        if "make-it-in-germany" not in mon_mail:            
            email = str(unquote(link.get('href')))
            print("i = "+ str(i) + " j = "+ str(j) + "  --> "+ email )
            # j'utilise unquote() de urlib pour parser le mail qui est codé en format url avec des %
            emails.append(email)
            
            writer.writerow(
                {'name': l.strip('\r\n'), 'email': email})
            data['name'] = unquote(l).strip('\r\n')
            data['email'] = email
            json_data = json.dumps(data, ensure_ascii=False)
            file.write(json_data)
            file.write(",\n")
            i=i+1

"""
        # ici je récupere le 2eme email(propre a celui qui a poste l'offre d'emploie) car j'ai remarqué que les autres sont propres au site de make it germany et qui ne m'interessent pas
        if(i==2):
            email = str(unquote(link.get('href')))
            print("j = "+ str(J) + " --> "+ email )
            # j'utilise unquote() de urlib pour parser le mail qui est codé en format url avec des %
            emails.append(email)
            writer.writerow(
                {'name': l.strip('\r\n'), 'email': email})
            data['name'] = unquote(l).strip('\r\n')
            data['email'] = email


            json_data = json.dumps(data, ensure_ascii=False)
            file.write(json_data)
            file.write(",\n")
        elif(i==4):
            i=0
            J=J+1
"""


"""for link in soup.findAll('a', attrs={'href': re.compile("^mailto:")}):
        emails.append(link.get('href'))
        print(link.get('href'))
    for tel in soup.findAll('a', attrs={'href': re.compile("^tel:")}):
        tels.append(tel.get('href'))
        print(tel.get('href'))
    """



print("Toute la liste des emails est ici : ")

#print(emails)
#print(emails)
#print(tels)

file.write("\n]")
filecsv.close()
file.close()