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
reviewGraphHovers=[]
projectionGraphHovers=[]
confidenceParamClicks=[]
revenueParamClicks=[]
timeStart=time.time()
contractReviews=[]

contractsOpened=[]
contractsReviewed=[]


# docList = pd.read_csv('assets/files/studyFiles/studyDf2.csv')
docList = pd.read_csv('assets/files/studyFiles/studyDf2.csv')
docList['tfcProjection'] = docList["tfcConfidence"]

def get_bounding_box_rect_from_quadpoints(quadpoints):
        """
        Get the bounding box rectangle from the quadpoints.
        [small_x, big_y, big_x, big_y, small_x, small_y, big_x, small_y]
        """
        quadpoints = [quadpoints[i : i + 2] for i in range(0, len(quadpoints), 2)]
        quadpoints = np.array(quadpoints)
        small_x = min(quadpoints[:, 0])
        big_y = max(quadpoints[:, 1])
        big_x = max(quadpoints[:, 0])
        small_y = min(quadpoints[:, 1])
        return [small_x, small_y, big_x, big_y]

test=[
                120.02881844380404,
                626.7102145373038,
                299.75450955278046,
                626.7102145373038,
                120.02881844380404,
                617.8191909488739,
                299.75450955278046,
                617.8191909488739,
                299.75450955278046,
                626.7102145373038,
                425.49898601771804,
                626.7102145373038,
                299.75450955278046,
                617.8191909488739,
                425.49898601771804,
                617.8191909488739,
                425.49898601771804,
                626.7102145373038,
                427.4042053580959,
                626.7102145373038,
                425.49898601771804,
                617.8191909488739,
                427.4042053580959,
                617.8191909488739,
                49.53570284982389,
                617.1841178354147,
                446.4563987618743,
                617.1841178354147,
                49.53570284982389,
                607.6580211335254,
                446.4563987618743,
                607.6580211335254,
                447.0914718753336,
                617.1841178354147,
                534.096488419255,
                617.1841178354147,
                447.0914718753336,
                607.6580211335254,
                534.096488419255,
                607.6580211335254,
                49.53570284982389,
                607.0229480200661,
                149.87725477639023,
                607.0229480200661,
                49.53570284982389,
                598.1319244316362,
                149.87725477639023,
                598.1319244316362
            ]
print("/n")
print(get_bounding_box_rect_from_quadpoints(test))
print("/n")

def write_json(new_data, filename='assets/files/studyFiles/userDataTestCondition.json'):
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
            contractInfo['impactFactor'] = round(float(contractInfo['revenue'] * (1 - contractInfo['tfcConfidence'])),2)

            dictContract['tfcConfidence'] = docList.loc[docList['contractID'] == fileNameNoExt, 'tfcConfidence'].iloc[
                0]
            # compute impact factor as revenue * 1-confidence
            dictContract['impactFactor'] = round(float(contractInfo['revenue'] * (1 - contractInfo['tfcConfidence'])),2)
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
    layout = go.Layout(
        barmode='overlay')

    fig = px.strip(dfOrig, x='total at risk without reviews',stripmode='overlay',color_discrete_sequence=['steelblue'])
    # fig = px.box(dfOrig, x='total at risk without reviews')

    # fig = go.Figure()
    #
    fig.add_trace(
            go.Box(x=dfOrig['total at risk without reviews'],
                   name="Sampled Outcome",
                   marker_color = 'steelblue',
                   hoverinfo='skip'))

    fig.update_layout( legend={'traceorder': 'normal'})
    # fig.add_trace(
    #         go.Box(x=dfOrig['total at risk without reviews'],
    #                name="Sampled Outcome",
    #                marker_color = 'steelblue',
    #                hovertemplate='x',
    #                marker_size=2,
    #                boxpoints='all'))
    # fig.update_layout(hovermode='x',hoverdistance=2000)

    Q1= np.quantile(dfOrig['total at risk without reviews'],0.25)
    Q3= np.quantile(dfOrig['total at risk without reviews'],0.75)
    IQR=Q3-Q1
    Lower_Fence = Q1 - (1.5 * IQR)
    Upper_Fence = Q3 + (1.5 * IQR)

    # fig.add_annotation(
    #     x=statistics.median(dfOrig['total at risk without reviews'])+100000, y=-0.8, text=str(locale.currency(statistics.median(dfOrig['total at risk without reviews']),grouping=True)),
    #     yanchor='bottom', showarrow=False, arrowhead=1, arrowsize=1
    #     , arrowwidth=2, arrowcolor="#636363", ax=-20, ay=-30,textangle= 45,
    #     font=dict(size=12, color="steelblue", family="Sans Serif"), align="left")
    #
    #
    # fig.add_annotation(
    #     x=Q1+100000, y=-0.8, text=str(locale.currency(Q1,grouping=True)),
    #     yanchor='bottom', showarrow=False, arrowhead=1, arrowsize=1
    #     , arrowwidth=2, arrowcolor="#636363", ax=-20, ay=-30,textangle= 45,
    #     font=dict(size=12, color="steelblue", family="Sans Serif"), align="left")
    #
    # fig.add_annotation(
    #     x=np.quantile(dfOrig['total at risk without reviews'],0.75)+100000, y=-0.8, text=str(locale.currency(np.quantile(dfOrig['total at risk without reviews'],0.75),grouping=True)),
    #    yanchor='bottom', showarrow=False, arrowhead=1, arrowsize=1
    #     , arrowwidth=2, arrowcolor="#636363", ax=-20, ay=-30,textangle= 45,
    #     font=dict(size=12, color="steelblue", family="Sans Serif"), align="left")
    #
    # fig.add_annotation(
    #     x=Lower_Fence+100000, y=-0.8, text=str(locale.currency(Lower_Fence,grouping=True)),
    #    yanchor='bottom', showarrow=False, arrowhead=1, arrowsize=1
    #     , arrowwidth=2, arrowcolor="#636363", ax=-20, ay=-30,textangle= 45,
    #     font=dict(size=12, color="steelblue", family="Sans Serif"), align="left")
    #
    # fig.add_annotation(
    #     x=Upper_Fence+100000, y=-0.8, text=str(locale.currency(Upper_Fence,grouping=True)),
    #    yanchor='bottom', showarrow=False, arrowhead=1, arrowsize=1
    #     , arrowwidth=2, arrowcolor="#636363", ax=-20, ay=-30,textangle= 45,
    #     font=dict(size=12, color="steelblue", family="Sans Serif"), align="left")

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
    fig.add_hline(y=0.50, line_width=2, line_dash="dash", line_color="steelblue")
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
                        html.Div([
                            html.A(dbc.Button('Finish and Exit', id='submitAnswer', n_clicks=0, style={"width":"150px"}),href="/thankYouPage")
                        ],style={'display':'flex','justifyContent':'center'}),
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
                        ],width=3),
                        dbc.Col([
                            dcc.Graph(id="reviewGraph", figure=reviewGraph(docList),
                                      style={'height': '200px', 'width': '100%', 'marginLeft': '0px', 'margin': 'auto'})
                        ], width=4),
                        dbc.Col([
                            html.Div([
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
                                ]),
                            ])
                        ], width=4),

                    ]),
            ],style={'background': 'white','color':'#43464B','padding': '20px','marginRight':'10px','marginTop':'10px','borderRadius': '6px 6px 6px 6px'})

sampledDf=samplingData(docList, docList['tfcProjection'])

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
                            dcc.Graph(id="graph-Projections",figure=revPlot(sampledDf),
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
def updateData(docTable, pdfRendered):
    global docList
    global fullDocTable

    for item in docTable:
        itemID= item["contractId"]
        itemHighlights=item["data"]["highlightsArr"][0]["creator"]

        # figure out if item rendered has just been reviewed to update sampledData
        if itemID == pdfRendered:
            docListSelected= docList[docList['contractID']==itemID]
            if itemHighlights['isReviewed'] != docListSelected.iloc[0]['reviewed']:
                isSampled= True
            else:
                isSampled= False

        #update data
        #update this item in docList dataframe
        docList['reviewed'] = docList.apply(
            lambda x: itemHighlights['isReviewed'] if x['contractID'] == itemID else x['reviewed'], axis=1)
        # ******Record which contract is being reviewed and timestamp******
        docList['tfc'] = docList.apply(
            lambda x: itemHighlights['isCorrect'] if x['contractID'] == itemID else x['tfc'], axis=1)
        #if is reviewed is true tfcProjection is 1
        docList['tfcProjection'] = docList.apply(
            lambda x: 1.0 if x['reviewed'] == True else x['tfcConfidence'], axis=1)
        # docList['tfcProjection'] = docList.apply(
        #     lambda x: x['tfcConfidence'] if x['contractID'] == itemID else 1.0 if x['reviewed'] == True else x['tfcConfidence'], axis=1)
        #update changed item in fullDocTable table
        for (index, d) in enumerate(fullDocTable):
            if d["contractId"] == itemID:
                fullDocTable[index] = item

    return fullDocTable,docList, isSampled

#TODO: automatically submit page when time is over

# callback for timer
@callback(
    Output('label1', 'children'),
    [Input('interval1', 'n_intervals')
     ])
def update_interval(n):
    # secondsLeft=900 -n  #15 minutes - time elapsed
    # return nextHref, 'Time Remaining: ' + str(datetime.timedelta(seconds=secondsLeft))
    return 'Time Elapsed: ' + str(datetime.timedelta(seconds=n))

def filterData(docs, confValues, revValues):
    filteredDocumentTable = []
    for item in docs:
        if (item['data']['revenue'] <= revValues[1] and item['data']['revenue'] >= revValues[0]):
            if (item['data']['tfcConfidence'] <= confValues[1] and item['data']['tfcConfidence'] >= confValues[0]):
                filteredDocumentTable.append(item)

    return filteredDocumentTable

# @callback(
#     Output('dataStore','data'),
#     Input("userIDStore", "data")
# )
# def testID(userIDStore):
#     print("user id  store is", userIDStore)
#     return 1
# #
@callback(
    Output('dataStore','data'),
    Input("submitAnswer","n_clicks_timestamp"),
    Input('label1', "children"),
    Input("userIDStore", "data"),
)
def recordData(submitAnswer,timeElapsedText,userIDStore):
    global contractsOpened
    global contractsReviewed
    global docList

    timeElapsed= timeElapsedText.split(': ')[1]

    elementTriggered = ctx.triggered_id

    button_pressed = np.nanargmax(
        np.array(
            [0, submitAnswer], dtype=np.float64
        ))

    if button_pressed ==1:
        print("submit button has been pressed")

        #get contracts reviewed id and review decision
        dfContractsReviewed= docList[docList["reviewed"]==True]
        contractsReviewedID=list(dfContractsReviewed["contractID"])
        contractsReviewedDecision=list(dfContractsReviewed["tfc"])
        contractsReviewed = {contractsReviewedID[i]: contractsReviewedDecision[i] for i in range(len(contractsReviewedID))}

        print("========")
        print("user id  store",userIDStore)
        print("user id  is ",userIDStore['userID'])
        print("time elapsed is ",timeElapsed)
        print("contracts opened is ",contractsOpened)
        print("contracts reviewed is ",contractsReviewed)
        print("========")

        #record data
        newRecord = {
                        "userID":userIDStore['userID'],
                        "condition":"test",
                        "timeElapsed": str(timeElapsed),
                        "contractsOpened": str(contractsOpened),
                        "contractsReviewed": str(contractsReviewed),
        }
        print("new record is ",newRecord)
        write_json(newRecord)
        dfUserActivity2 = json.load(open('assets/files/studyFiles/userDataTestCondition.json'))
        print("dfUserActivity2 is ", dfUserActivity2)

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
     ],
    State("pdf-view", "documentTable"))
def mainCallback(sliderConf, sliderRev, toggle, pdfRendered,currentDocTable):
     global fullDocTable
     global docList
     global contractsOpened
     global sampledDf

     elementTriggered=ctx.triggered_id
     # print("elementTriggered is ",ctx.triggered_id)

     # everytime a contract is selected or reviewed
     # update fullDocTable and docList
     # to match retrieved updated data from pdf-view
     if elementTriggered == "pdf-view":
        print("pdf view selected")
        print("current doc table is ",currentDocTable)
        fullDocTable, docList, isSampled = updateData(currentDocTable,pdfRendered)
        if isSampled ==True :
           print("data is being sampled")
           print("docList tfc is",docList['tfcProjection'])
           print("docList revenue is",docList['revenue'])

           sampledDf= samplingData(docList, docList['tfcProjection'])

        #filter full doc table based on slider values
        filteredDocumentTable = filterData(fullDocTable, sliderConf, sliderRev)
        # pdfRendered = filteredDocumentTable[0]['contractId']
        #add to list of contracts opened
        contractsOpened.append(pdfRendered)

     elif elementTriggered == None:
        #pass data to be displayed as fullDocTable
        filteredDocumentTable = fullDocTable

     # when sliders are selected
     # filter data from document table to display
     elif elementTriggered == "slider_confidence" or elementTriggered == "slider_revenue":
         print("table filtered")
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

     # sampledDf= samplingData(docList, docList['tfcProjection'])
     mostLikelyRev = statistics.median(sampledDf['total at risk without reviews'])
     insightText="The most likely total revenue at risk is {}".format(locale.currency(mostLikelyRev,grouping=True))

     docListTFC= docList[docList['tfc']==True]
     totalValue=sum((docListTFC['revenue']))
     insightTotalText="The total value of all contracts where TFC=yes is {}".format(locale.currency(totalValue,grouping=True))

     return  (filteredDocumentTable, pdfRendered,reviewGraphSlider(docList,sliderConf[0],sliderConf[1],sliderRev[0],sliderRev[1]),revPlot(sampledDf), reviewTitle, numReviewedText, numNotReviewedText,progressReviewed,progressNotReviewed,insightText,insightTotalText)

layout = html.Div(
    [
        dbc.Row([testingSection,timerSection,overviewSection, statsSection]),
        dbc.Row(pdf_viewer),
        dcc.Store(id='dataStore'),
    ]
)

# if __name__ == "__main__":
#     app.run_server(debug=True)
