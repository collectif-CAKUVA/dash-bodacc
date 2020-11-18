import xml.etree.ElementTree as et

import pandas as pd
from matplotlib.pyplot import rcParams

import download_extract as de
import funct_pool
import api
import time

# anomalies = entrée 89 > pas de siret


# rcParams.update({'font.size': 15})

test = ''
de.download()
de.extract_tar()

""" get element tree module to iter on xml files """
tree = et.parse('RCS-A_BXA20200102.xml')
root = tree.getroot()

""" retrieve the siren number from the xml files"""
for root1 in root.iter("avis"):
    s_numero_identification = funct_pool.get_personnes(root1)
    etablissement = root1.find("etablissement")
    if etablissement is None:
        s_activite.append("non renseigné")
    else:
        s_activite = funct_pool.get_etablissement(root1)

start_time = time.time()

""" iteration on the lenght s_numero_identification 
    1/ api request with siren to get the siret and APE code
    2/ print activite from the XML 
 """
for siren in range(len(s_numero_identification)):
    print(f'entrée n° {siren + 1}')
    print(s_numero_identification[siren])
    api.api_request(s_numero_identification[siren])
    print(s_activite[siren])
    print('##########' * 5)

""" counter """
end_time = time.time()
print(
    F"le temps d'execution du script est de {round(end_time - start_time)} s, soit {round((end_time - start_time) / 60)} min")

""" compare the lists """
print(f" nombre d'activité {len(s_activite)}, nombre de siren {len(s_numero_identification)}")

# df_control = pd.DataFrame({
#     'numero d identification': len(s_numero_identification),
# }, index=["nb_lignes"]).T
#
# df_final = pd.DataFrame({
#     'Num RCS': s_numero_identification
# })

# print(df_final)

# print(ape, activite)
