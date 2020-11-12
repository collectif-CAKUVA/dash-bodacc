import xml.etree.ElementTree as et

import pandas as pd
from matplotlib.pyplot import rcParams

import download_extract as de
import funct_pool
from api import api_request

rcParams.update({'font.size': 15})

test = ''

de.download()
de.extract_tar()


""" get element tree module to iter on xml files """
tree = et.parse('RCS-A_BXA20200102.xml')
root = tree.getroot()

""" retrieve the siren number from the xml files"""
for i in root.iter("avis"):
    root1 = i
    s_numero_identification = funct_pool.get_personnes(root1)

for siren in s_numero_identification:
    api_request(siren)

df_control = pd.DataFrame({
    'numero d identification': len(s_numero_identification),
}, index=["nb_lignes"]).T

df_final = pd.DataFrame({
    'Num RCS': s_numero_identification
})

# print(df_final)
