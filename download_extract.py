import requests
import tarfile

test = 'RCS-A_BXA20200102.taz'


def download():
    """ download taz file from Bodacc """
    test = 'RCS-A_BXA20200102.taz'
    url2 = f"https://echanges.dila.gouv.fr/OPENDATA/BODACC/2020/{test}"
    response = requests.get(url2, stream=True)
    if response.status_code == 200:
        with open(test, 'wb') as f:
            f.write(response.raw.read())
    return test


def extract_tar():
    """Extract .tar files to .xml"""
    tar = tarfile.open(test)
    tar.extractall()
    tar.close()
