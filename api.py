import requests
import json
import re
from csv_ape import ape_dict


sirenn_api = []
siret = []
ape = []
s_activite_insee= []
adresse = []


def api_request(siren):



    # time.sleep(2)
    """ global refer to sirenn_api list outside the function """
    url3 = f"https://entreprise.data.gouv.fr/api/sirene/v3/unites_legales/{siren}"
    remove_characters = [".", "[", "]", '"']
    response = requests.get(url3)
    if response.status_code == 200:
        json_data = json.loads(response.text)
        try:
            x = ape_dict.get(json_data['unite_legale']['etablissement_siege']['activite_principale'].replace('.', ''))
            clean = x[0]
        except:
            pass

        #try:
        #    print(json_data['unite_legale']['etablissements'][0]['siret'])
            # siret.append(json_data['unite_legale']['etablissements'][0]['siret'])

        #except:
        #    print(" /!\ erreur SIRET" * 5)

        try:
            print(json_data['unite_legale']['etablissement_siege']['activite_principale'])
            # ape.append(json_data['unite_legale']['etablissement_siege']['activite_principale'])
            # print key value from dict in code_ape.py removing (.)


            # print insee acitivite
            s_activite_insee.append(clean)
            print(clean)
            print(len(s_activite_insee))
            # print(json_data['unite_legale']['etablissement_siege']['geo_adresse'])
            # adresse.append(json_data['unite_legale']['etablissement_siege']['geo_adresse'])


        except:
            print(" /!\ erreur APE " * 5)
            # ape.append('none')
            s_activite_insee.append('none')
            print(len(s_activite_insee))

    else:
        print(response.status_code)
        sirenn_api.append("none")
        s_activite_insee.append('none')
        print("BAD REQUEST")

    return s_activite_insee

