from __main__ import *
from api import  *

s_numero_identification = []


def get_personnes(root):
    """get personnes in avis """
    for personnes in root.iter("personnes"):
        for personne in personnes.iter('personne'):
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

    return s_numero_identification


def fill_up():
    """fill empty if no data"""
    ape.append(None)
    activite.append(None)
    adresse.append(None)

    return ape, activite, adresse