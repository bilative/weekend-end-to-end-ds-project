
from dash_bootstrap_components._components.DropdownMenuItem import DropdownMenuItem
import dash_html_components as html
import dash_bootstrap_components as dbc


pageList = ['basic_dataviz', 'prediction_section']

navbar = dbc.NavbarSimple(
    children= [
        html.Img(src = 'https://user-images.githubusercontent.com/70684994/129666763-24eb8837-d544-44d5-9b5e-82d3683570e2.jpg', height= '55px'),
        dbc.DropdownMenu(
            children= [
                dbc.DropdownMenuItem('Basic Dataviz', href="/basic_dataviz"),
                dbc.DropdownMenuItem('Prediction Section', href="/prediction_section")
            ],
            nav = False,
            in_navbar= True,
            label= 'Other Pages'
        )
    ],
    brand= "Bilal's Weekend Project",
    brand_href = '#',
    color= 'primary',
    dark= True
)