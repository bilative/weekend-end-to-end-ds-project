import warnings

import dash
import dash_bootstrap_components as dbc
from dash_bootstrap_components._components.Button import Button
from dash_bootstrap_components._components.Card import Card
from dash_bootstrap_components._components.CardBody import CardBody
import dash_core_components as dcc
from dash_core_components.Dropdown import Dropdown
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_table

from datetime import date

REFRESH_INTERVAL = dcc.Interval(
    id='interval-component', interval=12*150005, n_intervals=0)
p1Layout = html.Div([
    dbc.Card(
        dbc.CardBody([
                dcc.Dropdown(
                                id='select-categorical',
                                value = 'Bodytype',
                                options=[
                                    {'label': 'Bodytype','value': 'Bodytype'},
                                    {'label': 'FuelType', 'value': 'FuelType'}
                                ]),
            dbc.Row([
                dbc.Col([
                    html.H2('Box Plot by Price and a Categorical Variable'),
                    dcc.Graph(id= 'first-one')
                ], width=6),
                dbc.Col([
                    html.H2('Mils of Cars by Years and Bodytypes'),
                    dcc.Graph(id = 'third-one')
                ], width=6)
            ])],style={'backgroundColor':'#c4c2b9'})

    ),
    html.Hr(),
    dbc.Card(
        dbc.CardBody([
            dbc.Col([
                html.H2('Bar Chart by Counts of a Categorical Variable by Years'),
                dcc.Graph(id='second-one')
            ])
        ],style={'backgroundColor':'#c4c2b9'})
    ),
    REFRESH_INTERVAL
], style={'background-color': '#FFFFFF'})