import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash import html, Input, Output, State, callback_context, dash_table,callback,ctx
import json, operator

dash.register_page(__name__, path='/lastPage')

layout = html.Div(children=[
    html.H1(children='Please enter your user testing ID.'),

    html.Div(
        [
            html.P("Please enter your user testing ID."),
            dbc.Input(id="userTestingID", type="text"),
        ],
        id="estimateInputDiv"),
    html.Div([
        html.A(dbc.Button('Submit', id='submitUserId', n_clicks=0),id="thankYouPageLink",href="/thankYouPage")
    ],style={'display':'flex','justifyContent':'center'}),
    # html.Div(children='''
    #     Thank you for taking this survey! Please paste the following code into Prolific to receive compensation: 'uniqueCode'
    # '''),
],style={'margin-left':'150px','margin-right':'150px','margin-top':'50px'})


def write_json(new_data, filename='assets/files/studyFiles/userDataInteractions.json'):
    print("inside write json")
    with open(filename, 'r+') as file:
        # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data["interaction_details"].append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent=4)

@callback(
    Output('thankYouPageLink', 'href'),
    [Input('submitUserId', 'n_clicks_timestamp'),
     Input("userIDStore", "data"),
     Input("userTestingID", "value"),
     ])
def saveUserTestingID(n, userIDStore,userTestingID):

    elementTriggered = ctx.triggered_id

    if elementTriggered == "submitUserId":
        matchingIDRecord= {"dashUserID":userIDStore['userID'],
                           "userTestingID":userTestingID
        }
        #open file and find record with same user ID
        write_json(matchingIDRecord)

    return "/thankYouPage"
