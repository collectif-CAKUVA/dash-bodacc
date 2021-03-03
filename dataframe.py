import pandas as pd
# import pprint

"""
Index(['Unnamed: 0', 'siren', 'departement', 'date_publication',
       'activite_déclarée', 'code_ape', 'activte_insee'],
      dtype='object')
"""

""" transforme CSV to dataframe  """
df = pd.read_csv("bodacc_janvier_fevrier.csv")
#print(df.columns)

df2 = df.groupby(['code_ape', 'activte_insee', 'date_publication'], as_index=False).size()
df2['size']
df3 = df2.sort_values(by='size', ascending=False)
df4 = df3.head(5)
print(df4)