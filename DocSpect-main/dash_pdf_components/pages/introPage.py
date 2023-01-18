import dash
from dash import Dash, html, dcc,callback, Input, Output, State, ctx
import dash_bootstrap_components as dbc
import numpy as np

dash.register_page(__name__, path='/')


layout = html.Div(children=[
    html.Div(
        [
            html.H2(children='DocSpect Interface'),
            html.Header("Please enter your user testing ID before starting this task."),
            dbc.Input(id="userTestingID", type="text"),
            html.Div(children=[
                html.A(dbc.Button("Start the task", style={"width": "300px"}, id="startTaskBtn"),
                       id="interfaceHref"),
            ], style={'display': 'flex', 'align-items': 'center', 'justify-content': 'center', 'margin-top': '20px'}
            ),
        ], style={'margin-left': '150px', 'margin-right': '150px', 'margin-top': '50px'}
    ),
],style={'margin-left':'150px','margin-right':'150px','margin-top':'50px'})

@callback(Output("interfaceHref","href"),
          Input("conditionData","data"))
def passInterfaceUrl(condition):
    print("condition is ",condition)
    if condition=="control":
        return  "/controlPage"
    elif condition=="test":
        return "/mainPage"

@callback(Output("userIDStore","data"),
          [Input("startTaskBtn","n_clicks_timestamp"),
          State("userTestingID","value")])
def saveTestingID(startTaskBtn,userTestingID):
    print("inside save testing ID")
    elementTriggered = ctx.triggered_id

    button_pressed = np.nanargmax(
        np.array(
            [0, startTaskBtn], dtype=np.float64
        ))

    if button_pressed ==1:
        testRecord = {
            "userID": str(userTestingID),
        }
        print("test record is ",testRecord)
        return testRecord