import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__, path='/instructions1')

layout = html.Div(children=[
    html.H1(children='Study Instructions'),

    html.Div(children='''
        Welcome to DocSpect and thank you for participating in this study. You have up to an hour to complete this task to the best of your ability. 
        Please feel free to submit your response if you are finished sooner.
    '''),
    html.A(dbc.Button("Next"), href='/TFCPracticeInstructions'),

],style={'margin-left':'150px','margin-right':'150px','margin-top':'50px'})