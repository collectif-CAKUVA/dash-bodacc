from dataframe import *
import dash
import dash_core_components as dcc
import plotly.express as px
import dash_html_components as html

""" 
graph 1 --> date + activite + code APE 
Data:
--> date sur au moins 1 mois
--> code APE
--> activite de l'insee
"""

""" création de dataframe et du graph --> Dash / plotly"""
app = dash.Dash(__name__)
# print(df)
fig = px.line(df2, x="date_publication", y="size", color="code_ape", template='plotly_dark')

""" html display """
app.layout = html.Div(children=[
    dcc.Graph(className='row', id='example-graph', figure=fig),
])

""" run app"""
if __name__ == '__main__':
    app.run_server(debug=True)
