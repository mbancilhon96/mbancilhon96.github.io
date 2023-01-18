import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__, path='/TFCPracticeInstructions')

layout = html.Div(children=[
    html.H1(children='Important Definition: Termination for Convenience'),

    html.Div(children=
        '''In agreements, Termination for Convenience (T for C) clauses are intended to provide the agreeing party with the option to terminate the contract without any just cause. While Termination for Convenience provides both parties the freedom to exit the arrangement at any point in time without breaching the contract, it creates revenue uncertainty whenever payments are involved.
       '''),
    html.Br(),
    html.Div(children=
             ''' To familiarize yourself with T for C clauses, please read the following examples. On the next page, you will be tested on T for C.'''),
    html.Br(),
    html.Div(children='''Termination for Convenience Clauses''',style={'font-weight':'bold'}),
    html.Br(),
    html.Div(children='''"Notwithstanding any other provision of this Agreement, [company name] may terminate this Agreement, at any time, upon sixty (60) days' prior written notice to Licensor."'''),
    html.Br(),
    html.Div(children='''"This Agreement may be terminated by either party for any reason or no reason, whether or not extended beyond the initial term, by giving the other party written notice ninety (90) days in advance."'''),
    html.Br(),
    html.Div(children='''NOT Termination for Convenience Clauses''',style={'font-weight':'bold'}),
    html.Br(),
    html.Div(children='''"This Agreement may be terminated by either party at the expiration of its term or any renewal term upon thirty (30) days written notice to the other party."'''),
    html.Br(),
    html.Div(children='''"...[company name] agrees that for a period of ninety (90) days prior to the expiration of the Term (unless the Agreement is terminated by Wade as permitted hereunder), [company name] shall have the exclusive right to negotiate for continued endorsement by Athlete of the [company name] Products.'"'''),
    html.Br(),
    html.Div(children='''"Thereafter, this Agreement shall automatically continue in effect until either party gives the other at least six (6) months prior written notice of termination."'''),
    html.Br(),
    html.A(dbc.Button("Next"), href='/TFCPractice'),
    html.Br(),
],style={'margin-left':'150px','margin-right':'150px','margin-top':'50px'})

