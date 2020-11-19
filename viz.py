import pandas as pd
from tabulate import tabulate
from Bodacc.__main__ import s_numero_identification, s_numeroDepartement, s_date_parution, s_activite_declaree, \
    s_activite_insee

df_final = pd.DataFrame({
     'siren': s_numero_identification,
     'departement': s_numeroDepartement,
     'date_publication': s_date_parution,
     'activite_déclarée': s_activite_declaree,
     'activte_insee': s_activite_insee
})
with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
    df_final.to_html('temp.html')
    gk = df_final.groupby('activte_insee')
    try:
        print(gk.describe())
        gk.describe().to_html("test.html")
    except:
        pass