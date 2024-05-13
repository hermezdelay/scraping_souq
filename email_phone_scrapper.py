from bs4 import BeautifulSoup
import re
import requests

allsite = ["https://www.systhen.com",
           "https://www.systhen.com/contact/", "https://www.zeendoc.com", "https://www.zeendoc.com/votre-projet/", "https://www.zeendoc.com/contact/", "https://www.zeendoc.com/prendre-rdv/",
           "https://www.cotranet.com", "https://www.cotranet.com/rendez-vous/", "https://www.getyooz.com/fr/", "https://www.getyooz.com/fr/nous-contacter"]
emails = []
tels = []
for l in allsite:
    print("le site " + l + " contient :")
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