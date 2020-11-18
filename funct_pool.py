from __main__ import *
from api import  *
import itertools

s_numero_identification = []
s_activite = []

x = 0

def get_personnes(root):

    global x

    """get personnes in avis """
    for personnes in root.iter("personnes"):
        for personne in personnes.iter('personne'):
            x +=1
            try:
                personne.find('personneMorale/numeroImmatriculation/numeroIdentification')
                choix2 = personne.find('personneMorale/numeroImmatriculation/numeroIdentification')
                s_numero_identification.append((choix2.text).replace(' ', ''))
                print(choix2.text)

            except:

                try:
                    personne.find('personnePhysique/numeroImmatriculation/numeroIdentification')
                    choix = personne.find('personnePhysique/numeroImmatriculation/numeroIdentification')
                    s_numero_identification.append((choix.text).replace(' ', ''))
                    print(choix.text)

                except:
                    print('Non immatriculée')
                    s_numero_identification.append("None")

            print(x)

    return s_numero_identification


def get_etablissement(root):
    '''get etablissement in avis'''
    stop = 1
    k = root.find('etablissement')
    if k is None:
        s_activite.append('aucune activite')
    else:
        for etablissement in itertools.islice(root.iter('etablissement'), 0, stop):

            try:
                j = etablissement.find('activite')
                s_activite.append(j.text)
            except:
                s_activite.append('aucune activite')



    #dict_etablissement = {
        #'activite': s_activite
        #'enseigne': s_enseigne,
        #'origineFonds': s_origine_fonds,
        #'qualiteEtablissement': s_qualite_etab,
    #}




    return s_activite
