import xml.etree.ElementTree as et
import csv
import time
import glob, os
from download_extract import download, extract_tar, test
from parserr import parsing
from tqdm import tqdm

"""dowloading + extracting with download_extract.py"""
#download()
#extract_tar(test)


os.chdir("./.")
total_entrees = 0
y = 0
nb_entree_ds_fichier = 0
nb_fil_total = 0

""" chrono on """
start_time = time.time()


""" .xml file counter """
for file in glob.glob("*.xml"):
    nb_fil_total += 1
print(nb_fil_total)


liste = []

for file in glob.glob("*.xml"):

    print(file)
    y +=1

    nb_entree_ds_fichier = 0

    tree = et.parse(file)
    root = tree.getroot()

    date = root.findtext('dateParution')
    x = root.findall('.//avis')

    for root1 in tqdm(root.iter("avis"), total=len(x), desc='Progress'):
        #print(f'FICHIER n° {y}/{nb_fil_total}')
        nb_entree_ds_fichier += 1
        total_entrees += 1
        #print(f'Entrée n°{nb_entree_ds_fichier} de {file} pour {total_entrees} entrées totales')
        liste = parsing(root1, date)

    #database.add_entreprise(liste)

""" time counter """
end_time = time.time()
temps = end_time - start_time
print(f"le temps d'execution du script est de {round(temps)} s, soit {round(temps / 60)} min , soit {round(temps/3600)} heures")


""" export dic list to csv"""
keys = liste[0].keys()
with open('data_test.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(liste)




