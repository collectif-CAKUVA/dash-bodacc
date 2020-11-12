import requests

# import time

info = []


def api_request(siren):
    # time.sleep(2)
    url3 = f"https://entreprise.data.gouv.fr/api/sirene/v3/unites_legales/{siren}"
    response = requests.get(url3)
    # print(response.status_code)
    if response.status_code == 200:
        # info.append(response)
        print(response.json())



