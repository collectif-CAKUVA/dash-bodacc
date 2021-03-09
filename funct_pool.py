"""

parsing module

"""


import itertools
from api import api_request, s_activite_insee, s_ape

s_date_publication = []
s_numero_identification = []
s_activite_declaree = []
s_code_postal = []

def get_etablissement(root):

    '''get etablissement in avis'''
    stop = 1
    k = root.find('etablissement')
    if k is None:
        s_activite_declaree.append('aucune activite')
        s_code_postal.append("cp non renseigne")
        print('aucune activite')
        print('cp non renseigne')
    else:
        for etablissement in itertools.islice(root.iter('etablissement'), 0, stop):

            try:
                j = etablissement.find('activite')
                s_activite_declaree.append(j.text)
                print(j.text)
            except:
                s_activite_declaree.append('aucune activite')
                print('aucune activite')

            try:
                cp = etablissement.find('adresse/codePostal')
                s_code_postal.append(cp.text)
                print(cp.text)

            except:
                s_code_postal.append('non renseigne')
                print("non renseigne")

    return s_activite_declaree,s_code_postal

def get_personnes(root):
    stop = 1
    global s_activite_declaree
    global s_code_postal
    etablissement = root.find("etablissement")
    if etablissement is None:
        s_activite_declaree.append("non renseignee")
        print('non renseignee')
        s_code_postal.append('non renseigne')
        print("non renseigne")
    else:
        get_etablissement(root)
    """get personnes in avis """
    for personnes in root.iter("personnes"):
        for personne in itertools.islice(personnes.iter('personne'), 0, stop):


            try:
                personne.find('personneMorale/numeroImmatriculation/numeroIdentification')
                choix2 = personne.find('personneMorale/numeroImmatriculation/numeroIdentification')
                x = choix2.text.replace(' ', '')
                s_numero_identification.append(x)
                api_request(x)
                print(f'SIREN:{x}')

            except:

                try:
                    personne.find('personnePhysique/numeroImmatriculation/numeroIdentification')
                    choix = personne.find('personnePhysique/numeroImmatriculation/numeroIdentification')
                    y = choix.text.replace(' ', '')
                    s_numero_identification.append(y)
                    api_request(y)
                    print(f'SIREN:{y}')

                except:
                    print('Non immatriculée')
                    s_numero_identification.append("Non immatricule")
                    s_activite_insee.append('Non immatricule')
                    s_ape.append('Non immatricule')

            #print(x)

    return s_numero_identification





