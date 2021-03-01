import requests
import tarfile
from scrap import files

#test = 'RCS-A_BXA20200102.taz'


def download(test):
    """ download taz file from Bodacc """
    #test = 'RCS-A_BXA20200102.taz'

    url2 = f"https://echanges.dila.gouv.fr/OPENDATA/BODACC/2020/{test}"
    response = requests.get(url2, stream=True)
    if response.status_code == 200:
        with open(test, 'wb') as f:
            f.write(response.raw.read())
            print(f'downloadfing {test}')



def extract_tar(test):
    """Extract .tar files to .xml"""
    tar = tarfile.open(test)
    tar.extractall()
    tar.close()
