import pandas as pd

from Bodacc.__main__ import s_numero_identification, s_numeroDepartement, s_date_parution, \
    s_activite_insee
from Bodacc.funct_pool import s_activite_declaree

df_final = pd.DataFrame({
     'siren': s_numero_identification,
     'departement': s_numeroDepartement,
     'date_publication': s_date_parution,
     'activite_déclarée': s_activite_declaree,
     'code_ape': s_ape,
     'activte_insee': s_activite_insee
})
with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    df_final.to_html('temp.html')
    df_final.to_csv('data.csv', header = True, encoding= 'utf-8')
    gk = df_final.groupby('activte_insee').count().reset_index()
    try:
        gk.describe().to_html("test.html")
    except:
        pass