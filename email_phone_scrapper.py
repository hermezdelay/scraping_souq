from bs4 import BeautifulSoup
import re
import requests

allsite = ["https://www.systhen.com",
           "https://www.systhen.com/contact/", "https://www.zeendoc.com", "https://www.zeendoc.com/votre-projet/", "https://www.zeendoc.com/contact/", "https://www.zeendoc.com/prendre-rdv/",
           "https://www.cotranet.com", "https://www.cotranet.com/rendez-vous/", "https://www.qualios.com/fr/contact.html","https://www.getyooz.com/fr/", "https://www.getyooz.com/fr/nous-contacter"
           , "https://www.qualios.com/fr/presentation-qualios-doc.html", "https://www.laserfiche.com/contact/", "https://www.laserfiche.com"
           , "https://www.dimo-dematerialisation.com/contact/", "https://www.dimo-dematerialisation.com/logiciel-ged/", "https://www.ged.fr/ged-contact/"
           , "https://www.ged.fr/logiciel-ged/", "https://www.scoqi.fr/logiciel-qualite-scoqi-demande-de-documentation-demande-de-contact/", "https://www.scoqi.fr/logiciel-qualite/gestion-documentaire-ged-gestion-des-documents-logiciel-qualite-de-gestion-documentaire-ged/?gad_source=1&gclid=CjwKCAjw9IayBhBJEiwAVuc3fgJtfB65czRLPGDPrhfmCnAT2JLOVus6T0UPS9dY77hTo3iKObZ5tRoCA40QAvD_BwE"]
emails = []
tels = []
for l in allsite:
    print("----------------- le site " + l + " contient : ----------------------")
    r = requests.get(l)
    soup = BeautifulSoup(r.content, "html.parser")
    for link in soup.findAll('a', attrs={'href': re.compile("^mailto:")}):
        emails.append(link.get('href'))
        print(link.get('href'))
    for tel in soup.findAll('a', attrs={'href': re.compile("^tel:")}):
        tels.append(tel.get('href'))
        print(tel.get('href'))

print("Toute la liste des emails est ici : ")
print(emails)
print(tels)