import dash
from dash import html, dcc, dash_table, Input, Output, State, callback
import dash_bootstrap_components as dbc

dash.register_page(__name__, path='/docSpectInstructions')

table_header = [
    html.Thead(html.Tr([html.Th("Company Name"), html.Th("T for C"), html.Th("T for C confidence"),  html.Th("Value ($)"), html.Th("Impact")
    ]))
]
row1 = html.Tr([html.Td("Company A"), html.Td("Yes"), html.Td("0.97"),html.Td("900,000"),html.Td("27,000")])
row2 = html.Tr([html.Td("Company B"), html.Td("Yes"), html.Td("0.72"),html.Td("90,000"),html.Td("25,200")])
row3 = html.Tr([html.Td("Company C"), html.Td("Yes"), html.Td("0.85"),html.Td("150,000"),html.Td("22,500")])
row4 = html.Tr([html.Td("Company D"), html.Td("Yes"), html.Td("0.95"),html.Td("60,000"),html.Td("3000")])

table_body = [html.Tbody([row1, row2, row3, row4])]

layout = html.Div(children=[
    html.H1(children='Training Part 1 : Choosing which contracts to review'),
    html.Br(),
    html.Header("Part of your task for this experiment consists of determining which contracts should be manually inspected. You should prioritize the inspection of contracts with high value and high algorithm uncertainty (low confidence) to increase your chances of accurately reporting the total value of contracts. To help you out, we created an Impact Factor where we multiplied the contract value by the algorithm's uncertainty (1 - confidence). The higher the Impact Factor, the more accurate your estimate is likely to be."),
    html.Br(),
    html.Header(
        "Here is some information about four contracts."),
    html.Br(),
    dbc.Table(table_header + table_body, bordered=True,style={"width":"50%","text-align":"right"}),
    html.Br(),
    html.Header("Let's say you can only review TWO contracts to estimate the total contract value. Which TWO contracts should you choose to increase the accuracy of your revenue estimate?"),
    html.Br(),
    dcc.Checklist(
        options=['Company A', 'Company B', 'Company C','Company D'],
        inline=False,
        style={"width": '10%', 'display': "inline-block"},
        id="choiceChecklist"
    ),

    html.Br(),
    html.Br(),
    html.Header("", id="checklistValidationText",style={'color':'red'}),
    html.A(dbc.Button("Next",id="nextDocSpect",style={"display":"none"}), href='/docSpectInstructions2'),
    html.Br(),

],style={'margin-left':'150px','margin-right':'150px','margin-top':'50px'})

@callback(
    [Output("checklistValidationText", "children"),Output("nextDocSpect","style")],
    Input("choiceChecklist", "value"),
)
def checklistValidation(checklistSelected):
    print(checklistSelected)
    if checklistSelected is not None:
        if len(checklistSelected) != 2:
            return "You must select two options", {'display': "none"}
        else:
            if (checklistSelected[0] == "Company A" and checklistSelected[1] == "Company B") or (checklistSelected[0] == "Company B" and checklistSelected[1] == "Company A"):
                 return "", {'display': "block"}
            else:
                return "Try again. These are not the two highest impact contracts", {'display': "none"}
    else:
        return "", {'display': "none"}




