import pandas as pd
# import pprint

"""
Index(['Unnamed: 0', 'siren', 'departement', 'date_publication',
       'activite_déclarée', 'code_ape', 'activte_insee'],
      dtype='object')
"""

""" transforme CSV to dataframe  """
df = pd.read_csv("bodacc_janvier_fevrier.csv")

df_p = df.groupby(['code_ape']).size().sort_values(ascending=False).head(12)


#df2 = df.groupby(['code_ape', 'activte_insee', 'date_publication'], as_index=False).size()


df_top = df.loc[df.code_ape.isin(df_p.index), ['code_ape', 'date_publication', 'activte_insee']]
print(df_top.code_ape.unique())
df_final = df_top.groupby(['code_ape', 'activte_insee', 'date_publication'], as_index=False).size()
print(df_final)




# df_top = df2[(df2['code_ape'] == '68.20B') & (df2['code_ape'] == '53.20Z') & (df2['code_ape'] == '70.10Z')
# & (df2['code_ape'] == '56.10C')]


# print(df_top)
# df_top = df2[(df2['size'] > 100)]


