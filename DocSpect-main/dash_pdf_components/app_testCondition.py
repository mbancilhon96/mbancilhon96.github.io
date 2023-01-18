from dash import Dash, html, dcc,callback, Input, Output, State, ctx
import dash
import dash_bootstrap_components as dbc
import uuid
import numpy as np
import random
import json
from json import JSONEncoder


app = Dash(__name__, 
    use_pages=True,
    external_scripts=['https://documentcloud.adobe.com/view-sdk/viewer.js']
)

#app.css.append_css({'external_url': '/assets/styleDash.css'})

CONCORD_LOGO = app.get_asset_url("images/concord-logo-dark.png")

uniqueId = uuid.uuid1()

navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(html.Img(src=CONCORD_LOGO, height="30px"), id="col-logo"),
                    ],
                    align="center",
                    className="navbar-logo-row",
                ),
                href="#"
            )
        ],
        id="navbar-container"
    ),
    color="dark",
    dark=True,
)

app.layout = html.Div([
    #dbc.Row(navbar),
    dcc.Store(id='userIDStore',storage_type='session'),
    dcc.Store(id='conditionData', storage_type='session',data="test"),
    html.H1("Test",id="testStore"),
    dcc.Location(id='url', refresh=True),
    html.Div([dbc.Progress(style={"height": "8px",'width':"400px"}, className="mb-3",id="progressBar")],
             style={'display': 'flex', 'align-items': 'center', 'justify-content': 'center','margin-top':'40px'}),
    dash.page_container,
])

@callback(Output("testStore","children"),
          Input("userIDStore","data"))
def updateTestingIDLabel(userTestingID):
    print("inside update testing ID label")
    if userTestingID is None:
        return ""
    else: return "User testing id: "+str(userTestingID['userID'])

@callback(Output('progressBar', 'value'),
              [Input('url', 'pathname')])
def updateProgressBar(pathname):
    if pathname == '/':
        return 0
    elif pathname == '/mainPage':
            return 50
    elif pathname == '/thankYouPage':
        return 100

if __name__ == '__main__':
	app.run_server(debug=True)