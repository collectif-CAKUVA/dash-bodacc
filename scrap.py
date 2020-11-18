import bs4
from requests import get
import re

""" scrapp bodacc request """
url = 'https://echanges.dila.gouv.fr/OPENDATA/BODACC/2020/'
r = get(url, allow_redirects=True)
soup = bs4.BeautifulSoup(r.content, "lxml")
files = []

""" regex to target only RCS-A files (bodacc A) """
pages = soup.findAll('a', href=re.compile('RCS-A'))
print("Total Links Found:ch", pages.__len__())
for l in pages:
    files.append(l.get('href'))
