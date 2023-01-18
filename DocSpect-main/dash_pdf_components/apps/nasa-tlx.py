import dash
from dash import html, dcc

dash.register_page(__name__, path='/nasa-tlx')

layout = html.Div(children=[
    html.H1(children='Workload Questionnaire'),

    html.Div(children=[
        html.Div(children=[
            html.Header("How mentally demanding was the task?"),
            dcc.Slider(0, 20, 1,
                       value=10,
                       id='mentalDemand',
                        marks = {
                                    0: 'Not mentally demanding',
                                    20: 'Extremely mentally demanding',
                                },
            ),
        ]),
        html.Div(children=[
            html.Header("How physically demanding was the task?"),
            dcc.Slider(0, 20, 1,
                       value=10,
                       id='physicalDemand',
                       marks={
                           0: 'Not physically demanding',
                           20: 'Extremely physically demanding',
                       },
                       ),
        ]),
        html.Div(children=[
            html.Header("How hurried or rushed was the pace of the task?"),
            dcc.Slider(0, 20, 1,
                       value=10,
                       id='temporalDemand',
                       marks={
                           0: 'Not hurried or rushed demanding',
                           20: 'Extremely hurried or rushed demanding',
                       },
                       ),

        ]),
        html.Div(children=[
            html.Header("How successful were you in accomplishing what you were asked to do?"),
            dcc.Slider(0, 20, 1,
                       value=10,
                       id='performance',
                       marks={
                           0: 'Not successful',
                           20: 'Extremely successful',
                       },
                       ),
        ]),
        html.Div(children=[
            html.Header("How hard did you have to work to accomplish your level of performance?"),
            dcc.Slider(0, 20, 1,
                       value=10,
                       id='effort',
                       marks={
                           0: 'Not hard',
                           20: 'Extremely hard',
                       },
                       ),
        ]),
        html.Div(children=[
            html.Header("How insecure, discouraged, irritated, stressed and annoyed were you? "),
            dcc.Slider(0, 20, 1,
                       value=10,
                       id='frustration',
                        marks={
                           0: 'Not insecure',
                           20: 'Extremely insecure',
                       },
                       ),
        ]),
        html.Br(),
        html.A(html.Button("Next"), href='/usability'),

    ]),
],style={'margin-left':'150px','margin-right':'150px','margin-top':'50px'})