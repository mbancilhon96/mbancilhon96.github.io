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

#import csv of contracts and contract info
docList= pd.read_csv('assets/files/testFiles/docList.csv')
docList['tfcProjection']=docList["tfcConfidence"]
docList['tfcAllTrue'] = docList.apply(lambda x: 1.0, axis=1)
docList['tfcAllFalse'] = docList.apply(lambda x: 0.0, axis=1)
# print("docList is ",docList)


def load_annotations(json_file_path):
    arr = []
    with open(json_file_path, 'r') as file:
        for line in file:
            arr.append(json.loads(line))
    return arr


#create doc table
mypath= "assets/files/testFiles/"
allFiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
print("all Files is ")
print(allFiles)

documentTable=[]

#interaction variables
dfUserActivity=pd.DataFrame()
reviewGraphHovers=[]
projectionGraphHovers=[]
confidenceParamClicks=[]
revenueParamClicks=[]
timeStart=time.time()
contractReviews=[]

documentTable.append(
{
    "contractId": "DR3215053",
    "impactFactor": 5250,
    "data": {
        "key": "DR3215053_00873923_Parent.pdf",
        "fileUrl": "assets/files/DR3215053_00873923_Parent.pdf",
        "fileName": "DR3215053_00873923_Parent",
        "highlightsArr": [
          { "@context": ["https://www.w3.org/ns/anno.jsonld", "https://comments.acrobat.com/ns/anno.jsonld"], "id": "7f79dd7c-265c-4fad-90e8-693e2fa4309e", "type": "Annotation", "motivation": "commenting", "bodyValue": "1. Example sentence highlight 1.", "target": { "source": "DR3215053", "selector": { "node": { "index": 0 }, "quadPoints": [59.095872, 673.3267731199998, 336.7232149708801, 673.3267731199998, 59.095872, 665.3595411199998, 336.7232149708801, 665.3595411199998], "opacity": 0.4, "subtype": "highlight", "boundingBox": [0, 0, 595, 842], "strokeColor": "#90EE90", "type": "AdobeAnnoSelector" } }, "creator": { "category": "Clause", "name": "TFC", "type": "Person", "isReviewed": False, "isCorrect": True }, "created": "2022-07-19T13:52:20Z", "modified": "2022-07-19T13:52:20Z" }
        ],
        "endUser": "",
        "region": "Americas",
        "fiscalYear": 2021,
        "marketArea": "",
        "revenue": 150000,
        "tfcConfidence": 0.65
      }
  }
)

pdfList=[]
jsonLinesList=[]
for fileName in allFiles:
    if ".pdf" in fileName:
        fileNameNoExt=os.path.splitext(fileName)[0]
        pdfList.append(fileName)
        contractID=fileName.split('_')[0]
        dictContract = {}
        contractInfo = {}
        dictContract['contractId']= contractID
        contractInfo['key']=fileName
        contractInfo['fileUrl']= "assets/files/testFiles/{}".format(fileName)
        contractInfo['fileName']=fileNameNoExt
        annotationUrl= "assets/files/testFiles/{}_annot.jsonlines".format(contractID)

        highlightsArr= load_annotations(annotationUrl)
        highlightsArr[0]['target']['source']= contractID
        highlightsArr[0]['creator']['isReviewed']= docList.loc[docList['contractID'] == contractID, 'reviewed'].iloc[0]
        highlightsArr[0]['creator']['isCorrect']= docList.loc[docList['contractID'] == contractID, 'tfc'].iloc[0]

        contractInfo['highlightsArr']=highlightsArr

        # contractInfo['tfc']=docList.loc[docList['contractID'] == contractID, 'tfc'].iloc[0]
        contractInfo['tfcConfidence']=docList.loc[docList['contractID'] == contractID, 'tfcConfidence'].iloc[0]
        contractInfo['revenue']=docList.loc[docList['contractID'] == contractID, 'revenue'].iloc[0]
        # contractInfo['reviewed']=docList.loc[docList['contractID'] == contractID, 'reviewed'].iloc[0]
        contractInfo['endUser']=docList.loc[docList['contractID'] == contractID, 'endUser'].iloc[0]
        contractInfo['region']=docList.loc[docList['contractID'] == contractID, 'region'].iloc[0]
        contractInfo['fiscalYear']=docList.loc[docList['contractID'] == contractID, 'fiscalYear'].iloc[0]
        contractInfo['marketArea']=docList.loc[docList['contractID'] == contractID, 'marketArea'].iloc[0]
        # compute impact factor as revenue * 1-confidence
        dictContract['impactFactor']=float(contractInfo['revenue'] * (1- contractInfo['tfcConfidence']))
        dictContract['data']=contractInfo
        documentTable.append(dictContract)

# order in descending order of impact factor
documentTableSorted= sorted(documentTable, key=itemgetter('impactFactor'), reverse=True)
print("document table sorted is ",documentTableSorted)
print(documentTableSorted[0]['impactFactor'])
documentTable=documentTableSorted

def samplingData(df, conf):
    data = []  # [[200, 0.7], [10, 1.0], [300, 0.5]]
    data_reviewed = []
    n_reviews = 0

    contract_values=df['revenue']
    confidences=conf

    for v, c in zip(contract_values, confidences):
        data.append([v, c])

        # some arbitrary toy strategy for reviewing
        if rand() > 0.9:
            n_reviews = n_reviews + 1
            data_reviewed.append([v, round(c - 0.2)])
        else:
            data_reviewed.append([v, c])

    df = pd.DataFrame(data, columns=['contract-value', 'confidence'])

    n_repetitions = 1000
    sample = {}

    for contract_value, confidence in data:
        s = np.random.binomial(1, confidence, n_repetitions)
        s = [x * contract_value for x in s]
        sample[str(contract_value) + '@' + str(confidence) + '@' + str(randint(0, 10000000, 1)) ] = s

    df_sample_results = pd.DataFrame(sample)
    df_sample_results['total at risk without reviews'] = df_sample_results.sum(axis=1)
    return df_sample_results


def revPlot(dfNotSampled, dfOrig, dfNew, trueReviewsSamples, falseReviewsSamples):
    fig = go.Figure()

    dfReviewed=dfNotSampled[dfNotSampled['reviewed']=="1"]
    dfNotReviewed=dfNotSampled[dfNotSampled['reviewed']=="0"]
    dfReviewedSample= samplingData(dfReviewed,dfReviewed["tfcProjection"])
    dfNotReviewedSample= samplingData(dfNotReviewed,dfNotReviewed["tfcProjection"])

    fig.add_trace(go.Box(x=trueReviewsSamples['total at risk without reviews'],
                         name="All True Reviews", marker_color = 'steelblue'))
    fig.add_trace(go.Box(x=falseReviewsSamples['total at risk without reviews'],
                         name="All False Reviews", marker_color = 'steelblue'))
    fig.add_trace(go.Box(x=dfOrig['total at risk without reviews'],
                         name="Probabilistic total", marker_color = 'steelblue'))
    fig.add_trace(go.Box(x=dfReviewedSample['total at risk without reviews'],
                         name="Probabilistic reviewed", marker_color='#66c2a5'))
    fig.add_trace(go.Box(x=dfNotReviewedSample['total at risk without reviews'],name="Probabilistic not reviewed", marker_color='#FFA500'))
    fig.add_annotation(
        x=max(trueReviewsSamples['total at risk without reviews']), y=0+0.25, text=f'Maximum possible revenue', yanchor='bottom', showarrow=False, arrowhead=1, arrowsize=1
        , arrowwidth=2, arrowcolor="#636363", ax=-20, ay=-30, font=dict(size=11, color="steelblue", family="Sans Serif"), align="left")

    fig.add_annotation(
        x=min(falseReviewsSamples['total at risk without reviews']), y=1 + 0.25, text=f'Minimum possible revenue',
        yanchor='bottom', showarrow=False, arrowhead=1, arrowsize=1
        , arrowwidth=2, arrowcolor="#636363", ax=-20, ay=-30,
        font=dict(size=11, color="steelblue", family="Sans Serif"), align="left")

    fig.add_annotation(
        x=statistics.median(dfOrig['total at risk without reviews']), y=2 + 0.25, text=f'Most likely revenue',
        yanchor='bottom', showarrow=False, arrowhead=1, arrowsize=1
        , arrowwidth=2, arrowcolor="#636363", ax=-20, ay=-30,
        font=dict(size=11, color="steelblue", family="Sans Serif"), align="left")

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
    # fig.update_traces(marker=dict(color='#66c2a5')
    #                   ,selector=dict(mode='markers'))
    fig.update_layout(
        font_size=10, #tick labels
        showlegend=False,
        margin=dict(l=20, r=20, t=20, b=20),
    )
    fig.update_xaxes(title_font_family="Arial",title_font_size=12 )
    fig.update_yaxes(title_font_family="Arial",title_font_size=12 )

    return fig

testingSection=  dbc.Row([
                    dbc.Row([
                        dbc.Button("i", id="testingInfoOpen", className="me-1", n_clicks=0, color="light",
                                                                   style={'margin': '0', 'font-size': 14,
                                                                          'border-radius': 10, 'width': '20px', }),
                        html.Header("Testing Section",
                                    style={'margin':'auto','font-size': 18,
                                           'text-align': 'center'}),
                    ]),
                    dbc.Row([
                            html.Header("Using the information and features provided below, find the closest possible"
                                        " estimate for the largest revenue at risk due to termination for convenience. "
                                        "You will have up to an hour to complete this task but feel free to submit your answer when"
                                        " you are confident with it. To submit, press the submit button below. Please note that once"
                                        " your answer is submitted, you will not be able to go back to change it." ,
                                        style={'margin-top': '20px','margin-bottom': '0px','font-size': 12,'height': 'auto','width':'auto'}),
                    ],style={'height':'auto','padding-right':'200px','padding-left':'200px'}),
                    dbc.Row([
                        html.Header(html.Br()),
                        dbc.Col([html.Header("What is your estimate?($)",style= {'width':'200px','margin-top':'5px','font-size': 12})],width=5),
                        dbc.Col([
                            dcc.Input(
                            id="estimateInput",
                            type="number",
                            placeholder="your answer",
                            style= {'width':'200px','margin-left':'32px','font-size': 12,'align':'left'}
                            )
                        ])
                    ],style={'marginLeft':'100px','marginRight':'100px','padding-right':'200px','padding-left':'200px'}),
                    dbc.Row([
                        html.Header(html.Br()),
                        dbc.Col([html.Header("How confident are you in this estimate? (%)",
                                             style={'width': '300px', 'margin-top': '5px', 'font-size': 12})],
                                width=5),
                        dbc.Col([
                            dcc.Input(
                                id="confidenceInput",
                                type="number",
                                placeholder="your answer",
                                style={'width': '200px', 'margin-left': '32px', 'font-size': 12, 'align': 'left'}
                            )
                        ])
                    ],style={'marginLeft':'100px','marginRight':'100px','padding-right':'200px','padding-left':'200px'}),
                    dbc.Row([
                        html.Header(html.Br()),
                        html.A(html.Button('Submit', id='submitAnswer', n_clicks=0, style={'display':'flex','align-items':'center','justify-content': 'center','font-size': 12}),href="/nasa-tlx", style={'display':'flex','align-items':'center','justify-content': 'center'}),
                        dcc.Download(id="downloadUserActivity"),
                    ])
                ],style={'background': 'white','color':'#43464B','padding': '20px','margin-right':'10px','margin-top':'10px','border-radius': '6px 6px 6px 6px'})


parameterSection=  dbc.Col([
                            dbc.Row([
                                dbc.Button("i", id="paramInfoOpen", className="me-1", n_clicks=0, color="light",
                                           style={'margin': '0', 'font-size': 14,
                                                  'border-radius': 10, 'width': '20px', }),
                                dbc.Modal(
                                    [
                                        dbc.ModalHeader(dbc.ModalTitle("Parameters")),
                                        dbc.ModalBody("Specify the thresholds for the confidence and contract revenue you would like to review. The total number of contracts within those thresholds as well as the confidence and revenue for each contract is displayed in the Overview section"),
                                        dbc.ModalFooter(
                                            dbc.Button(
                                                "Close", id="paramClose", className="ms-auto", n_clicks=0
                                            )
                                        ),
                                    ],
                                    id="paramModal",
                                    is_open=False,
                                ),

                            ]),
                            dbc.Row([
                                html.Header("Parameters",
                                            style={'margin':'auto','font-size': 18,
                                                   'text-align': 'center'}),
                            ]),
                            dbc.Row([
                                    dbc.Col([html.Header("TFC confidence to review",style={'margin-top': '20px','margin-bottom': '0px', 'margin-left': '40px', 'font-size': 12})]),
                                    dbc.Col([html.Div([dcc.RangeSlider(0.5, 1, id='slider_confidence', marks=None, step=0.05,value=[0.5,1],tooltip={"placement": "bottom", "always_visible": True})],
                                        style={'margin-top': '20px','width': '200px', 'padding-top': '5px'})]),
                            ]),
                            dbc.Row([
                                dbc.Col([html.Header("Value to review ($)", style={'margin-bottom': '0px', 'margin-left': '40px', 'font-size': 12})]),
                                dbc.Col([html.Div([dcc.RangeSlider(0, max(docList['revenue'])+10, id='slider_revenue', marks=None, step=10,value=[0,max(docList['revenue'])+10],tooltip={"placement": "bottom", "always_visible": True})],
                                        style={'width': '200px', 'display': 'inline-block', 'padding-top': '5px'})]),
                            ]),
                            dbc.Row([
                                    dbc.Col([
                                        html.Header("Region",
                                                    style={'margin-top': '20px', 'margin-right': '20px',
                                                           'margin-left': '40px', 'font-size': 12}),
                                    ]),
                                    dbc.Col([
                                        html.Button('All', id='regionAll', n_clicks=0, style={'font-size': 12}),
                                        html.Button('Americas', id='regionAmericas', n_clicks=0, style={'font-size': 12}),  # Region filter
                                        html.Button('EMEA', id='regionEMEA', n_clicks=0, style={'font-size': 12})
                                    ])
                            ]),
                            dbc.Row([
                                dbc.Col([
                                    html.Header("Fiscal Year",
                                                style={'margin-top': '10px', 'margin-right': '20px', 'margin-bottom': '0px',
                                                       'margin-left': '40px', 'font-size': 12})
                                ]),
                                dbc.Col([
                                    dcc.Dropdown(["All"] + list(np.unique(np.array(docList['fiscalYear']))), "All",
                                                 id='fiscalYearDropdown', style={'width': '100%', 'padding-right': '10px','font-size':12}),
                                ])
                            ])
                        ],style={'background': 'white','color':'#43464B','padding': '20px','margin-right':'10px','margin-top':'10px','border-radius': '6px 6px 6px 6px'})

overviewSection=dbc.Col([
                    dbc.Row([
                        dbc.Button("i", id="overviewInfoOpen", className="me-1",n_clicks=0,color="light",style={'margin':'0','font-size': 14,
'border-radius' : 10,'width':'10px',}),
                        dbc.Modal(
                            [
                                dbc.ModalHeader(dbc.ModalTitle("Overview")),
                                dbc.ModalBody("This section displays how many contracts are within the Parameters that you set for reviewing. In the graph, you can see each individual contract as a point and see their confidence and value. "),
                                dbc.ModalFooter(
                                    dbc.Button(
                                        "Close", id="overviewClose", className="ms-auto", n_clicks=0
                                    )
                                ),
                            ],
                            id="overviewModal",
                            is_open=False,
                        ),
                    ]),

                    dbc.Row([
                        html.Header("Overview",
                                    style={'margin':'auto', 'font-size': 18,
                                           'text-align': 'center'})
                    ]),
                    # progress bar
                    dbc.Row([
                        dbc.Col([
                            dbc.Progress([
                                dbc.Progress(value=0, id="progressReviewed", color="#66c2a5", bar=True),
                                dbc.Progress(value=100, id="progressNotReviewed", color="#FFA500", bar=True)
                            ], style={'height': "8px", "width": "200px", 'padding': "0px", "font-size": "14px",
                                      'border-radius': '12px 12px 12px 12px', 'margin-top': '15px',
                                      'margin-left': '100px', 'align': 'center'}),
                            html.Header("{} reviewed".format(
                                docList[(docList['tfc'] == True) & (docList['reviewed'] == True)].shape[
                                    0]),
                                id="numReviewed",
                                style={'display': 'inline-block', 'text-align': 'center',
                                       'margin-right': '10px', 'color': '#66c2a5',
                                       'padding': '0px', 'margin-left': "100px", 'font-size': '12px',
                                       'margin-bottom': '0px'}),
                            html.Header("{} not reviewed".format(
                                docList[(docList['tfc'] == "Y") & (docList['reviewed'] == "0")].shape[0]),
                                id="numNotReviewed",
                                style={'display': 'inline-block', 'text-align': 'right',
                                       'margin-right': '10px', 'color': '#FFA500',
                                       'padding': '0px', 'margin-left': "25px", 'font-size': '12px',
                                       'margin-bottom': '0px'})
                        ]),
                        dbc.Col([
                            html.Header("{} contracts".format(docList[docList['tfc'] == True].shape[0]),
                                        id="numReviews",
                                        style={'color': '#7E7E7E', 'font-size': '16px','margin-top':'5px'}),
                        ])
                    ]),
                    # review graph
                    dbc.Row([
                        dcc.Graph(id="reviewGraph", figure=reviewGraph(docList),
                                  style={'width': '30vh', 'height': '25vh', 'margin-left': '90px', 'margin': 'auto'})
                    ]),
            ],style={'background': 'white','color':'#43464B','padding': '20px','margin-right':'10px','margin-top':'10px','border-radius': '6px 6px 6px 6px'})

sampledData1=samplingData(docList, docList['tfcConfidence'])
sampledData2=samplingData(docList, docList['tfcProjection'])
sampledData3=samplingData(docList, docList['tfcAllTrue'])
sampledData4= samplingData(docList, docList['tfcAllFalse'])

listSampled2= list(sampledData2['total at risk without reviews'])
mostLikelyRev=mode(listSampled2)
#mostLikelyRevRange=
quantiles= list(sampledData2['total at risk without reviews'].quantile([0.25,0.5,0.75]))
lowerQuantile=quantiles[0]
median= quantiles[1]
upperQuantile=quantiles[2]
iqr = upperQuantile - lowerQuantile
upper_whisker = sampledData2['total at risk without reviews'][sampledData2['total at risk without reviews']<=upperQuantile+1.5*iqr].max()
lower_whisker = sampledData2['total at risk without reviews'][sampledData2['total at risk without reviews']>=lowerQuantile-1.5*iqr].min()

statsSection= dbc.Col([
                    dbc.Row([
                        dbc.Button("i", id="statsInfoOpen", className="me-1", n_clicks=0, color="light",
                                   style={'margin': '0', 'font-size': 14,
                                          'border-radius': 10, 'width': '20px', }),
                        dbc.Modal(
                            [
                                dbc.ModalHeader(dbc.ModalTitle("Insights")),
                                dbc.ModalBody(
                                    "We used a sampling technique to provide statistics for the total estimated revenue at risk from all contracts containing Termination for Convenience clauses. The box plot shows the range of possible values. "),
                                dbc.ModalFooter(
                                    dbc.Button(
                                        "Close", id="statsClose", className="ms-auto", n_clicks=0
                                    )
                                ),
                            ],
                            id="statsModal",
                            is_open=False,
                        ),
                    ]),
                    dbc.Row([
                        html.Header("Insights",
                                    style={'margin':'auto','font-size': 18,
                                           'text-align': 'center'}),
                    ]),
                    dbc.Row([
                        html.Header("The most likely total revenue at risk is {}".format(locale.currency(median,grouping=True)),
                                    id="insight1",
                                    style={'margin':'auto','margin-bottom':'5px','margin-top':'20px','font-size': 12,
                                           'text-align': 'center'}),
                    ]),
                    dbc.Row([
                        html.Header(
                            "There is a 50% chance that the total revenue at risk is between {} and {}.".format(locale.currency(lowerQuantile, grouping=True), locale.currency(upperQuantile, grouping=True)),
                            id="insight2",
                            style={'margin': 'auto', 'margin-bottom': '5px', 'margin-top': '5px', 'font-size': 12,
                                   'text-align': 'center'}),
                    ]),
                    dbc.Row([
                        html.Header(
                            "It is highly certain that the total revenue at risk is between {} and {}".format(locale.currency(lower_whisker, grouping=True), locale.currency(upper_whisker, grouping=True)),
                            id="insight3",
                            style={'margin': 'auto', 'margin-bottom': '20px', 'margin-top': '5px', 'font-size': 12,
                                   'text-align': 'center'}),
                    ]),
                    #projection graph
                    dbc.Row([
                            dcc.Graph(id="graph-Projections",figure=revPlot(docList,sampledData1,sampledData2,sampledData3,sampledData4),
                                    style={'width': '60vh', 'height': '20vh','align':'left','margin-top':'0px','margin':'auto'})
                    ])
],style={'background': 'white','color':'#43464B','padding': '20px','margin-right':'10px','margin-top':'10px','border-radius': '6px 6px 6px 6px'})

pdf_viewer = dbc.Col([
                dbc.Row([
                        dbc.Button("i", id="pdfInfoOpen", className="me-1", n_clicks=0, color="light",
                                   style={'margin': '0', 'font-size': 14,
                                          'border-radius': 10, 'width': '20px', }),
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
                dbc.Row([
                    html.Header("Document Review",
                                style={'margin':'auto','font-size': 18,
                                       'text-align': 'center'}),
                    html.Header(html.Br()),

                ]),
                dbc.Row([
                    html.Header("Click a document in the left side bar to view it as a pdf. The documents in the left sidebar are ordered by highest impact factor first. Head to the right sidebar to confirm or refute TFC clause detection in the document.",
                                style={'margin': 'auto', 'font-size': 14,
                                       'text-align': 'center'}),
                    html.Header(html.Br()),
                ]),
                dbc.Row(
                    [
                        dash_pdf_components.DashPdfComponents(
                            id='pdf-view',
                            label='pdf-view-label',
                            pdfRendered="DR3215053",
                            apiKey=API_KEY,
                            documentTable=documentTable,
                            toggle=False
                        )
                    ],
                    id='pdf-col',
                )
            ],style={'background': 'white', 'color': '#43464B', 'padding': '20px', 'margin-right': '10px',
                           'margin-top': '10px', 'border-radius': '6px 6px 6px 6px'})

#
timerSection=html.Div([
    dcc.Interval(id='interval1', interval=1 * 1000, n_intervals=0),
    html.H1(id='label1', children='')
])
#callback for info buttons
@callback(Output('overviewModal', 'is_open'),
    [Input('overviewInfoOpen', 'n_clicks'),Input("overviewClose", "n_clicks")],
    [State("overviewModal", "is_open")])
def showOverviewModal(overviewInfoOpen,overviewClose,is_open):
        if overviewClose or overviewInfoOpen:
            return not is_open
        return is_open

@callback(Output('paramModal', 'is_open'),
    [Input('paramInfoOpen', 'n_clicks'),Input("paramClose", "n_clicks")],
    [State("paramModal", "is_open")])
def showParamModal(paramInfoOpen,paramInfoClose,is_open):
        if paramInfoClose or paramInfoOpen:
            return not is_open
        return is_open

@callback(Output('statsModal', 'is_open'),
    [Input('statsInfoOpen', 'n_clicks'),Input("statsClose", "n_clicks")],
    [State("statsModal", "is_open")])
def showStatsModal(statsInfoOpen,statsClose,is_open):
        if statsClose or statsInfoOpen:
            return not is_open
        return is_open

#callback for timer
# @callback(Output('label1', 'children'),
#     [Input('interval1', 'n_intervals')])
# def update_interval(n):
#     secondsLeft=900 -n  #15 minutes - time elapsed
#     return 'Time Remaining: ' + str(datetime.timedelta(seconds=secondsLeft))

#TODO: automatically submit page when time is over


#graph callback
#TODO: merge with pdf-view callback
@callback(
    [ Output('reviewGraph', 'figure'),
     Output('graph-Projections', 'figure'),
     Output('numReviews','children'),
     Output('numReviewed','children'),
      Output('numNotReviewed', 'children'),
      Output('progressReviewed','value'),
     Output('progressNotReviewed', 'value'),
    # Output('output_contract', 'children'),
      Output("pdf-view", "documentTable"),
      Output("insight1", "children"),
      Output("insight2", "children"),
      Output("insight3", "children")
      ],
    [ Input('slider_confidence', 'value'),  #confidence slider
     Input('slider_revenue', 'value'),
     Input('fiscalYearDropdown', 'value'),  #fiscal year dropdown filter
     Input('regionAll', 'n_clicks_timestamp'),
     Input('regionAmericas', 'n_clicks_timestamp'),
     Input('regionEMEA', 'n_clicks_timestamp'),
      Input("pdf-view", "key"),
      Input("pdf-view", "pdfRendered"),
      Input("pdf-view", "documentTable"),
      Input("pdf-view", "toggle"),
      # mouse events
      Input("reviewGraph", "hoverData"),
      Input("graph-Projections","hoverData"),
        Input('estimateInput', 'value'),
        Input('confidenceInput', 'value'),
        Input('submitAnswer', 'n_clicks_timestamp'),
      ]
)   #review sliders min and max
def updateGraphs(sliderVal,sliderRev, fiscalYearFilter, regionAll, regionAmericas, regionEMEA,key, currContractId, docTableUpdates, toggle, reviewGraphMouseOn,graphProjectionsMouseOn,estimateInput,confidenceInput, submitAnswer):
    print("inside callback")
    global dfUserActivity
    global docList
    df=docList
    global confidenceParamClicks
    global revenueParamClicks
    global reviewGraphHovers
    global projectionGraphHovers
    global timeStart

    #record mouse events
    if reviewGraphMouseOn != None:
        xCoord=reviewGraphMouseOn['points'][0]['x']
        yCoord=reviewGraphMouseOn['points'][0]['y']
        dictHover={"x":xCoord,"y":yCoord,"timestamp":time.time()}
        reviewGraphHovers.append(dictHover)

    if graphProjectionsMouseOn != None:
        xCoord=graphProjectionsMouseOn['points'][0]['x']
        yCoord=graphProjectionsMouseOn['points'][0]['y']
        dictHover={"x":xCoord,"y":yCoord,"projectionTimestamp":time.time()}
        projectionGraphHovers.append(dictHover)

    elementTriggered=ctx.triggered_id
    print("the element triggered is ",elementTriggered)
    #if slider_confidence is changed
    if elementTriggered=="slider_confidence":
        confValue0=sliderVal[0]
        confValue1=sliderVal[1]
        confTimestamp=time.time()
        dictConf={"confValue0":confValue0, "confValue1":confValue1,"confTimestamp":confTimestamp}
        confidenceParamClicks.append(dictConf)
    elif elementTriggered=="slider_revenue":
        revValue0=sliderRev[0]
        revValue1=sliderRev[1]
        revTimestamp=time.time()
        dictRev={"revValue0":revValue0, "revValue1":revValue1,"revTimestamp":revTimestamp}
        revenueParamClicks.append(dictRev)

    button_pressed = np.nanargmax(
        np.array(
            [0, submitAnswer,regionAll, regionAmericas, regionEMEA], dtype=np.float64
        ))
    if button_pressed == 1:  # user submitted their answer
        print("submit button has been pressed")
        dfCurrentUser=pd.DataFrame({"userID": [uuid.uuid1()], #generate random user ID
                                     "timeStart":[timeStart],
                                     "timeEnd":[time.time()],
                                     "estimateInput":[estimateInput],
                                     "confidenceInput":[confidenceInput],
                                    "confParamClicks": [confidenceParamClicks],
                                    "revenueParamClicks": [revenueParamClicks],
                                    "reviewGraphHovers":[reviewGraphHovers],
                                     "projectionGraphHovers":[projectionGraphHovers],
                                    "userReviews":[contractReviews],})

        try: #if df is not empty
            dfUserActivity=pd.read_csv("dfUserActivity.csv",index_col=[0])
            updatedUserActivity=dfUserActivity.append(dfCurrentUser)
            updatedUserActivity.to_csv("dfUserActivity.csv", mode='a',header=False)  # append mode
        except:
            updatedUserActivity = dfCurrentUser #if df is empty
            updatedUserActivity.to_csv("dfUserActivity.csv", mode='a')  # append mode
        #updatedUserActivity.to_csv("dfUserActivity.csv",mode='a') #append mode

    #update docList based on reviews
    for item in docTableUpdates:
        if item["contractId"] == currContractId:
            itemChanged= item["data"]["highlightsArr"][0]["creator"]  #item that is being changed
            #update dataframe for this contract
            docList['reviewed']=docList.apply(lambda x: itemChanged['isReviewed'] if x['contractID']==currContractId else x['reviewed'], axis=1)
            docList['tfc']=docList.apply(lambda x: itemChanged['isCorrect'] if x['contractID']==currContractId else x['tfc'], axis=1)
            print("contract number ", currContractId," is being reviewed")
            print("is reviewed is ", itemChanged['isReviewed'])
            #itemChanged['isReviewed'] indicates when item has been reviewed
            #create timestamp here with review (approve or refute)
            if itemChanged['isReviewed']:
                contractReviews.append({"contractID":currContractId,"timeReviewed":time.time(),"isTFCCorrect":itemChanged['isCorrect']})

    #==Filters==
    if fiscalYearFilter!="All":
        df = df[df['fiscalYear'] == fiscalYearFilter]
        title = "Total Revenue at Risk for %s" % (fiscalYearFilter)
    else:
        title="Total Revenue at Risk"

    #region buttons

    if button_pressed==3:
        df = df[df['region'] == "Americas"]
        title = title + " in the Americas"
    elif button_pressed==4:
        df = df[df['region'] == "EMEA"]
        title = title + " in EMEA"

    df['tfcProjection']=df.apply(lambda x: 1.0 if x['reviewed']==True else x['tfcConfidence'], axis=1)
    df['tfcAllTrue'] = df.apply(lambda x: x['tfcProjection'] if x['tfc'] == True and ( float(x['revenue']) > sliderRev[1] or float(x['revenue'] < sliderRev[0]) or  float(x['tfcProjection']) > sliderVal[1] or float(x['tfcProjection']) < sliderVal[0]) else 1.0, axis=1)
    df['tfcAllFalse'] = df.apply(lambda x: x['tfcProjection'] if x['tfc'] == True and ( float(x['revenue']) > sliderRev[1] or float(x['revenue'] < sliderRev[0]) or  float(x['tfcProjection']) > sliderVal[1] or float(x['tfcProjection']) < sliderVal[0]) else 0.0, axis=1)
    newDocumentTable=[]
    for item in docTableUpdates:
        if (item['data']['revenue'] < sliderRev[1] and item['data']['revenue'] > sliderRev[0]) and (item['data']['tfcConfidence'] < sliderVal[1] and item['data']['tfcConfidence'] > sliderVal[0]):
            newDocumentTable.append(item)  #add item to newDocumentTable


    # print("length newDocumentTable is ",len(newDocumentTable))
    #======create sampling data for box plot=====
    origData=samplingData(df,df['tfcProjection'])
    allTrueSampled=samplingData(df,df['tfcAllTrue'])
    allFalseSampled=samplingData(df,df['tfcAllFalse'])

    listSampled2 = list(origData['total at risk without reviews'])
    quantiles = list(origData['total at risk without reviews'].quantile([0.25, 0.5, 0.75]))
    lowerQuantile = quantiles[0]
    median = quantiles[1]
    upperQuantile = quantiles[2]
    iqr = upperQuantile - lowerQuantile
    upper_whisker = origData['total at risk without reviews'][
        sampledData2['total at risk without reviews'] <= upperQuantile + 1.5 * iqr].max()
    lower_whisker = origData['total at risk without reviews'][
        sampledData2['total at risk without reviews'] >= lowerQuantile - 1.5 * iqr].min()

    #update insights
    insight1Text= "The most likely total revenue at risk is {}".format(locale.currency(median,grouping=True))
    insight2Text= "There is a 50% chance that the total revenue at risk is between {} and {}.".format(locale.currency(lowerQuantile, grouping=True), locale.currency(upperQuantile, grouping=True))
    insight3Text= "It is highly certain that the total revenue at risk is between {} and {}".format(locale.currency(lower_whisker, grouping=True), locale.currency(upper_whisker, grouping=True)),

    # ====display quantities for total, reviewed, not reviewed=====
    dfTotalToReview= df[ (df['tfcConfidence']> sliderVal[0]) & (df['tfcConfidence']< sliderVal[1])]
    dfTotalToReview= dfTotalToReview[ (dfTotalToReview['revenue']> sliderRev[0]) & (dfTotalToReview['revenue']< sliderRev[1])]
    dfTotalToReview['tfcProjection']=dfTotalToReview.apply(lambda x: 1.0 if x['reviewed']==True else x['tfcConfidence'], axis=1)

    if dfTotalToReview.empty:
        numReviews=0
    else:
        numReviews=dfTotalToReview.shape[0]
    reviewTitle="{} contracts".format(int(numReviews))

    dfReviewed= dfTotalToReview[dfTotalToReview['reviewed']==True]
    if dfReviewed.empty:
        numReviewed=0
    else:
        numReviewed=dfReviewed.shape[0]
    numReviewedText="{} reviewed".format(int(numReviewed))

    dfNotReviewed= dfTotalToReview[dfTotalToReview['reviewed']==False]
    if dfNotReviewed.empty:
        numNotReviewed=0
    else:
        numNotReviewed=dfNotReviewed.shape[0]
    numNotReviewedText="{} not reviewed".format(int(numNotReviewed))

    progressReviewed=(int(numReviewed)/(int(numNotReviewed)+int(numReviewed)))*100
    progressNotReviewed=(int(numNotReviewed)/(int(numNotReviewed)+int(numReviewed)))*100

    return (reviewGraphSlider(df,sliderVal[0],sliderVal[1],sliderRev[0],sliderRev[1]),revPlot(dfTotalToReview,origData,origData,allTrueSampled,allFalseSampled) ,reviewTitle, numReviewedText, numNotReviewedText,progressReviewed,progressNotReviewed,newDocumentTable, insight1Text,insight2Text,insight3Text)


layout = html.Div(
    [
        dbc.Row([testingSection,overviewSection,parameterSection, statsSection]),
        dbc.Row(pdf_viewer),
    ]
)

# if __name__ == "__main__":
#     app.run_server(debug=True)
