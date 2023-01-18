import dash
from dash import html, dcc

dash.register_page(__name__, path='/lastPage')

layout = html.Div(children=[
    html.H1(children='Thank you!'),

    html.Div(children='''
        Thank you for taking this survey! Please paste the following code into Prolific to receive compensation: 'uniqueCode'
    '''),
],style={'margin-left':'150px','margin-right':'150px','margin-top':'50px'})