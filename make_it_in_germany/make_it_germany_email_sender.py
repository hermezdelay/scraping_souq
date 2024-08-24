import csv
from urllib.parse import unquote
import time




"""



import smtplib, ssl
# on rentre les renseignements pris sur le site du fournisseur
smtp_address = 'smtp.gmail.com'
smtp_port = 465

# on rentre les informations sur notre adresse e-mail
email_address = 'bonprixalgerie2022@gmail.com'
email_password = 'D@lisec2017'

# on rentre les informations sur le destinataire
email_receiver = 'dalil.systhen@gmail.com'

# on crée la connexion
context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_address, smtp_port, context=context) as server:
  # connexion au compte
  server.login(email_address, email_password)
  # envoi du mail
  server.sendmail(email_address, email_receiver, 'le contenu de l\'e-mail')
"""

"""
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


import smtplib, ssl
# on rentre les renseignements pris sur le site du fournisseur
smtp_address = 'smtp.gmail.com'
smtp_port = 465
email_address = 'bonprixalgerie2022@gmail.com'
email_password = 'D@lisec2017'

email_receiver = 'dalil.systhen@gmail.com'
# on crée un e-mail
message = MIMEMultipart("alternative")
# on ajoute un sujet
message["Subject"] = "[DataScientest] e-mail essai"
# un émetteur
message["From"] = email_address
# un destinataire
message["To"] = email_receiver

# on crée un texte et sa version HTML
texte = '''
Bonjour 
Ma super newsletter
Cdt
mon_lien_incroyable
'''

html = '''
<html>
<body>
<h1>Bonjour</h1>
<p>Ma super newsletter</p>
<b>Cdt</b>
<br>
<a href="https://datascientest.com">mon_lien_incroyable</a>
</body>
</html>
'''

# on crée deux éléments MIMEText
texte_mime = MIMEText(texte, 'plain')
html_mime = MIMEText(html, 'html')

# on attache ces deux éléments
message.attach(texte_mime)
message.attach(html_mime)

# on crée la connexion
context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_address, smtp_port, context=context) as server:
  # connexion au compte
  server.login(email_adress, email_password)
  # envoi du mail
  server.sendmail(email_address, email_receiver, message.as_string())
"""
"""
# coding: utf-8

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


email_address = 'bonprixalgerie2022@gmail.com'
email_password = 'dalil1991'
email_receiver = 'dalil.systhen@gmail.com'
msg = MIMEMultipart()
msg['From'] = email_address
msg['To'] = email_receiver
msg['Subject'] = 'Le sujet de mon mail'
message = 'Bonjour !'
msg.attach(MIMEText(message))
mailserver = smtplib.SMTP('smtp.gmail.com', 587)
mailserver.ehlo()
mailserver.starttls()
mailserver.ehlo()
mailserver.login(email_address, email_password)
mailserver.sendmail(email_address, email_receiver , msg.as_string())
mailserver.quit()
"""
import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from getpass import getpass

smtp_server = "smtp-mail.outlook.com"
#smtp_server = "smtp.office365.com"
smtp_port = 587
#smtp_port = 25
#smtp_port = 465
sender_email = 'safia.chrf@outlook.com'
email_password = 'dalil1991'
student_email = 'mailto:hermez.dalil@outlook.fr'
subject = "Web developer application - CHARFAOUI Safia"
message = (f"Dear Hiring Manager,"
           f"\n\nI came across the opportunity opening as a web developer, and I am writing to express my strong interest in the role. With my experience in Frontend development, I am confident that I would make a valuable addition to your team at your company."
           f"\n\nIn my current role as web developer at Dalisec Company, I have had the opportunity to achieve all projects that I've been affected to, which has prepared me well for the requirements of your job offer. I am excited about the possibility of contributing my skills to your company and being part of your team."
           f"\n\nI’ve spent time researching your business and am excited about the opportunity. The job description provides a fantastic snapshot of the role and what life would be like at your wonderfull organization."
           f"\n\nI’m excited about this opportunity and would love to know more about the process, including timelines for you to decide on interviews."
           f"\n\nI look forward to hearing from you."
           f"\nBest regards,"
           f"\nCHARFAOUI Safia.")

try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, email_password)
except Exception as e:
    print("Erreur lors de la connexion au serveur SMTP :", str(e))
    exit()


msg = MIMEMultipart()
msg["From"] = sender_email
msg["To"] = student_email
msg["Subject"] = subject
msg.attach(MIMEText(message, "plain"))


with open('make_it_in_germany.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        print(f'{line_count} -\t{unquote(row["email"])}')
        student_email = unquote(row["email"])
        try:
            server.sendmail(sender_email, student_email, msg.as_string())
            print(f"E-mail envoyé à ({student_email})")
            server.quit()
            print("Envoi de l'e-mails terminé.")
        except Exception as e:
            print(f"Erreur lors de l'envoi de l'e-mail à ({student_email}):", str(e))

        time.sleep(5)
        line_count += 1
    print(f'Processed {line_count} lines.')



