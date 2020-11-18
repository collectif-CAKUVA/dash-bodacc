import requests
import json
from csv_ape import d
import funct_pool

#850828005
sirenn = []
siret = []
ape = []
activite = []
adresse = []
bug = 0
total = 0

def api_request(siren):
    # time.sleep(2)
    global bug
    global total
    global sirenn

    url3 = f"https://entreprise.data.gouv.fr/api/sirene/v3/unites_legales/{siren}"
    response = requests.get(url3)


    #x = json_data['unite_legale']['etablissements'][0]['siret']
    #y = json_data['unite_legale']['siren']
    #z = json_data['unite_legale']['etablissement_siege']['activite_principale']

    if response.status_code == 200:
        # info.append(response)
        json_data = json.loads(response.text)

        try:
            print(json_data['unite_legale']['etablissements'][0]['siret'])
            #siret.append(json_data['unite_legale']['etablissements'][0]['siret'])

        except:

            print(" /!\ erreur SIRET" * 5)

        try:
            print(json_data['unite_legale']['etablissement_siege']['activite_principale'])
            #ape.append(json_data['unite_legale']['etablissement_siege']['activite_principale'])

            # print key value from dict in code_ape.py removing (.)
            print(d.get(json_data['unite_legale']['etablissement_siege']['activite_principale'].replace('.' ,'')))
            #activite.append(d.get(json_data['unite_legale']['etablissement_siege']['activite_principale'].replace('.' ,'')))

            #print(json_data['unite_legale']['etablissement_siege']['geo_adresse'])
            #adresse.append(json_data['unite_legale']['etablissement_siege']['geo_adresse'])


        except:
            print(" /!\ erreur APE "*5)
            #ape.append('none')
            #activite.append('none')

    else:
        print(response.status_code)
        sirenn.append("none")
        print("BAD REQUEST")


            #print('None')
            #bug += 1
            #print('##########' * 5)

        #print(f"{round((bug / total) * 100)}% d'erreur")


    return sirenn#, siret, ape, activite

def api_insee(siret):
    url4 = f"https://api.insee.fr/entreprises/sirene/V3/siret/{siret}"
    response2 = requests.get(url4)
    if response2.status_code == 200:

        json_data2 = json.loads(response2.text)

        try:
            print(json_data2["etablissement"]["uniteLegale"]["activitePrincipaleUniteLegale"])

        except:
            print("error")