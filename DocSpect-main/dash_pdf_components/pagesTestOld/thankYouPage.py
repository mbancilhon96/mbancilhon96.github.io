import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__, path='/thankYouPage')

layout = html.Div(children=[
    html.H1(children='Thank you!'),
    html.Div(children='''
        Thank you for taking this survey! Please head back to the main survey for some questions about this task.
    '''),
],style={'margin-left':'150px','margin-right':'150px','margin-top':'50px'})

