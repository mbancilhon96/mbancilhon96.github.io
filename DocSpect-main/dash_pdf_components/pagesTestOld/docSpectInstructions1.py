import dash
from dash import html, dcc, dash_table, Input, Output, State, callback
import dash_bootstrap_components as dbc

dash.register_page(__name__, path='/docSpectInstructions1')

layout = html.Div(children=[
    html.H1(children='Experiment Instructions'),

    html.Div(children='''
       Professionals often have to review a large number of agreements to identify T for C clauses in order to estimate the maximum total revenue at risk. 
       To assist them, we developed an algorithm that automatically detects Termination for 
    Convenience clauses in agreements. However, the algorithm sometimes makes mistakes and misidentifies other clauses to be Termination for Convenience Clauses.  
    Your task will be to estimate the total value for contracts with T for C clauses. We will provide you with the contracts for which the algorithm detected a T for C clause, the contract value in dollars ($) and the algorithm's confidence in the T for C detection. But in order to provide an accurate estimate, you might have to manually review some contracts.
'''),
    html.Br(),
    html.Header("Your bonus for this task will depend on how close your estimate is to the correct amount. If your estimate is correct, you win a bonus of $5. If your estimate is within 10% of the correct answer, you win $4, and so on. "),
    html.Br(),
    html.A(dbc.Button("Next",id="nextDocSpect"), href='/docSpectInstructions'),
    html.Br(),

],style={'margin-left':'150px','margin-right':'150px','margin-top':'50px'})


