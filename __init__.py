from bs4 import BeautifulSoup
import requests
import tarfile
import re
import sys
import os
import pandas as pd 
import xml.etree.ElementTree as et
from collections import defaultdict


url = 'https://echanges.dila.gouv.fr/OPENDATA/BODACC/2020/'
r = requests.get(url, allow_redirects=True)
soup = BeautifulSoup(r.content, "lxml")
files = []


pages = soup.findAll('a', href=re.compile('RCS-A')) #regex to target only RCS-A files (bodacc A)
print("Total Links Found:",pages.__len__())
for l in pages:
     files.append(l.get('href'))

test = 'RCS-A_BXA20200102.taz'
url2 = f"https://echanges.dila.gouv.fr/OPENDATA/BODACC/2020/{test}"
response = requests.get(url2, stream=True)
if response.status_code == 200:
    with open(test, 'wb') as f:
        f.write(response.raw.read())

def extract_tar():
    '''Extract .tar files to .xml'''
    tar = tarfile.open(test)
    tar.extractall()
    tar.close()
extract_tar()


def get_personnes(root):
    '''get personnes in avis '''
    for personnes in root.iter("personnes"):
        for personne in personnes.iter('personne'):
            #hommage à camacho
            try:
                choix = personne.find('personnePhysique/numeroImmatriculation/numeroIdentification')
                s_numero_identification.append((choix.text).replace(' ', ''))
            except:

                try:
                        choix2 = personne.find('personneMorale/numeroImmatriculation/numeroIdentification')
                        s_numero_identification.append((choix2.text).replace(' ', ''))

                except:
                    print('Non immatriculée')
                    s_numero_identification.append(None)   

s_numero_identification = []
s_cp_personne = []
s_ville_personne = []
s_date_parution = []
s_numeroDepartement=[]

tree=et.parse('RCS-A_BXA20200102.xml')
root=tree.getroot()




for i in root.iter("avis"):
    root1 = i 
    
    x = 'MIXTE'

    get_personnes(root1)
    #get_adresse_france(root1)
    #get_adresse_france(root1) not called
    
    
    # 'tribunal' = "GREFFE DU TRIBUNAL MIXTE DE COMMERCE DE "CITY" " or "GREFFE DU TRIBUNAL DE COMMERCE DE "CITY"
    # str that must be erased to get CITY only
    n_dep = root1.find('tribunal')
    if x in n_dep.text:
        s_numeroDepartement.append((n_dep.text).replace('GREFFE DU TRIBUNAL MIXTE DE COMMERCE DE ', ''))     
    else:
        s_numeroDepartement.append((n_dep.text).replace('GREFFE DU TRIBUNAL DE COMMERCE DE ', ''))  
    
    g = root.find('dateParution')
    s_date_parution.append(g.text)        



# test lines number
# line number must be all the same len 
# line number = len(s_numeroDepartement))

df1 = pd.DataFrame({
         'numero d identification': len(s_numero_identification),
         #'s_cp_personne' : len(s_cp_personne), 
         #'s_ville_personne': len(s_ville_personne),
         'tribunal':len(s_numeroDepartement),
         'date_parution': len(s_date_parution) 
        
},index=["nb_lignes"]).T


df1

liste_test = [
s_numero_identification,
s_numeroDepartement,
s_date_parution
]

df_final = pd.DataFrame({

    'Num RCS': s_numero_identification,
    'tribunal': s_numeroDepartement,
    #'CP': s_cp_personne,         
    #'ville':s_ville_personne, 
    'date de creation':s_date_parution
             
            })

pd.to_numeric(df_final['Num RCS'], downcast='integer')

df_final['date de creation'] =  pd.to_datetime(df_final['date de creation'])

df_final['day'] = pd.DatetimeIndex(df_final['date de creation']).day
df_final['month'] = pd.DatetimeIndex(df_final['date de creation']).month
df_final['year'] = pd.DatetimeIndex(df_final['date de creation']).year
df_final['quarter'] = pd.DatetimeIndex(df_final['date de creation']).quarter

print(df_final)

(df_final.to_json(#path_or_buf = 'test.json',)
    orient='index'))
