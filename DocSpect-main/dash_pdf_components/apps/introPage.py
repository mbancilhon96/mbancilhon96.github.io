import dash
from dash import html, dcc

dash.register_page(__name__, path='/')

layout = html.Div(children=[
    html.H1(children='Welcome!'),

    html.Div(children='''
        Thank you for participating in this study. By agreeing to participate, you consent to the use of your data for research purposes. No identifiable information will be collected.
    '''),

],style={'margin-left':'150px','margin-right':'150px','margin-top':'50px'})