from bs4 import BeautifulSoup
import requests
import tarfile
import re
import sys
import os
import pandas as pd 
import xml.etree.ElementTree as et
from collections import defaultdict
import matplotlib.pyplot as plt


from download_extract import download, extract_tar
from funct_pool import get_personnes 

plt.rcParams.update({'font.size': 15})

test = ''

download()
extract_tar()

#XML parsing func



s_cp_personne = []
s_ville_personne = []
s_date_parution = []
s_numeroDepartement=[]

tree=et.parse('RCS-A_BXA20200102.xml')
root=tree.getroot()



#main parsing process
for i in root.iter("avis"):
    root1 = i 
    
    x = 'MIXTE'
    s_numero_identification = get_personnes(root1)

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




df_control = pd.DataFrame({
         'numero d identification': len(s_numero_identification),
         #'s_cp_personne' : len(s_cp_personne), 
         #'s_ville_personne': len(s_ville_personne),
         'tribunal':len(s_numeroDepartement),
         'date_parution': len(s_date_parution) 
        
},index=["nb_lignes"]).T


print(df_control)

df_final = pd.DataFrame({
             'Num RCS': s_numero_identification,
             'tribunal': s_numeroDepartement,
             #'CP': s_cp_personne,
                         
             #'ville':s_ville_personne, 
             'date de creation':s_date_parution
             
            })

print(df_final)