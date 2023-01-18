import dash
from dash import html, dcc

dash.register_page(__name__, path='/demographics')

layout = html.Div(children=[
    html.H1(children='Demographics'),

    html.Div(children=[
        html.Div(children=[
            html.Header("Gender"),
            dcc.Dropdown(['Male', 'Female', 'Other','Prefer not to say'], 'Male'),
            html.Header("Age"),
            dcc.Dropdown(list([x for x in range(18, 65)]), 18),
            html.Header("Level of Education"),
            dcc.Dropdown(['High School', 'Undergraduate', 'Graduate','Other','Prefer not to say'], 'High School'),
            html.Br(),
            html.A(html.Button("Submit"), href='/lastPage'),
        ])
    ]),
],style={'margin-left':'150px','margin-right':'150px','margin-top':'50px'})