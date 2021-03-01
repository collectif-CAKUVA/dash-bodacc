import requests
import tarfile
#from scrap import files


"""

testing module

"""

test = 'RCS-A_BXA20210005.taz'


def download():
    """ download taz file from Bodacc """
    test = 'RCS-A_BXA20210005.taz'

    url2 = f"https://echanges.dila.gouv.fr/OPENDATA/BODACC/2021/{test}"
    response = requests.get(url2, stream=True)
    if response.status_code == 200:
        with open(test, 'wb') as f:
            f.write(response.raw.read())
            print(f'downloading {test}')

def extract_tar(test):
    """Extract .tar files to .xml"""
    tar = tarfile.open(test)
    tar.extractall()
    tar.close()
