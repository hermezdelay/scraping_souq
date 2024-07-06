
# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import json
import csv
import requests

from winsound import Beep
from selenium import webdriver
from time import *

from urllib.error import HTTPError

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    partial_data = None

    url = 'https://aadl3inscription2024.dz/AR/Inscription-desktop.php'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36'
    }
    ouvert = False
    i=0
    while( ouvert == False):
        try:
            Beep(32200, 200)
            i=i+1
            connect_timeout = 2
            read_timeout = 10
            response = requests.get(url,timeout=(connect_timeout, read_timeout))

            if(response.status_code == 404): # pour surveiller l'erreur 404
                print("The response 404 for iteration", i)
                sleep(3)
                continue
            response.raise_for_status()
        except requests.exceptions.Timeout:
            print("The request timed out! %s", i)
        except HTTPError as hp:
            print('l"except du try %s', hp)

        else:# si sa marche je fait un bip sonore et j'ouvre l'url dans un nouvel navigateur
            print("it works")
            ouvert = True

            Beep(300, 12000)
            browser = webdriver.Chrome()

            print('debut du browser')
            browser.get(url)
            print('ouverture du browser')

            sleep(5000)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/


