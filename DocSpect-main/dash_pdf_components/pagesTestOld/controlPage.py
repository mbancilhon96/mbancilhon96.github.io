from random import sample
from select import select
import dash
from dash import html, Input, Output, State, callback_context, dash_table,callback,ctx
import pandas as pd
from collections import OrderedDict
import numpy as np
from itertools import compress, product, chain, combinations
import dash_pdf_components
import dash_bootstrap_components as dbc
import json
#mel added libraries
from dash import dcc
import plotly.express as px
from numpy.random import randint, rand, uniform
import plotly.graph_objects as go
import statistics
from statistics import mode
import os
from os import listdir
from os.path import isfile, join
import locale
import time
import uuid
import json, operator
import datetime
from operator import itemgetter
# from dash_extensions.enrich import Output, DashProxy, Input, MultiplexerTransform

# To use default settings, set locale to None or leave second argument blank.
locale.setlocale(locale.LC_ALL, 'en_US')

dash.register_page(
    __name__,
    path='/controlPage',
    use_pages=True,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    external_scripts=['https://documentcloud.adobe.com/view-sdk/main.js']
)

title = "Dash PDF Reader"
API_KEY = '899d52477b7d4b589f808242e8d36cc3' #This client ID only works for localhost
### read jsonlines file with annotations

def load_annotations(json_file_path):
    print("inside load annotations")
    arr = []
    with open(json_file_path, 'r') as file:
        for line in file:
            arr.append(json.loads(line))
    return arr

nextHref=""

#interaction variables
dfUserActivity=pd.DataFrame()
reviewGraphHovers=[]
projectionGraphHovers=[]
confidenceParamClicks=[]
revenueParamClicks=[]
timeStart=time.time()
contractReviews=[]

contractsOpened=[]
contractsReviewed=[]

docList = pd.read_csv('assets/files/studyFiles/studyDf.csv')
docList['tfcProjection'] = docList["tfcConfidence"]

dfUserActivity = json.load(open('assets/files/studyFiles/userDataInteractions.json'))
print("dfUserActivity is ", dfUserActivity)

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

# write_json(newRecord)
#
# dfUserActivity2 = json.load(open('assets/files/studyFiles/userDataInteractions.json'))
# print("dfUserActivity2 is ", dfUserActivity2)

mypath = "assets/files/studyFiles/"
allFiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

documentTable = []

for fileName in allFiles:
    if ".pdf" in fileName:
        fileNameNoExt = os.path.splitext(fileName)[0]
        # if the contract is in docList
        if (fileNameNoExt in set(docList['contractID'])):
            dictContract = {}
            contractInfo = {}
            contractInfo['showImpact'] = False
            dictContract['contractId'] = fileNameNoExt
            contractInfo['key'] = fileName
            contractInfo['fileUrl'] = "assets/files/studyFiles/{}".format(fileName)
            contractInfo['fileName'] = fileNameNoExt
            # annotationUrl = "assets/files/studyFiles/json/{}_annot.jsonlines".format(contractID)
            annotationUrl = "assets/files/studyFiles/json/{}.json".format(fileNameNoExt)
            highlightsArr=[]
            highlightsArr.append(json.load(open(annotationUrl)))
            # highlightsArr = load_annotations(annotationUrl)
            highlightsArr[0]['target']['source'] = fileNameNoExt
            highlightsArr[0]['creator']['isReviewed'] = docList.loc[docList['contractID'] == fileNameNoExt, 'reviewed'].iloc[0]
            highlightsArr[0]['creator']['isCorrect'] = docList.loc[docList['contractID'] == fileNameNoExt, 'tfc'].iloc[
                0]
            contractInfo['highlightsArr'] = highlightsArr
            contractInfo['tfcConfidence'] = docList.loc[docList['contractID'] == fileNameNoExt, 'tfcConfidence'].iloc[
                0]
            contractInfo['revenue'] = docList.loc[docList['contractID'] == fileNameNoExt, 'revenue'].iloc[0]
            # contractInfo['reviewed']=docList.loc[docList['contractID'] == contractID, 'reviewed'].iloc[0]
            contractInfo['endUser'] = docList.loc[docList['contractID'] == fileNameNoExt, 'endUser'].iloc[0]
            contractInfo['region'] = docList.loc[docList['contractID'] == fileNameNoExt, 'region'].iloc[0]
            contractInfo['fiscalYear'] = docList.loc[docList['contractID'] == fileNameNoExt, 'fiscalYear'].iloc[0]
            contractInfo['marketArea'] = docList.loc[docList['contractID'] == fileNameNoExt, 'marketArea'].iloc[0]
            contractInfo['impactFactor'] = float(contractInfo['revenue'] * (1 - contractInfo['tfcConfidence']))

            dictContract['tfcConfidence'] = docList.loc[docList['contractID'] == fileNameNoExt, 'tfcConfidence'].iloc[
                0]
            # compute impact factor as revenue * 1-confidence
            dictContract['impactFactor'] = float(contractInfo['revenue'] * (1 - contractInfo['tfcConfidence']))
            dictContract['data'] = contractInfo
            documentTable.append(dictContract)

# order in descending order of impact factor
documentTableSorted = sorted(documentTable, key=itemgetter('impactFactor'), reverse=True)
fullDocTable= documentTableSorted


testingSection=  html.Div([
                        html.Div(
                            [
                                html.P("What would you estimate the total value across contracts with T for C clauses?($)"),
                                dbc.Input(id="estimateInputControl",type="number"),
                            ],
                            id="estimateInputDiv"),
                        html.Div(
                            [
                                html.P("How confident are you in this estimate? (%)"),
                                dbc.Input(id="confidenceInputControl",type="number" ),
                            ],
                            id="confidenceInputDiv"),
                        html.Header(html.Br()),
                        html.Div([
                            html.A(dbc.Button('Submit', id='submitAnswerControl', n_clicks=0), id="nextPageLinkControl")
                        ],style={'display':'flex','justifyContent':'center'}),
                ],style={'paddingLeft':'100px','paddingRight':'100px'})

pdf_viewer = dbc.Col([
                dbc.Row([
                    html.P("Select a contract to open the pdf and review it.")
                ]),
                dbc.Row([
                        dbc.Button("i", id="pdfInfoOpen", className="me-1", n_clicks=0, color="light",
                                   style={'margin': '0', 'fontSize': 14,
                                          'borderRadius': 10, 'width': '20px', 'display':'none'}),
                        dbc.Modal(
                            [
                                dbc.ModalHeader(dbc.ModalTitle("Document Viewer")),
                                dbc.ModalBody(
                                    "This is where you review all the documents "),
                                dbc.ModalFooter(
                                    dbc.Button(
                                        "Close", id="pdfClose", className="ms-auto", n_clicks=0
                                    )
                                ),
                            ],
                            id="pdfModal",
                            is_open=False,
                        ),
                    ]),
                dbc.Row(
                    [
                        dash_pdf_components.DashPdfComponents(
                            # key='just-test-key',
                            id='pdf-view-control',
                            label='pdf-view-label',
                            pdfRendered="",
                            apiKey=API_KEY,
                            documentTable=fullDocTable,
                            toggle=False
                        )
                    ],
                    id='pdf-col',
                )
            ],style={'padding': '20px', 'marginRight': '10px',
                           'marginTop': '10px', 'borderRadius': '6px 6px 6px 6px'})


timerSection=html.Div([
    dcc.Interval(id='interval1', interval=1 * 1000, n_intervals=0),
    html.H1(id='timeLabelControl', children=''),
    dbc.Row([
        html.Header("The total value of all contracts where TFC=yes is {}".format(locale.currency(999, grouping=True)),
                    id="insightTotalControl",
                    style={'margin': 'auto', 'marginBottom': '5px', 'marginTop': '20px', 'fontSize': 16,
                           'textAlign': 'center'}),
    ]),
])


# when a review is made, data changes
# the pdf-viewer returns the current view of table (could be filtered)
# when a contract is being reviewed, this current table gets updated
# we need to use the data from this current table to update the full table and the full dataframe
def updateData(docTable):
    print("inside update data")
    global docList
    global fullDocTable
    print("docTable is ",docTable)

    for item in docTable:
        itemID= item["contractId"]
        itemHighlights=item["data"]["highlightsArr"][0]["creator"]
        print("highlightsArr is ",highlightsArr)
        #update this item in docList dataframe
        docList['reviewed'] = docList.apply(
            lambda x: itemHighlights['isReviewed'] if x['contractID'] == itemID else x['reviewed'], axis=1)
        # ******Record which contract is being reviewed and timestamp******
        docList['tfc'] = docList.apply(
            lambda x: itemHighlights['isCorrect'] if x['contractID'] == itemID else x['tfc'], axis=1)
        #if is reviewed is true tfcProjection is 1
        docList['tfcProjection'] = docList.apply(
            lambda x: x['tfcConfidence'] if x['contractID'] == itemID else 1.0 if x['reviewed'] == True else x['tfcConfidence'], axis=1)
        for (index, d) in enumerate(fullDocTable):
            if d["contractId"] == itemID:
                fullDocTable[index] = item

    print("docTable tfc is ", docList['tfcConfidence'])
    print("docTable tfc is ", docList['tfcProjection'])
    return fullDocTable,docList

# @callback(
#     Input("controlTestOrder", "data"),
# )
# def findOrder(controlTestOrder):
#     if controlTestOrder[0]=="controlPage":
#         nextHref="/secondPageIntro"
#     else:
#         nextHref="/lastPage"
#
#     return nextHref

#TODO: automatically submit page when time is over
# callback for timer
@callback(
   Output('nextPageLinkControl', 'href'),
   Output('timeLabelControl', 'children'),
  [Input('interval1', 'n_intervals'),
   Input("controlTestOrder", "data"),
   ])
def update_interval(n, controlTestOrder):
    if controlTestOrder[0]=="controlPage":
        nextHref="/secondPageIntro"
    elif controlTestOrder[1]=="controlPage":
        nextHref="/lastPage"

    # secondsLeft=900 -n  #15 minutes - time elapsed
    # return nextHref, 'Time Remaining: ' + str(datetime.timedelta(seconds=secondsLeft))
    return nextHref, 'Time Elapsed: ' + str(datetime.timedelta(seconds=n))

@callback(
    # Output('dataStore','data'),
    Output("submitAnswerControl", "n_clicks"), #trigger button click when timer is up
    Input("submitAnswerControl","n_clicks_timestamp"),
    Input('timeLabelControl', "children"),
    Input("estimateInputControl", "value"),
    Input("confidenceInputControl", "value"),
    Input("userIDStore", "data"),
)
def recordData(submitAnswer,timeElapsedText,estimateInput,confidenceInput, userIDStore ):
    global contractsOpened
    global contractsReviewed
    global docList

    timeElapsed= timeElapsedText.split(': ')[1]

    print("userID data store is ",userIDStore)
    print("userID is ",userIDStore['userID'])

    elementTriggered = ctx.triggered_id
    # print("elementTriggered is ", ctx.triggered_id)

    button_pressed = np.nanargmax(
        np.array(
            [0, submitAnswer], dtype=np.float64
        ))
    # if button_pressed == 1 or timeRemaining==str(datetime.timedelta(seconds=0)):  # user submitted their answer or time is up

    if button_pressed == 1:  # user submitted their answer or time is up
        print("submit button has been pressed or timer is up")
        #if time is pressed, automatically go to next page

        #get contracts reviewed id and review decision
        dfContractsReviewed= docList[docList["reviewed"]==True]
        contractsReviewedID=list(dfContractsReviewed["contractID"])
        contractsReviewedDecision=list(dfContractsReviewed["tfc"])
        contractsReviewed = {contractsReviewedID[i]: contractsReviewedDecision[i] for i in range(len(contractsReviewedID))}

        print("contractsReviewedID is ", contractsReviewedID)
        print("contractsReviewedDecision is ", contractsReviewedDecision)
        print("========")
        print("user id is ",[uuid.uuid1()])
        print("time remaining is ",timeElapsed)
        print("estimate input is ",estimateInput)
        print("confidence input is ",confidenceInput)
        print("contracts opened is ",contractsOpened)
        print("contracts reviewed is ",contractsReviewed)
        print("========")

        #record data
        newRecord = {
                        "userID":userIDStore['userID'],
                        "condition":"control",
                        "timeElapsed": str(timeElapsed),
                        "estimateInput": str(estimateInput),
                        "confidenceInput": str(confidenceInput),
                        "contractsOpened": str(contractsOpened),
                        "contractsReviewed": str(contractsReviewed),
                        "conditionOrder": userIDStore['conditionOrder']
        }

        write_json(newRecord)
        dfUserActivity2 = json.load(open('assets/files/studyFiles/userDataInteractions.json'))
        print("dfUserActivity2 is ", dfUserActivity2)

        return 1

@callback(
    Output("pdf-view-control", "documentTable"),
    Output("pdf-view-control", "pdfRendered"),
    Output('insightTotalControl', 'children'),
    [ Input("pdf-view-control", "toggle"),
     Input("pdf-view-control", "pdfRendered"),
     ],
    State("pdf-view-control", "documentTable"))
def mainCallback(toggle, pdfRendered,currentDocTable, ):
     global fullDocTable
     global docList
     global contractsOpened

     elementTriggered=ctx.triggered_id

     # everytime a contract is selected or reviewed
     # update fullDocTable and docList
     # to match retrieved updated data from pdf-view
     if elementTriggered == "pdf-view-control":
        fullDocTable, docList = updateData(currentDocTable)
        contractsOpened.append(pdfRendered)
        print("contracts opened is ",contractsOpened)

     elif elementTriggered == "slider_confidence" or elementTriggered == "slider_revenue":
         pdfRendered = fullDocTable[0]['contractId']

     print("pdf rendered is ",pdfRendered)

     docListTFC= docList[docList['tfc']==True]
     totalValue=sum((docListTFC['revenue']))
     insightTotalText="The total value of all contracts where TFC=yes is {}".format(locale.currency(totalValue,grouping=True))

     return  (fullDocTable, pdfRendered,insightTotalText)

layout = html.Div(
    [
        dbc.Row([testingSection,timerSection]),
        dbc.Row(pdf_viewer),
        dcc.Store(id='dataStore',data=dfUserActivity)
    ]
)
