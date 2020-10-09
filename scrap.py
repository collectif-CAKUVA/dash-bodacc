from bs4 import BeautifulSoup
import requests
import re
import sys
import os



url = 'https://echanges.dila.gouv.fr/OPENDATA/BODACC/2020/'
r = requests.get(url, allow_redirects=True)
soup = BeautifulSoup(r.content, "lxml")
files = []

pages = soup.findAll('a', href=re.compile('RCS-A')) #regex to target only RCS-A files (bodacc A)
print("Total Links Found:ch",pages.__len__())
for l in pages:
     files.append(l.get('href'))