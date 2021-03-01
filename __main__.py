import xml.etree.ElementTree as et
import time
import glob, os
from api import s_activite_insee, s_ape
from funct_pool import s_activite_declaree, get_personnes

s_numeroDepartement = []
s_date_parution = []
s_error = []

os.chdir("./.")
total_entrees = 0
y = 0
nb_entree_ds_fichier = 0
nb_fil_total = 0
start_time = time.time()

for file in glob.glob("*.xml"):
    nb_fil_total += 1
print(nb_fil_total)

for file in glob.glob("*.xml"):

    print(file)
    y +=1

    nb_entree_ds_fichier = 0

    try:
        tree = et.parse(file)
        root = tree.getroot()

        try:
            date = root.find('dateParution').text
            print(date)

        except:
            s_date_parution.append("pas de date")


        try:
            for root1 in root.iter("avis"):
                print(f'FICHIER n° {y}/{nb_fil_total}')
                time.sleep(0.15)
                nb_entree_ds_fichier += 1
                total_entrees += 1
                print(f'Entrée n°{nb_entree_ds_fichier} de {file} pour {total_entrees} entrées totales')
                s_numero_identification = get_personnes(root1)
                s_date_parution.append(date)

                n_dep = root1.find('numeroDepartement')
                if n_dep is None:
                    s_numeroDepartement.append('None')
                else:
                    s_numeroDepartement.append(n_dep.text)

                print(
                 len(s_activite_declaree),
                 len(s_numero_identification),
                 len(s_numeroDepartement),
                 len(s_activite_insee),
                 len(s_ape))


                if len(s_activite_declaree) != total_entrees \
                    or len(s_numero_identification) != total_entrees \
                    or len(s_numeroDepartement) != total_entrees\
                    or len(s_activite_insee) != total_entrees\
                    or len(s_ape)!= total_entrees:

                    break

                print("*_*_"*10)
        except:
            print('gg')

    except:
        print(f'{file} could not be parsed')
        s_error.append(file)
print(s_error)

""" counter """
end_time = time.time()
temps = end_time - start_time
print(F"le temps d'execution du script est de {round(temps)} s, soit {round(temps / 60)} min , soit round(temps)/360 heures")

print( f'nombre Act déclarée: {len(s_activite_declaree)} nombre num id {len(s_numero_identification)} '
       f'n° dep {len(s_numeroDepartement)}, nb acti insee {len(s_activite_insee)}, nb APE {len(s_ape)}')






