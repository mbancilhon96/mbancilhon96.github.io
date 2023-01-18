from dash import Dash, html, dcc,callback, Input, Output, State
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
conditionArray=random.sample(["controlPage","mainPage"],2)
# conditionArray = ["mainPage","controlPage"]
print("conditionArray is ",conditionArray)

testRecord =  {
  "userID": str(uuid.uuid1()),
  "timeRemaining": "",
  "estimateInput": "",
  "confidenceInput": "",
  "contractsOpened": "",
  "contractsReviewed": "",
  "conditionOrder":conditionArray
}



app.layout = html.Div([
    #dbc.Row(navbar),
    dcc.Store(id='userIDStore', data=testRecord),
    dcc.Store(id='controlTestOrder', data=conditionArray),
    # dcc.Store(id='userIDStore',data= testRecord),
    dcc.Location(id='url', refresh=True),
    html.Div([dbc.Progress(style={"height": "8px",'width':"400px"}, className="mb-3",id="progressBar")],
             style={'display': 'flex', 'align-items': 'center', 'justify-content': 'center','margin-top':'40px'}),
    dash.page_container,
    html.Div(id='page-content'),
])

firstPageIntro=html.Div([
    html.Div(
        [
            html.Div(children=[
                html.A(dbc.Button("Start the first task",style={"width":"300px"}), href=dash.page_registry['pages.{}'.format(conditionArray[0])]['relative_path']),
                ],style={'display':'flex','align-items':'center','justify-content': 'center','margin-top':'20px'}
            ),
        ]
    ),
])

@callback([Output('progressBar', 'value'),
            Output('page-content', 'children')],
              [Input('url', 'pathname'),
               Input('controlTestOrder', 'data')])
def display_page(pathname, conditionOrder):
    if pathname == '/':
        return 0, firstPageIntro
    elif pathname == '/secondPageIntro':
        return 33.3333,""
    elif pathname == '/mainPage':
        if conditionOrder[0] == "mainPage":
            return 16.6666,""
        elif conditionOrder[0] == "controlPage":
            return 49.9999,""
    elif pathname == '/controlPage':
        if conditionOrder[0] == "controlPage":
            return 16.6666,""
        elif conditionOrder[0] == "mainPage":
            return 49.9999,""
    elif pathname == '/lastPage':
        return 66.6666,""
    elif pathname == '/thankYouPage':
        return 100,""
    # if pathname == '/':
    #     return 0,instructions1_layout
    # elif pathname == '/TFCPracticeInstructions':
    #     return 16.6666,""
    # elif pathname == '/TFCPractice':
    #     return 24.9999,""
    # elif pathname == '/docSpectInstructions1':
    #     return 33.3333,""
    # elif pathname == '/docSpectInstructions':
    #     return 41.6666,""
    # elif pathname == '/docSpectInstructions2':
    #     return 49.9999,""
    # elif pathname == '/docSpectInstructions3':
    #     return 58.3333,""
    # elif pathname == '/docSpectInstructions4':
    #     return 66.6666,""
    # elif pathname == '/mainPage':
    #     return 74.9999,""
    # elif pathname == '/controlPage':
    #     return 83.3333,""
    # elif pathname=="/nasa-tlx":
    #     return 83.3333,""
    # elif pathname=="/customUsability":
    #     return 91.6666,""
    # elif pathname=="/demographics":
    #     return 100,""
    # elif pathname=="/lastPage":
    #     return 100,""

if __name__ == '__main__':
	app.run_server(debug=True)