import dash
from dash import html, dcc

dash.register_page(__name__, path='/interfaceTutorial')

layout = html.Div(children=[
    html.H1(children='Study Instructions'),

    html.Div(children='''
        Watch the following short videos to understand how to use DocSpect. 
    '''),
],style={'margin-left':'150px','margin-right':'150px','margin-top':'50px'})