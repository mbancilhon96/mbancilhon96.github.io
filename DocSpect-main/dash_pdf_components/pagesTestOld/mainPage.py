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
    path='/mainPage',
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

docList = pd.read_csv('assets/files/studyFiles/studyDf2.csv')
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
            contractInfo['showImpact'] = True
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

# fullDocTable= documentTable

#use T for C confidence to sample data
#if contract has been reviewed by user, confidence goes up to 1
def samplingData(df, conf):
    # print("in sampling data")
    data = []  # [[200, 0.7], [10, 1.0], [300, 0.5]]
    data_reviewed = []
    n_reviews = 0

    contract_values=df['revenue']
    confidences=conf

    for v, c in zip(contract_values, confidences):
        data.append([v, c])

    df = pd.DataFrame(data, columns=['contract-value', 'confidence'])

    n_repetitions = 1000
    sample = {}

    for contract_value, confidence in data:
        s = np.random.binomial(1, confidence, n_repetitions)
        s = [x * contract_value for x in s]
        sample[str(contract_value) + '@' + str(confidence) + '@' + str(randint(0, 10000000, 1)) ] = s

    df_sample_results = pd.DataFrame(sample)
    df_sample_results['total at risk without reviews'] = df_sample_results.sum(axis=1)
    # print("df_sample_results is ", df_sample_results)
    return df_sample_results

def revPlot(dfOrig):
    fig = go.Figure()

    fig.add_trace(
            go.Box(x=dfOrig['total at risk without reviews'],
                         name="Sampled Outcome", marker_color = 'steelblue',hoverinfo='skip'))

    Q1= np.quantile(dfOrig['total at risk without reviews'],0.25)
    Q3= np.quantile(dfOrig['total at risk without reviews'],0.75)
    IQR=Q3-Q1
    Lower_Fence = Q1 - (1.5 * IQR)
    Upper_Fence = Q3 + (1.5 * IQR)

    # fig.add_annotation(
    #     x=statistics.median(dfOrig['total at risk without reviews']), y=0 + 0.30, text=f'Most likely revenue',
    #     yanchor='bottom', showarrow=False, arrowhead=1, arrowsize=1
    #     , arrowwidth=2, arrowcolor="#636363", ax=-20, ay=-30,
    #     font=dict(size=11, color="steelblue", family="Sans Serif"), align="left")

    fig.add_annotation(
        x=statistics.median(dfOrig['total at risk without reviews'])+100000, y=-0.8, text=str(locale.currency(statistics.median(dfOrig['total at risk without reviews']),grouping=True)),
        yanchor='bottom', showarrow=False, arrowhead=1, arrowsize=1
        , arrowwidth=2, arrowcolor="#636363", ax=-20, ay=-30,textangle= 45,
        font=dict(size=12, color="steelblue", family="Sans Serif"), align="left")


    fig.add_annotation(
        x=Q1+100000, y=-0.8, text=str(locale.currency(Q1,grouping=True)),
        yanchor='bottom', showarrow=False, arrowhead=1, arrowsize=1
        , arrowwidth=2, arrowcolor="#636363", ax=-20, ay=-30,textangle= 45,
        font=dict(size=12, color="steelblue", family="Sans Serif"), align="left")

    fig.add_annotation(
        x=np.quantile(dfOrig['total at risk without reviews'],0.75)+100000, y=-0.8, text=str(locale.currency(np.quantile(dfOrig['total at risk without reviews'],0.75),grouping=True)),
       yanchor='bottom', showarrow=False, arrowhead=1, arrowsize=1
        , arrowwidth=2, arrowcolor="#636363", ax=-20, ay=-30,textangle= 45,
        font=dict(size=12, color="steelblue", family="Sans Serif"), align="left")

    fig.add_annotation(
        x=Lower_Fence+100000, y=-0.8, text=str(locale.currency(Lower_Fence,grouping=True)),
       yanchor='bottom', showarrow=False, arrowhead=1, arrowsize=1
        , arrowwidth=2, arrowcolor="#636363", ax=-20, ay=-30,textangle= 45,
        font=dict(size=12, color="steelblue", family="Sans Serif"), align="left")

    fig.add_annotation(
        x=Upper_Fence+100000, y=-0.8, text=str(locale.currency(Upper_Fence,grouping=True)),
       yanchor='bottom', showarrow=False, arrowhead=1, arrowsize=1
        , arrowwidth=2, arrowcolor="#636363", ax=-20, ay=-30,textangle= 45,
        font=dict(size=12, color="steelblue", family="Sans Serif"), align="left")

    fig.layout.plot_bgcolor = 'white'
    fig.layout.paper_bgcolor = 'white'
    fig.update_layout(
        showlegend=False,
        margin=dict(l=0, r=0, t=0, b=0),
    )
    return fig

def reviewGraph(df):
    # color_discrete_sequence = ['#FFA500', '#66c2a5'],
    fig = px.scatter(df, x="revenue", y="tfcConfidence",color="reviewed",color_discrete_map={
                False: "#FFA500",
                True: '#66c2a5'},
                     labels={
                         "tfcConfidence": "T for C confidence",
                         "revenue": "Contract Value"
                     })
    fig.update_traces(marker_size=5)
    fig.add_vline(x=0, line_width=2, line_dash="dash", line_color="steelblue")
    fig.add_vline(x=max(df['revenue']), line_width=2, line_dash="dash", line_color="steelblue")
    fig.add_hline(y=0.5, line_width=2, line_dash="dash", line_color="steelblue")
    fig.add_hline(y=1, line_width=2, line_dash="dash", line_color="steelblue")
    fig.layout.plot_bgcolor = 'white'
    fig.layout.paper_bgcolor = 'white'

    fig.update_layout(
        font_size=10,  #tick labels
        showlegend=False,
        margin=dict(l=20, r=20, t=20, b=20),
    )
    fig.update_xaxes(title_font_family="Arial",title_font_size=12 )
    fig.update_yaxes(title_font_family="Arial",title_font_size=12 )

    return fig

def reviewGraphSlider(df,x1,x2,y1,y2):
    fig = px.scatter(df, x="revenue", y="tfcConfidence",color="reviewed", color_discrete_map={
                False: "#FFA500",
                True: '#66c2a5'},
                     labels={
                         "tfcConfidence": "T for C confidence",
                         "revenue": "Contract Value"
                     })
    fig.update_traces(marker_size=5)
    fig.layout.plot_bgcolor = 'white'
    fig.layout.paper_bgcolor = 'white'

    fig.add_vline(x=y1, line_width=2, line_dash="dash", line_color="steelblue")
    fig.add_vline(x=y2, line_width=2, line_dash="dash", line_color="steelblue")
    fig.add_hline(y=x1, line_width=2, line_dash="dash", line_color="steelblue")
    fig.add_hline(y=x2, line_width=2, line_dash="dash", line_color="steelblue")

    fig.update_layout(
        font_size=10, #tick labels
        showlegend=False,
        margin=dict(l=20, r=20, t=20, b=20),
    )
    fig.update_xaxes(title_font_family="Arial",title_font_size=12)
    fig.update_yaxes(title_font_family="Arial",title_font_size=12)

    return fig

testingSection=  html.Div([
                        html.Div(
                            [
                                html.P("What would you estimate the total value across contracts with T for C clauses?($)"),
                                dbc.Input(id="estimateInput",type="number"),
                            ],
                            id="estimateInputDiv"),
                        html.Div(
                            [
                                html.P("How confident are you in this estimate? (%)"),
                                dbc.Input(id="confidenceInput",type="number" ),
                            ],
                            id="confidenceInputDiv"),
                        html.Header(html.Br()),
                        html.Div([
                            html.A(dbc.Button('Submit', id='submitAnswer', n_clicks=0),id="nextPageLink")
                        ],style={'display':'flex','justifyContent':'center'}),
                        dcc.Download(id="downloadUserActivity"),
                ],style={'paddingLeft':'100px','paddingRight':'100px'})

parameterSection=  dbc.Col([
                            dbc.Row([
                                    dbc.Col([html.Header("TFC confidence to review",style={'marginTop': '20px','marginBottom': '0px', 'marginLeft': '40px', 'fontSize': 14})]),
                                    dbc.Col([html.Div([dcc.RangeSlider(0.5, 1, id='slider_confidence', marks=None, step=0.05,value=[0.5,1],tooltip={"placement": "bottom", "always_visible": True})],
                                        style={'marginTop': '20px','width': '200px', 'paddingTop': '5px'})]),
                            ]),
                            dbc.Row([
                                dbc.Col([html.Header("Value to review ($)", style={'marginBottom': '0px', 'marginLeft': '40px', 'fontSize': 14})]),
                                dbc.Col([html.Div([dcc.RangeSlider(0, max(docList['revenue'])+10, id='slider_revenue', marks=None, step=10,value=[0,max(docList['revenue'])+10],tooltip={"placement": "bottom", "always_visible": True})],
                                        style={'width': '200px', 'display': 'inline-block', 'paddingTop': '5px'})]),
                            ]),
                        ],style={'background': 'white','color':'#43464B','padding': '20px','marginRight':'10px','marginTop':'10px','borderRadius': '6px 6px 6px 6px'})

overviewSection=dbc.Col([
                    # progress bar
                    dbc.Row([html.Header("Pick your reviewing parameters.", style={'fontWeight':'bold'})]),
                    dbc.Row([html.Br()]),
                    dbc.Row([
                        dbc.Col([
                            dbc.Row([
                                html.P(["T for C confidence"]),
                                html.Div([dcc.RangeSlider(0.5, 1, id='slider_confidence', marks=None, step=0.05,
                                                          value=[0.5, 1],
                                                          tooltip={"placement": "bottom", "always_visible": True})])
                            ]),
                            dbc.Row([
                                html.P("Contract Value ($)"),
                                html.Div(
                                    [dcc.RangeSlider(0, max(docList['revenue']) + 10, id='slider_revenue', marks=None,
                                                     step=10, value=[0, max(docList['revenue']) + 10],
                                                     tooltip={"placement": "bottom", "always_visible": True})])
                            ])
                        ],width=5),
                        dbc.Col([
                            dcc.Graph(id="reviewGraph", figure=reviewGraph(docList),
                                      style={'width': '30vh', 'height': '25vh', 'marginLeft': '90px', 'margin': 'auto'})
                        ],width=4),
                        dbc.Col([
                            html.Header("{} contracts in total".format(docList.shape[0]),
                                        id="numContracts",
                                        style={'color': '#7E7E7E'}),
                            html.Header("{} selected for review".format(docList[docList['tfc'] == True].shape[0]),
                                        id="numReviews",
                                        style={'color': 'steelblue'}),
                            html.Br(),
                            html.Header("{} reviewed".format(
                                docList[(docList['tfc'] == True) & (docList['reviewed'] == True)].shape[
                                    0]),
                                id="numReviewed",
                                style={'color': '#66c2a5'}),
                            html.Header("{} not reviewed".format(
                                docList[(docList['tfc'] == "Y") & (docList['reviewed'] == "0")].shape[0]),
                                id="numNotReviewed",
                                style={'color': '#FFA500'}),
                            dbc.Progress([
                                dbc.Progress(value=0, id="progressReviewed", color="#66c2a5", bar=True),
                                dbc.Progress(value=100, id="progressNotReviewed", color="#FFA500", bar=True)

                            ], style={'height': "8px", "width": "auto", 'marginBottom': '10px'}),
                        ],width=3)
                    ]),
            ],style={'background': 'white','color':'#43464B','padding': '20px','marginRight':'10px','marginTop':'10px','borderRadius': '6px 6px 6px 6px'})

sampledData1=samplingData(docList, docList['tfcProjection'])

statsSection= dbc.Col([
                    dbc.Row([
                        html.Header("The total value of all contracts where TFC=yes is {}".format(locale.currency(999, grouping=True)),
                                    id="insightTotal",
                                    style={'margin': 'auto', 'marginBottom': '5px', 'marginTop': '20px', 'fontSize': 16,
                                           'textAlign': 'center'}),
                    ]),
                    dbc.Row([
                        html.Header("The most likely total revenue at risk due to T for C is {}".format(locale.currency(999,grouping=True)),
                                    id="insight1",
                                    style={'margin':'auto','marginBottom':'5px','marginTop':'20px','fontSize': 16,
                                           'textAlign': 'center'}),
                    ]),
                    #projection graph
                    dbc.Row([
                            dcc.Graph(id="graph-Projections",figure=revPlot(sampledData1),
                                    style={'width': '60vh', 'height': '20vh','align':'left','marginTop':'0px','margin':'auto'})
                    ])
],style={'background': 'white','color':'#43464B','padding': '20px','marginRight':'10px','marginTop':'10px','borderRadius': '6px 6px 6px 6px'})

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
                            id='pdf-view',
                            label='pdf-view-label',
                            pdfRendered="",
                            apiKey=API_KEY,
                            documentTable=fullDocTable,
                            toggle=False,
                            showImpact=True
                        )
                    ],
                    id='pdf-col',
                )
            ],style={'padding': '20px', 'marginRight': '10px',
                           'marginTop': '10px', 'borderRadius': '6px 6px 6px 6px'})



timerSection=html.Div([
    dcc.Interval(id='interval1', interval=1 * 1000, n_intervals=0),
    html.H1(id='label1', children='')
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
        # docList['tfcProjection'] = docList.apply(
        #     lambda x: float(item['data']['tfcConfidence']) if x['contractID'] == itemID else x['tfcProjection'], axis=1)
        #update changed item in fullDocTable table
        # itemIndex = fullDocTable.index(item) #find index of element with same contract ID
        for (index, d) in enumerate(fullDocTable):
            if d["contractId"] == itemID:
                fullDocTable[index] = item

    print("docTable tfc is ", docList['tfcConfidence'])
    print("docTable tfc is ", docList['tfcProjection'])
    return fullDocTable,docList

#TODO: automatically submit page when time is over

# callback for timer
@callback(
    Output('nextPageLink', 'href'),
    Output('label1', 'children'),
    [Input('interval1', 'n_intervals'),
     Input("controlTestOrder", "data"),
     ])
def update_interval(n, controlTestOrder):
    if controlTestOrder[0]=="mainPage":
        nextHref="/secondPageIntro"
    elif controlTestOrder[1]=="mainPage":
        nextHref="/lastPage"

    # secondsLeft=900 -n  #15 minutes - time elapsed
    # return nextHref, 'Time Remaining: ' + str(datetime.timedelta(seconds=secondsLeft))
    return nextHref, 'Time Elapsed: ' + str(datetime.timedelta(seconds=n))

def filterData(docs, confValues, revValues):
    print("inside filter data")
    filteredDocumentTable = []
    for item in docs:
        if (item['data']['revenue'] <= revValues[1] and item['data']['revenue'] >= revValues[0]) and \
                (item['data']['tfcConfidence'] <= confValues[1] and item['data']['tfcConfidence'] >= confValues[0]):
            filteredDocumentTable.append(item)

    return filteredDocumentTable

#=====Record all user interactions when user submits or when time is over=====
#Estimate Answer
#Input Answer
#Number of pdfs clicked
#Number of pdfs edited
#Parameters clicked
#Overall time taken


@callback(
    # Output('dataStore','data'),
    Output("submitAnswer", "n_clicks"), #trigger button click when timer is up
    Input("submitAnswer","n_clicks_timestamp"),
    Input('label1', "children"),
    Input("estimateInput", "value"),
    Input("confidenceInput", "value"),
    Input("dataStore", "data"),
    Input("userIDStore", "data"),

)
def recordData(submitAnswer,timeElapsedText,estimateInput,confidenceInput, dataStoreData,userIDStore ):
    global contractsOpened
    global contractsReviewed
    global docList

    timeElapsed= timeElapsedText.split(': ')[1]

    elementTriggered = ctx.triggered_id
    # print("elementTriggered is ", ctx.triggered_id)

    # ******Record user graph hovers******
    # if reviewGraphMouseOn != None:
    #     xCoord = reviewGraphMouseOn['points'][0]['x']
    #     yCoord = reviewGraphMouseOn['points'][0]['y']
    #     dictHover = {"x": xCoord, "y": yCoord, "timestamp": time.time()}
    #     reviewGraphHovers.append(dictHover)
    #
    # if graphProjectionsMouseOn != None:
    #     xCoord = graphProjectionsMouseOn['points'][0]['x']
    #     yCoord = graphProjectionsMouseOn['points'][0]['y']
    #     dictHover = {"x": xCoord, "y": yCoord, "timestamp": time.time()}
    #     projectionGraphHovers.append(dictHover)

    button_pressed = np.nanargmax(
        np.array(
            [0, submitAnswer], dtype=np.float64
        ))
    # if button_pressed == 1 or timeRemaining==str(datetime.timedelta(seconds=0)):  # user submitted their answer or time is up
    if button_pressed ==1:
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
        print("datastore data is ", dataStoreData)
        print("========")

        #record data
        newRecord = {
                        "userID":userIDStore['userID'],
                        "condition":"test",
                        "timeElapsed": str(timeElapsed),
                        "estimateInput": str(estimateInput),
                        "confidenceInput": str(confidenceInput),
                        "contractsOpened": str(contractsOpened),
                        "contractsReviewed": str(contractsReviewed),
                        "conditionOrder": userIDStore['conditionOrder']

        }
        # newRecord= {"userID": str(userIDStore['userID']),  # generate random user ID
        #               "timeRemaining": str(timeRemaining),
        #               "estimateInput": str(estimateInput),
        #               "confidenceInput": str(confidenceInput),
        #               "contractsOpened": str(contractsOpened),
        #               "contractsReviewed": str(contractsReviewed)}

        # newRecord=   {
        #   "userID": "thirdTest",
        #   "timeRemaining": "thirdTest",
        #   "estimateInput": "thirdTest",
        #   "confidenceInput": "thirdTest",
        #   "contractsOpened": "thirdTest",
        #   "contractsReviewed": "thirdTest"
        # }

        write_json(newRecord)
        dfUserActivity2 = json.load(open('assets/files/studyFiles/userDataInteractions.json'))
        print("dfUserActivity2 is ", dfUserActivity2)
        dataStoreData.append(newRecord)
        print("new datastore data is ", dataStoreData)

        # dataStoreData.to_json('assets/files/studyFiles/userDataInteractions.json', mode='a', index=False, header=False)

        # dfCurrentUser = pd.DataFrame({"userID": [uuid.uuid1()],  # generate random user ID
        #                               "timeRemaining": timeRemaining,
        #                               "estimateInput": estimateInput,
        #                               "confidenceInput": confidenceInput,
        #                               "contractsOpened": contractsOpened,
        #                               "contractsReviewed": contractsReviewed})

        # dfUserActivity = pd.read_csv('assets/files/studyFiles/studyDf.csv')
        # print("dfUserActivity is ",dfUserActivity)

        #dfCurrentUser.to_csv('assets/files/studyFiles/userDataInteractions.json', mode='a', index=False, header=False)

        # try:  # if df is not empty
        #     dfUserActivity = pd.read_csv("userDataInteractions.json", index_col=[0])
        #     updatedUserActivity = dfUserActivity.append(dfCurrentUser)
        #     print("in try. User activity is ",updatedUserActivity)
        #     updatedUserActivity.to_csv("userDataInteractions.json", mode='a', header=False)  # append mode
        # except:
        #     print("in except. User activity is ",updatedUserActivity)
        #     updatedUserActivity = dfCurrentUser  # if df is empty
        #     updatedUserActivity.to_csv("userDataInteractions.json", mode='a')  # append mode

        return 1

@callback(
    Output("pdf-view", "documentTable"),
    Output("pdf-view", "pdfRendered"),
    Output('reviewGraph', 'figure'),
    Output('graph-Projections', 'figure'),
    Output('numReviews', 'children'),
    Output('numReviewed', 'children'),
    Output('numNotReviewed', 'children'),
    Output('progressReviewed','value'),
    Output('progressNotReviewed', 'value'),
    Output('insight1', 'children'),
    Output('insightTotal', 'children'),
    [Input('slider_confidence', 'value'),
     Input('slider_revenue', 'value'),
     Input("pdf-view", "toggle"),
     Input("pdf-view", "pdfRendered"),
     # Input("reviewGraph", "hoverData"),
     # Input("graph-Projections", "hoverData")
     ],
    State("pdf-view", "documentTable"))
def mainCallback(sliderConf, sliderRev, toggle, pdfRendered,currentDocTable, ):
     global fullDocTable
     global docList
     global contractsOpened

     elementTriggered=ctx.triggered_id
     # print("elementTriggered is ",ctx.triggered_id)

     # everytime a contract is selected or reviewed
     # update fullDocTable and docList
     # to match retrieved updated data from pdf-view
     if elementTriggered == "pdf-view":
        fullDocTable, docList = updateData(currentDocTable)
        #filter full doc table based on slider values
        filteredDocumentTable = filterData(fullDocTable, sliderConf, sliderRev)
        # pdfRendered = filteredDocumentTable[0]['contractId']
        #add to list of contracts opened
        contractsOpened.append(pdfRendered)
        print("contracts opened is ",contractsOpened)

     elif elementTriggered == None:
        #pass data to be displayed as fullDocTable
        filteredDocumentTable = fullDocTable

     # elif elementTriggered == "reviewGraph" or elementTriggered == "graph-Projections":
     #     print("reviewGraphMouseOn is",reviewGraphMouseOn)
     #     print("graphProjectionsMouseOn is",graphProjectionsMouseOn)
     #     # ******Record user graph hovers******
     #     if reviewGraphMouseOn != None:
     #         xCoord = reviewGraphMouseOn['points'][0]['x']
     #         yCoord = reviewGraphMouseOn['points'][0]['y']
     #         dictHover = {"x": xCoord, "y": yCoord, "timestamp": time.time()}
     #         reviewGraphHovers.append(dictHover)
     #
     #     if graphProjectionsMouseOn != None:
     #         xCoord = graphProjectionsMouseOn['points'][0]['x']
     #         yCoord = graphProjectionsMouseOn['points'][0]['y']
     #         dictHover = {"x": xCoord, "y": yCoord, "timestamp": time.time()}
     #         projectionGraphHovers.append(dictHover)
     #     #pass data to be displayed as fullDocTable
     #     filteredDocumentTable = fullDocTable

     # when sliders are selected
     # filter data from document table to display
     elif elementTriggered == "slider_confidence" or elementTriggered == "slider_revenue":
         filteredDocumentTable = filterData(fullDocTable, sliderConf, sliderRev)
         pdfRendered = filteredDocumentTable[0]['contractId']
         #******Record user parameter clicks******
         if elementTriggered == "slider_confidence":
             dictConf = {"confValue0": sliderConf[0], "confValue1": sliderConf[1], "confTimestamp": time.time()}
             confidenceParamClicks.append(dictConf)
         elif elementTriggered == "slider_revenue":
             dictRev = {"revValue0": sliderRev[0], "revValue1": sliderRev[1], "revTimestamp": time.time()}
             revenueParamClicks.append(dictRev)

     # print("filtered document table is ", filteredDocumentTable)

     reviewTitle = "{} contracts selected for review".format(int(len(filteredDocumentTable)))

     dfReviewed = docList[docList['reviewed'] == True]
     if dfReviewed.empty:
         numReviewed = 0
     else:
         numReviewed = dfReviewed.shape[0]
     numReviewedText = "{} reviewed".format(int(numReviewed))

     dfNotReviewed = docList[docList['reviewed'] == False]
     if dfNotReviewed.empty:
         numNotReviewed = 0
     else:
         numNotReviewed = dfNotReviewed.shape[0]
     numNotReviewedText = "{} not reviewed".format(int(numNotReviewed))

     progressReviewed = (int(numReviewed) / (int(numNotReviewed) + int(numReviewed))) * 100
     progressNotReviewed = (int(numNotReviewed) / (int(numNotReviewed) + int(numReviewed))) * 100

     sampledDf= samplingData(docList, docList['tfcProjection'])
     mostLikelyRev = statistics.median(sampledDf['total at risk without reviews'])
     insightText="The most likely total revenue at risk is {}".format(locale.currency(mostLikelyRev,grouping=True))

     docListTFC= docList[docList['tfc']==True]
     totalValue=sum((docListTFC['revenue']))
     insightTotalText="The total value of all contracts where TFC=yes is {}".format(locale.currency(totalValue,grouping=True))

     print("full document table is ",len(fullDocTable))

     print("filtered document table is ",len(filteredDocumentTable))

     return  (filteredDocumentTable, pdfRendered,reviewGraphSlider(docList,sliderConf[0],sliderConf[1],sliderRev[0],sliderRev[1]),revPlot(sampledDf), reviewTitle, numReviewedText, numNotReviewedText,progressReviewed,progressNotReviewed,insightText,insightTotalText)
# @callback(
#     Output("pdf-view", "documentTable"),
#     Output('reviewGraph', 'figure'),
#     Output('graph-Projections', 'figure'),
#     [Input('slider_confidence', 'value'),
#      Input('slider_revenue', 'value'),
#      Input("pdf-view", "documentTable")])
# def filter_data(sliderConf, sliderRev, currentDocTable):
#      filteredDocumentTable = []
#
#      elementTriggered=ctx.triggered_id
#      print("elementTriggered is ",ctx.triggered_id)
#
#      # useCurrentDocTable to update fullDocTable
#      fullDocTable = updateData(currentDocTable)[0]
#      docList=updateData(currentDocTable)[1]
#
#      for item in fullDocTable:
#          if (item['data']['revenue'] <= sliderRev[1] and item['data']['revenue'] >= sliderRev[0]) and (
#                  item['data']['tfcConfidence'] <= sliderConf[1] and item['data']['tfcConfidence'] >= sliderConf[0]):
#              filteredDocumentTable.append(item)  #update docTable
#
#      #record user interactions with sliders
#      if elementTriggered == "slider_confidence" or elementTriggered == "slider_revenue" :
#          if elementTriggered=="slider_confidence":
#              dictConf={"confValue0":sliderConf[0], "confValue1":sliderConf[1],"confTimestamp":time.time()}
#              confidenceParamClicks.append(dictConf)
#          elif elementTriggered=="slider_revenue":
#              dictRev={"revValue0":sliderRev[0], "revValue1":sliderRev[1],"revTimestamp":time.time()}
#              revenueParamClicks.append(dictRev)
#
#      return  (filteredDocumentTable, reviewGraphSlider(docList,sliderConf[0],sliderConf[1],sliderConf[0],sliderRev[1]),revPlot(samplingData(docList, docList['tfcProjection'])))

layout = html.Div(
    [
        dbc.Row([testingSection,timerSection,overviewSection, statsSection]),

        dbc.Row(pdf_viewer),
        dcc.Store(id='dataStore',data=dfUserActivity),
    ]
)

# if __name__ == "__main__":
#     app.run_server(debug=True)
