import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from numpy.lib.function_base import select
import plotly.express as px
import warnings
from datetime import date

from libs.views.design import *
from libs.views.p1 import *
from libs.views.p2 import *
from libs.helpers import *
from libs.dbConn import *

warnings.filterwarnings('ignore')



app = dash.Dash(external_stylesheets=[dbc.themes.SANDSTONE])
app.config.suppress_callback_exceptions = True
content = html.Div(id="page-content")
app.layout = html.Div(
    [dcc.Location(id="url"), navbar, content])

##############################################
################# PAGE 1 #####################
##############################################



@app.callback([Output("first-one", "figure"),
                Output("second-one", "figure"),
                Output("third-one", "figure")],
              [Input("interval-component", "n_clicks"),
              Input("select-categorical", "value")])
def toggle_active_links(n_clicky, category):
    df = read_all()
    boxy = px.box(df, x= category, y = 'Price', color = 'Spoiler')

    barry = px.bar(x=df['Year'],
                y=df['counts'],
                color=df[category],
                barmode= 'group'
                )

    scatty = px.scatter(df, x= 'Year', y= 'Mil', color= 'Bodytype')
    return boxy, barry, scatty


##############################################
################# PAGE 2 #####################
##############################################

@app.callback(Output("predicted-price", "value"),
              [Input("age", "value"),
              Input("mil", "value"),
              Input("bodytype", "value"),
              Input("spoiler", "value"),
              Input("trim", "value"),
              Input("predict-button", "n_clicks")])
def toggle_active_links(age, mil, bodytype, spoiler, trim, clicky):
    
    isTrue = predictBUTTON.isNew(clicky)
    if isTrue:
        try:
            predicted_price = restPred(age, mil, bodytype, spoiler, trim)    
            return predicted_price
        except:
            return 404
    return 0

##############################################
################### END ######################
##############################################


@app.callback([Output(f"{i}-link", "active") for i in pageList],
              [Input("url", "pathname")],
              )
def toggle_active_links(pathname):
    if pathname == "/":
        # Treat page 1 as the homepage / index
        return True, False
    return [pathname == f"/{i}" for i in pageList]


@app.callback(Output("page-content", "children"),
              [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname in ["/", "/basic_dataviz"]:
        return p1Layout
    elif pathname == "/prediction_section":
        return p2Layout

    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"This page is not available..."),
        ]
    )


if __name__ == "__main__":
    app.run_server(debug=False, port=8050, host="0.0.0.0")