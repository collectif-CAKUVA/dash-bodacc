import pandas as pd

from __main__ import s_numero_identification, s_numeroDepartement, s_date_parution, \
    s_activite_insee
from api import s_ape
from funct_pool import s_activite_declaree

df_final = pd.DataFrame({
     'siren': s_numero_identification,
     'departement': s_numeroDepartement,
     'date_publication': s_date_parution,
     'activite_déclarée': s_activite_declaree,
     'code_ape': s_ape,
     'activte_insee': s_activite_insee
})

df_ml = pd.DataFrame({
    'activite': s_activite_declaree,
    'code_ape': s_ape
})


with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    df_final.to_html('temp.html')
    df_final.to_csv('data.csv', header = True, encoding= 'utf-8')
    df_ml.to_csv('raw_data.csv', header = True, encoding = 'utf_8')