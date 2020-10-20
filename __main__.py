import pandas as pd
import xml.etree.ElementTree as et
from matplotlib.pyplot import rcParams
import download_extract as de
import funct_pool

rcParams.update({'font.size': 15})

test = ''

de.download()
de.extract_tar()

# XML parsing func


s_cp_personne = []
s_ville_personne = []
s_date_parution = []
s_numeroDepartement = []

tree = et.parse('RCS-A_BXA20200102.xml')
root = tree.getroot()

# main parsing process
for i in root.iter("avis"):
    root1 = i

    x = 'MIXTE'
    s_numero_identification = funct_pool.get_personnes(root1)

    # get_adresse_france(root1)
    # get_adresse_france(root1) not called

    # 'tribunal' = "GREFFE DU TRIBUNAL MIXTE DE COMMERCE DE "CITY" " or "GREFFE DU TRIBUNAL DE COMMERCE DE "CITY"
    # str that must be erased to get CITY only
    n_dep = root1.find('tribunal')
    if x in n_dep.text:
        s_numeroDepartement.append((n_dep.text).replace('GREFFE DU TRIBUNAL MIXTE DE COMMERCE DE ', ''))
    else:
        s_numeroDepartement.append((n_dep.text).replace('GREFFE DU TRIBUNAL DE COMMERCE DE ', ''))

    g = root.find('dateParution')

    s_date_parution.append(g.text)

df_control = pd.DataFrame({
    'numero d identification': len(s_numero_identification),
    # 's_cp_personne' : len(s_cp_personne),
    # 's_ville_personne': len(s_ville_personne),
    'tribunal': len(s_numeroDepartement),
    'date_parution': len(s_date_parution)

}, index=["nb_lignes"]).T

#print(df_control)

df_final = pd.DataFrame({
    'Num RCS': s_numero_identification,
    'tribunal': s_numeroDepartement,
    # 'CP': s_cp_personne,
    # 'ville':s_ville_personne,
    'date de creation': s_date_parution

})

df_places = df_final["tribunal"]
# print(df_places)

print(df_final)
print(df_control)
print(df_places)
