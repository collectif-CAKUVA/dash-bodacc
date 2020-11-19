import xml.etree.ElementTree as et

import pandas as pd
from matplotlib.pyplot import rcParams

import download_extract as de
from funct_pool import get_personnes, get_etablissement
from api import api_request, s_activite_insee
import time

# anomalies = entrée 89 > pas de siret
# rcParams.update({'font.size': 15})
from Bodacc.api import s_activite_insee

test = ''
de.download()
de.extract_tar()

s_numeroDepartement = []
s_date_parution = []


""" get element tree module to iter on xml files """
tree = et.parse('RCS-A_BXA20200102.xml')
root = tree.getroot()

date = root.find('dateParution').text


""" retrieve the siren number from the xml files"""
for root1 in root.iter("avis"):
    s_numero_identification = get_personnes(root1)
    s_date_parution.append(date)
    etablissement = root1.find("etablissement")
    if etablissement is None:
        s_activite_declaree.append("non renseigné")
    else:
        s_activite_declaree= get_etablissement(root1)

    n_dep = root1.find('numeroDepartement')
    if n_dep is None:
        s_numeroDepartement.append('None')
    else:
        s_numeroDepartement.append(n_dep.text)



start_time = time.time()

""" iteration on the lenght s_numero_identification 
    1/ api request with siren to get the siret and APE code
    2/ print activite from the XML 
 """
for siren in range(len(s_numero_identification)):

    print(f'entrée n° {siren + 1}')
    print(s_date_parution[siren])
    print(s_numero_identification[siren])
    s_activite_insee = api_request(s_numero_identification[siren])
    print(s_activite_declaree[siren])
    print(s_numeroDepartement[siren])

    print('##########' * 5)

""" counter """
end_time = time.time()
print(
    F"le temps d'execution du script est de {round(end_time - start_time)} s, soit {round((end_time - start_time) / 60)} min")

""" compare the lists """
print(f" nombre d'activité {len(s_activite_declaree)}, nombre de siren {len(s_numero_identification)}")

print(len(s_activite_declaree), len(s_numero_identification), len(s_numeroDepartement), len(s_activite_insee))






