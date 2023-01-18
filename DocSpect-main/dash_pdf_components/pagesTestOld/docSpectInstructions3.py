import dash
from dash import html, dcc, Input, Output, State, callback
import dash_bootstrap_components as dbc

dash.register_page(__name__, path='/docSpectInstructions3')

layout = html.Div(children=[
    html.H1(children='Training Part 2 : Estimating Contracts Total Value'),
    html.Br(),
    html.Header("The contracts total value is $"),
    #how likely is it for a 0.85 confidence value to get the wrong answer? Use data and sample using this proportion
    html.Header("You were $x from the correct answer! "),
    html.Header("It turns out that the algorithm correct identified the T for C clause in contract A and misidentified the T for C clause in contract B "),
    html.A(dbc.Button("Next"), href='/docSpectInstructions4'),

],style={'margin-left':'150px','margin-right':'150px','margin-top':'50px'})

