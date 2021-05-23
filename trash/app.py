from dataframe import *
import dash
import dash_core_components as dcc
import plotly.express as px
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as go

""" 
graph 1 --> date + activite + code APE 
Data:
--> date sur au moins 1 mois
--> code APE
--> activite de l'insee
"""

# ['code_ape', 'activte_insee', 'date_publication', 'size']

""" création de dataframe et du graph --> Dash / plotly"""
app = dash.Dash(__name__)
# print(df)
fig = px.line(df_final, x="date_publication", y="size", color="code_ape",
              line_group='activte_insee', template='plotly_dark')

""" html display """
app.layout = html.Div(children=[
    dcc.Dropdown(id='selector', options=[{'label': 'CODE APE', 'value': 'code_ape'},
                                         {'label': 'INSEE', 'value': 'activte_insee'}],
                 className='selector'),
    dcc.Graph(className='row', id='bodacc-graph', figure=fig)
])


@app.callback(
    Output('bodacc-graph', 'figure'),
    Input('selector', 'value'))
def update_graph(value):
    figure = px.line(df_final, x="date_publication", y="size", color=value,
                     line_group='activte_insee', template='plotly_dark')
    return figure

""" run app"""
if __name__ == '__main__':
    app.run_server(debug=True)
