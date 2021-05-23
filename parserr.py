import xml.etree.ElementTree as et
import os
import time
from api import api_request

os.chdir("./.")

liste = []


def parsing(root1,date):


    """" recuperation siren """



    if root1.findtext('personnes/personne/personneMorale/numeroImmatriculation/numeroIdentification') is None:
        siren = root1.findtext('personnes/personne/personnePhysique/numeroImmatriculation/numeroIdentification')
    else:
        siren = root1.findtext('personnes/personne/personneMorale/numeroImmatriculation/numeroIdentification')


    try:
        siren2 = siren.replace(' ', '')
    except:
        print(siren)
        siren2 = "non immatricule"

    temp = root1.findtext('personnes/personne/adresse/france/codePostal')

    """ recuperation forme entreprise"""

    if root1.findtext('personnes/personne/personneMorale/formeJuridique') is None:
        forme_juridique = 'Entreprise Individuelle'
    else:
        forme_juridique = root1.findtext('personnes/personne/personneMorale/formeJuridique')

    if root1.findtext('etablissement/activite') is None:
        activite_declaree = "pas d'activite"
    else:
        activite_declaree = root1.findtext('etablissement/activite')

    if root1.findtext('etablissement/adresse/codePostal') is None:
        code_postal = temp
    else:
        code_postal = root1.findtext('etablissement/adresse/codePostal')

    if root1.findtext('acte/creation/dateImmatriculation') is None:
        if root1.findtext('acte/immatriculation/dateImmatriculation') is None:
            if root1.findtext('acte/vente/dateImmatriculation') is None:
                date_immat = date
            else:
                date_immat = root1.findtext('acte/vente/dateImmatriculation')
        else:
            date_immat = root1.findtext('acte/immatriculation/dateImmatriculation')
    else:
        date_immat = root1.findtext('acte/creation/dateImmatriculation')

    time.sleep(0.15)
    activite_insee, code_ape = api_request(siren2)



    liste.append(

        {'type' : 'creation',
         'siren': siren2,
         'forme_juridique' : forme_juridique,
         'activite': activite_declaree,
         'activite_insee' : activite_insee,
         'code_ape' : code_ape,
         'code_postal': code_postal,
         'date_immat' :date_immat
         }
    
    )

    return liste


