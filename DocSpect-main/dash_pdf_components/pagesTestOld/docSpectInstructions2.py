import dash
from dash import html, dcc, Input, Output, State, callback
import dash_bootstrap_components as dbc

dash.register_page(__name__, path='/docSpectInstructions2')

table_header = [
    html.Thead(html.Tr([html.Th("Company Name"), html.Th("T for C"), html.Th("T for C confidence"),  html.Th("Value ($)"), html.Th("Impact"),html.Th("Reviewed")
    ]))
]
row1 = html.Tr([html.Td("Company A"), html.Td("Yes"), html.Td("1.0"),html.Td("900,000"),html.Td("27,000"),html.Td("Yes")],style={'color':'green'})
row2 = html.Tr([html.Td("Company B"), html.Td("No"), html.Td("1.0"),html.Td("90,000"),html.Td("25,200"),html.Td("Yes")],style={'color':'red'})
row3 = html.Tr([html.Td("Company C"), html.Td("Yes"), html.Td("0.85"),html.Td("150,000"),html.Td("22,500"),html.Td("No")])
row4 = html.Tr([html.Td("Company D"), html.Td("Yes"), html.Td("0.95"),html.Td("60,000"),html.Td("3000"),html.Td("No")])

table_body = [html.Tbody([row1, row2, row3, row4])]

layout = html.Div(children=[
    html.H1(children='Training Part 2 : Estimating Contracts Total Value'),

    html.Div(children='''
       Let's say that after reviewing Contract A and B, you find that:
   '''),
    html.Div(children="The algorithm was correct for Company A, the clause it identified was a T for C clause.", id="correctContract",style={"color":"green"}),
    html.Div(children="The algorithm was wrong for Company B, the clause it identified was NOT a T for C clause.",id="incorrectContract",style={"color":"red"}),
    html.Br(),
    html.Div(children='''
    After you fixed the algorithm's mistake, this is what the updated table looks like.'''),
    html.Br(),
    dbc.Table(table_header + table_body, bordered=True, style={"width": "50%", "text-align": "right"}),
    html.Br(),
    html.Header("INSERT BOX PLOT AND INSIGHTS HERE"),
    html.Div(children='''
        What would you estimate the total value across contracts with T for C clauses? To help you out, we provided some graphs and insights.'''),
    html.Br(),
    dcc.Input(
            id="estimateInput",
            type="number",
            placeholder="enter your estimate",
        ),
    #insert graphs here
#     html.Div(children='''
#     But wait, what about company C and D? Even though you have not reviewed them, we know how likely it is for the algorithm to be correct based on its confidence. Using this information, we can estimate a range for the total potential revenue loss across all four contracts.
# '''),
#     html.Br(),
    html.A(dbc.Button("Submit"), href='/docSpectInstructions3'),

],style={'margin-left':'150px','margin-right':'150px','margin-top':'50px'})

# @callback(
#     [Output("correctContract", "children"),Output("incorrectContract","children")],
#     Input("choiceChecklist", "value"),
# )
# def checklistValidation(checklistSelected):
#     print(checklistSelected)
#     correctText= "The clause identified by the T for C algorithm in Contract " + checklistSelected[0] + " is a T for C"
#     incorrectText= "The clause identified by the T for C algorithm in Contract " + checklistSelected[1] + " is a T for C"
#     return correctText,incorrectText
#
