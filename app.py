import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
# from sqlalchemy import create_engine
# from config import name, user, password, host
# from request import request, production_france, export_mondial_charbon
import dash_html_components as html
from dataframe import *
""" stylesheet on codepen """
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

""" Use class Dash and connect to teh server """
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

""" connect to my AWS DB """
# conn = create_engine(f'postgresql://{user}:{password}@{host}/{name}')
# df = pd.read_sql(request, conn)
# df_production_france = pd.read_sql(production_france, conn)
# df_export_mondial_charbon = pd.read_sql(export_mondial_charbon, conn)
# print(export_mondial_charbon)

""" create fig with plotly """
fig = px.bar(data, x="date_publication", y="code_ape", color="departement", template='plotly_dark')
# fig2 = px.bar(df_production_france, x="years", y="values", color="products", template='plotly_dark')
# fig3 = px.bar(df_export_mondial_charbon, x="year", y="value", color="countries", template='plotly_dark')

""" html display """
# app.layout = html.Div(children=[
#     html.H1(children='TRANSITION ENERGETIQUE'),
#     html.Div(children=''' Importation des énergies renouvelables'''),
#     dcc.Graph(className='row', id='example-graph', figure=fig),
#     html.Div(children=''' Production française'''),
#     dcc.Graph(className='row', id='example-graph-2', figure=fig2),
# ])


app.layout = html.Div([
    html.Div([
        # html.Div([
        # html.Div([
            html.H3('TRANSITION ENERGETIQUE'),
            dcc.Graph(className='row', id='example-graph', figure=fig)
        ], className="six columns"),

    #     html.Div([
    #         html.H3('production des energies en France'),
    #         dcc.Graph(className='row', id='example-graph-2', figure=fig2)
    #     ], className="six columns"),
    # ], className="row")

    #     html.Div([
    #         html.H3('production des energies en France'),
    #         dcc.Graph(className='row', id='example-graph-3', figure=fig3)
    #     ], className="six columns"),
    # ], className="row")
])

if __name__ == '__main__':
    app.run_server(debug=True)
