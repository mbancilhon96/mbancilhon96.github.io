import dash
from dash import html, dcc
from dash import html, Input, Output, State, callback_context, dash_table,callback,ctx
import dash_bootstrap_components as dbc

dash.register_page(__name__, path='/secondPageIntro')

nextHref=""

@callback(
    Output("secondTaskLink", 'href'),
    Input("controlTestOrder", "data")
)
def findOrder(controlTestOrder):
    if controlTestOrder[1]=="controlPage":
        nextHref="/controlPage"
    elif controlTestOrder[1]=="mainPage":
        nextHref="/mainPage"

    print("next Href is ",nextHref)
    return nextHref

layout = html.Div([
            html.Div(children='''
            Remember that accuracy and completion time will be recorded for this task as well. Please click start whenever you are ready to start the second task. 
        '''),
            html.Div([
                html.A(dbc.Button('Start the second task', style={"width": "300px"}, id='startSecondTask', n_clicks=0),
                       id="secondTaskLink")
                ], style={'display': 'flex', 'justifyContent': 'center'})
            ])

# html.Div([
#     html.Div(
#         [
#             html.Div([
#                 html.A(dbc.Button("Start the second task",style={"width":"300px"}), id="secondTaskLink"),
#                 ],style={'display':'flex','align-items':'center','justify-content': 'center','margin-top':'20px'}
#             ),
#         ]
#     ),
# ])

