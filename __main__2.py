import xml.etree.ElementTree as et
import time
import glob, os
from download_extract import download, extract_tar, test
from parser import parsing
from tqdm import tqdm


"""dowloading + extracting with download_extract.py"""
download()
extract_tar(test)


os.chdir("./.")
total_entrees = 0
y = 0
nb_entree_ds_fichier = 0
nb_fil_total = 0
start_time = time.time()

for file in glob.glob("*.xml"):
    nb_fil_total += 1

#print(nb_fil_total)


for file in glob.glob("*.xml"):

    print(file)
    y +=1

    nb_entree_ds_fichier = 0

    tree = et.parse(file)
    root = tree.getroot()

    date = root.findtext('dateParution')
    x = root.findall('.//avis')



    for root1 in tqdm(root.iter("avis"), total= len(x), desc = 'Progress'):
        #print(f'FICHIER n° {y}/{nb_fil_total}')
        nb_entree_ds_fichier += 1
        total_entrees += 1
        #print(f'Entrée n°{nb_entree_ds_fichier} de {file} pour {total_entrees} entrées totales')
        liste = parsing(root1,date)


print(len(liste))

""" counter """
end_time = time.time()
temps = end_time - start_time
print(f"le temps d'execution du script est de {round(temps)} s, soit {round(temps / 60)} min , soit {round(temps/3600)} heures")




"""/!\ do not erase the import viz below > runs viz.py file"""

#import viz

"""/!\ do not erase the import viz above > runs viz.py file"""



