import warnings

import dash_daq as daq
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
p2Layout = html.Div([
    dbc.Card(
        dbc.CardBody([
            html.H1('To Predict Price of Your Car (Audi), fill the blanks please!!')
        ], style={'backgroundColor': '#B8D9FF'})
    ),
    dbc.Card(
        dbc.CardBody([
            dbc.Row([
                dbc.Col([
                    html.H5("Age of your car:"),
                    dbc.Input(
                        id="age",
                        type='number',
                        placeholder="Age of Your Car",
                                    style={'height': '50px', 'width': '500px'}
                    ),
                    html.H5("Mil of your car:"),
                    dbc.Input(
                        id="mil",
                        type='number',
                        placeholder="Mil of Your Car",
                                    style={'height': '50px', 'width': '500px'}
                    ),
                    html.H5("Bodytype of your car:"),
                    dcc.Dropdown(
                        id='bodytype',
                        placeholder='Count of Book',
                        options=[{'label': 'Wagon', 'value': 0},
                                 {'label': 'Hatchback', 'value': 1},
                                 {'label': 'Convertible', 'value': 2},
                                 {'label': 'Sedan', 'value': 3},
                                 {'label': 'Suv', 'value': 4}],
                        style={'height': '50px', 'width': '500px'}),
                    html.H5("Are there a spoiler?"),
                    dcc.RadioItems(id='spoiler',
                                   options=[
                                       {'label': 'Yes', 'value': 1},
                                       {'label': 'No', 'value': 0}
                                   ],
                                   value=1,
                                   style={'height': '50px', 'width': '500px'}
                                   ),
                    html.H5("Motor Capacity of your car:"),
                    dcc.Dropdown(
                        id='trim',
                        placeholder='Motor Capacity',
                        options=[{'label': '1.4', 'value': 1.4},
                                 {'label': '1.8', 'value': 1.8},
                                 {'label': '2.0', 'value': 2.0},
                                 {'label': '3.0', 'value': 3.0},
                                 {'label': '3.2', 'value': 3.2},
                                 {'label': '3.6', 'value': 3.6}],
                        style={'height': '50px', 'width': '500px'}),
                    dbc.Button("Predict", id='predict-button',
                               color="primary", className="mr-1")
                ], style={'float': 'center'}),
                dbc.Col(
                    dbc.Row(
                        dbc.Col(
                            id='card2',
                            children=[
                                html.H3('Predicted Price of Your Car is: ', style={
                                    'font-weight': 'bold'}),
                                html.H5("as €"),
                                daq.LEDDisplay(
                                    id='predicted-price',
                                    value=0,
                                    color='#92e0d3',
                                    backgroundColor='#1e2130',
                                    size=100
                                )
                            ]
                        )
                    ))
            ])
        ], style={'backgroundColor': '#B8D9F4'})

    ),
    REFRESH_INTERVAL
], style={'background-color': '#FFFFFF'})
