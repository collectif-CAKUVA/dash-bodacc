import os.path
import bs4
from requests import get
import re
import requests
import tarfile

"""
Downloads all .taz from data.gouv.fr (2021 folder)

then 

unzip.taz to .xml

# functionnal but unactivated. download_extract.py is enough for testing now
"""


def extract_tar(test):
    """Extract .tar files to .xml"""
    tar = tarfile.open(test)
    print(f'extracting {test}')
    tar.extractall()
    tar.close()

def download(test):
    """ download taz file from Bodacc """
    url2 = f"https://echanges.dila.gouv.fr/OPENDATA/BODACC/2021/{test}"
    response = requests.get(url2, stream=True)
    if os.path.isfile(f'./{test}') is False:
        if response.status_code == 200:
            with open(test, 'wb') as f:
                f.write(response.raw.read())
                print(f'downloadfing {test}')
            extract_tar(test)
    else:
        print('file already there')

def scrap ():
    """ scrapp bodacc request """
    url = 'https://echanges.dila.gouv.fr/OPENDATA/BODACC/2021/'
    r = get(url, allow_redirects=True)
    soup = bs4.BeautifulSoup(r.content, "lxml")

    """ regex to target only RCS-A files (bodacc A) """
    pages = soup.findAll('a', href=re.compile('RCS-A'))
    print("Total Links Found:", pages.__len__())
    for l in pages:
        download(l.get('href'))


if __name__ == '__main__':
    pass
    #scrap()