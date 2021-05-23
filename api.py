import requests
import json
from csv_ape import ape_dict


sirenn_api = []
siret = []
s_ape = []
s_activite_insee= []
adresse = []



def api_request(siren):

    url3 = f"https://entreprise.data.gouv.fr/api/sirene/v3/unites_legales/{siren}"

    response = requests.get(url3)
    if response.status_code == 200:
        json_data = json.loads(response.text)
        try:
            x = ape_dict.get(json_data['unite_legale']['etablissement_siege']['activite_principale'].replace('.', ''))
            clean = x[0]
            code_ape = json_data['unite_legale']['etablissement_siege']['activite_principale']
            activite_insee = clean

        except:
            code_ape = "APE Non Diffusable"
            activite_insee = "APE Non Diffusable"
            
    elif response.status_code == 429:
        print(response.status_code)
        print(" TOO MANY REQUEST "*10)
        code_ape = "APE Non Diffusable"
        activite_insee = "APE Non Diffusable"
    else:
        print(response.status_code)
        print(" BAD REQUEST" )
        code_ape = "APE Non Diffusable"
        activite_insee = "APE Non Diffusable"

    return activite_insee, code_ape

