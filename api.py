import requests
import json
from csv_ape import d

# import time

info = []
#83520611
siren = []
ape = []
activite = []
def api_request(siren):
    # time.sleep(2)
    url3 = f"https://entreprise.data.gouv.fr/api/sirene/v3/unites_legales/{siren}"
    response = requests.get(url3)
    # print(response.status_code)
    if response.status_code == 200:
        # info.append(response)

        json_data = json.loads(response.text)

        try:
            #print ape code
            print(json_data['unite_legale']['siren'])
            print(json_data['unite_legale']['etablissement_siege']['activite_principale'])
            ape.append(json_data['unite_legale']['etablissement_siege']['activite_principale'])
            # print key value from dict in code_ape.py removing (.)
            print(d.get(json_data['unite_legale']['etablissement_siege']['activite_principale'].replace('.','') ))
            activite.append(d.get(json_data['unite_legale']['etablissement_siege']['activite_principale'].replace('.','') ))
            print('##########' * 5)


            #print(json_data['unite_legale']['etablissement_siege']['libelle_commune'])

        except:

            print('None')
            print('##########' * 5)



