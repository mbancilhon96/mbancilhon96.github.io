import dash
from dash import html, dcc, Input, Output, State, callback
import dash_bootstrap_components as dbc

dash.register_page(__name__, path='/docSpectInstructions4')

layout = html.Div(children=[
    html.H1(children='Training Part 3 : Using DocSpect'),
    html.Br(),
    html.Header("Now that you have completed the training, you will be asked to estimate the total revenue at risk across 20 contracts in 4 "
                "minutes. The closer you are to the correct estimate, the larger your bonus will be."
                " You will likely not have enough time to manually inspect all contracts so make sure you use the impact factor to prioritize the reivews."
                "Make use of the graph to know the possible range for the estimate."),
    html.Br(),
    html.Header("Look at the following instructions to understand how to use DocSpect."),
    html.A(dbc.Button("Next"), href='/mainPage'),

],style={'margin-left':'150px','margin-right':'150px','margin-top':'50px'})