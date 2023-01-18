import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__, path='/customUsability')

layout = html.Div(children=[
    html.H1(children='Usability Questionnaire'),
    html.Div(
        [
            dbc.Label("I think that I would like to use DocSpect frequently"),
            dbc.RadioItems(
                options=[
                    {"label": "Strongly Disagree", "value": 1},
                    {"label": "Disagree", "value": 2},
                    {"label": "Neutral", "value": 3},
                    {"label": "Agree", "value": 4},
                    {"label": "Strongly Agree", "value": 4},
                ],
                value="",
                id="q1",
                inline=True,
            ),
        ]
    ),
    html.Br(),

    html.Div(
        [
            dbc.Label("I found DocSpect unnecessarily complex"),
            dbc.RadioItems(
                options=[
                    {"label": "Strongly Disagree", "value": 1},
                    {"label": "Disagree", "value": 2},
                    {"label": "Neutral", "value": 3},
                    {"label": "Agree", "value": 4},
                    {"label": "Strongly Agree", "value": 4},
                ],
                value="",
                id="q2",
                inline=True,
            ),
        ]
    ),
    html.Br(),

    html.Div(
        [
            dbc.Label("I thought DocSpect was easy to use"),
            dbc.RadioItems(
                options=[
                    {"label": "Strongly Disagree", "value": 1},
                    {"label": "Disagree", "value": 2},
                    {"label": "Neutral", "value": 3},
                    {"label": "Agree", "value": 4},
                    {"label": "Strongly Agree", "value": 4},
                ],
                value="",
                id="q3",
                inline=True,
            ),
        ]
    ),
    html.Br(),

    html.Div(
        [
            dbc.Label("I think that I would need the support of a technical person to be able to use DocSpect."),
            dbc.RadioItems(
                options=[
                    {"label": "Strongly Disagree", "value": 1},
                    {"label": "Disagree", "value": 2},
                    {"label": "Neutral", "value": 3},
                    {"label": "Agree", "value": 4},
                    {"label": "Strongly Agree", "value": 4},
                ],
                value="",
                id="q4",
                inline=True,
            ),
        ]
    ),
    html.Br(),

    html.Div(
        [
            dbc.Label("I found the various functions in this DocSpect were well integrated."),
            dbc.RadioItems(
                options=[
                    {"label": "Strongly Disagree", "value": 1},
                    {"label": "Disagree", "value": 2},
                    {"label": "Neutral", "value": 3},
                    {"label": "Agree", "value": 4},
                    {"label": "Strongly Agree", "value": 4},
                ],
                value="",
                id="q5",
                inline=True,
            ),
        ]
    ),
    html.Br(),
    html.Div(
        [
            dbc.Label("I thought there was too much inconsistency in DocSpect."),
            dbc.RadioItems(
                options=[
                    {"label": "Strongly Disagree", "value": 1},
                    {"label": "Disagree", "value": 2},
                    {"label": "Neutral", "value": 3},
                    {"label": "Agree", "value": 4},
                    {"label": "Strongly Agree", "value": 4},
                ],
                value="",
                id="q6",
                inline=True,
            ),
        ]
    ),
    html.Br(),
    html.Div(
        [
            dbc.Label("I imagine that most people would learn to use DocSpect very quickly."),
            dbc.RadioItems(
                options=[
                    {"label": "Strongly Disagree", "value": 1},
                    {"label": "Disagree", "value": 2},
                    {"label": "Neutral", "value": 3},
                    {"label": "Agree", "value": 4},
                    {"label": "Strongly Agree", "value": 4},
                ],
                value="",
                id="q7",
                inline=True,
            ),
        ]
    ),
    html.Br(),
    html.Div(
        [
            dbc.Label("I found DocSpect very cumbersome to use."),
            dbc.RadioItems(
                options=[
                    {"label": "Strongly Disagree", "value": 1},
                    {"label": "Disagree", "value": 2},
                    {"label": "Neutral", "value": 3},
                    {"label": "Agree", "value": 4},
                    {"label": "Strongly Agree", "value": 4},
                ],
                value="",
                id="q8",
                inline=True,
            ),
        ]
    ),
    html.Br(),

    html.Div(
        [
            dbc.Label("I felt very confident using DocSpect."),
            dbc.RadioItems(
                options=[
                    {"label": "Strongly Disagree", "value": 1},
                    {"label": "Disagree", "value": 2},
                    {"label": "Neutral", "value": 3},
                    {"label": "Agree", "value": 4},
                    {"label": "Strongly Agree", "value": 4},
                ],
                value="",
                id="q9",
                inline=True,
            ),
        ]
    ),
    html.Br(),
    html.Div(
        [
            dbc.Label("I needed to learn a lot of things before I could get going with DocSpect."),
            dbc.RadioItems(
                options=[
                    {"label": "Strongly Disagree", "value": 1},
                    {"label": "Disagree", "value": 2},
                    {"label": "Neutral", "value": 3},
                    {"label": "Agree", "value": 4},
                    {"label": "Strongly Agree", "value": 4},
                ],
                value="",
                id="q10",
                inline=True,
            ),
        ]
    ),
    html.Br(),
    html.A(html.Button("Next"), href='/demographics'),
    html.Br(),

],style={'margin-left':'150px','margin-right':'150px','margin-top':'50px'})