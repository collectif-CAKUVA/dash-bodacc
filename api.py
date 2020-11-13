import requests
import json
from csv_ape import d
import funct_pool

#850828005
siren = []
ape = []
activite = []
adresse = []
bug = 0
total = 0

def api_request(siren):
    # time.sleep(2)
    global bug
    global total
    url3 = f"https://entreprise.data.gouv.fr/api/sirene/v3/unites_legales/{siren}"
    response = requests.get(url3)
    # print(response.status_code)
    if response.status_code == 200:
        # info.append(response)

        json_data = json.loads(response.text)

        try:

            #print(json_data['unite_legale']['siren'])
            print(json_data['unite_legale']['etablissements'][0]['siret'])
            total += 1
            #print(json_data['unite_legale']['etablissement_siege']['activite_principale'])
            #ape.append(json_data['unite_legale']['etablissement_siege']['activite_principale'])

            # print key value from dict in code_ape.py removing (.)
            #print(d.get(json_data['unite_legale']['etablissement_siege']['activite_principale'].replace('.' ,'')))
            #activite.append(d.get(json_data['unite_legale']['etablissement_siege']['activite_principale'].replace('.' ,'')))

            #print(json_data['unite_legale']['etablissement_siege']['geo_adresse'])
            #adresse.append(json_data['unite_legale']['etablissement_siege']['geo_adresse'])

            print('##########' * 5)





        except:
            #funct_pool.fill_up()
            print('None')
            bug += 1
            print('##########' * 5)

        print(f"{round((bug / total) * 100)}% d'erreur")


    return bug, total



