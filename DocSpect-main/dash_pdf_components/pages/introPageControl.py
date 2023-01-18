import dash
from dash import html, dcc

dash.register_page(__name__, path='/control')

layout = html.Div(children=[
    html.H1(children='Baseline Interface Study'),
    #
    # html.Div(children='''
    #     Thank you for participating in this study. Remember that for this task, we will be recording both accuracy and completion time, so give your best estimate as fast as you can. Good luck!
    # '''),

],style={'margin-left':'150px','margin-right':'150px','margin-top':'50px'})