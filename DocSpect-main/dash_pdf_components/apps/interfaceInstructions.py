import dash
from dash import html, dcc

dash.register_page(__name__, path='/interfaceInstructions')

layout = html.Div(children=[
    html.H1(children='DocSpect: An Interface to Identify Termination for Convenience clauses'),

    html.Div(children='''
        Across several domains, people have to review a large number of agreements to identify T for C clauses in order to estimate the total revenue at risk. 
        This task is tedious, time-consuming and as a result, not all the contracts get reviewed. To address this issue, we developed an algorithm that than automatically detect Termination for 
        Convenience clauses across a large number of contracts. However, because of some subtleties in language, it sometimes make mistakes and misidentifies T for C clauses. 
        The algorithm will also report its confidence in the clause identification.
    '''),
    html.Br,
    html.Div(children='''
    '''),
    html.Br,
    html.Div(children='''
        For this task, pretend that your job is to review contracts using DocSpect. 
    '''),
],style={'margin-left':'150px','margin-right':'150px','margin-top':'50px'})