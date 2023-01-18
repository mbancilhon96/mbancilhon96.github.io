# from dash import Dash, dash_table, ctx
import dash
from dash import html, Input, Output, State, callback_context, dash_table
import pandas as pd
from collections import OrderedDict
import plotly.express as px
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
from itertools import compress, product, chain, combinations
import plotly.graph_objects as go
from operator import neg
import itertools
from plotly.subplots import make_subplots
#from poibin import PoiBin
#import poisson-binomial as poibin
from numpy.random import randint, rand, uniform
from plotly.tools import mpl_to_plotly
from collections import Counter
import dash_bootstrap_components as dbc

# app = Dash(__name__)
app = dash.Dash(
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    external_scripts=['https://documentcloud.adobe.com/view-sdk/main.js']
)
app.css.append_css({'external_url': '/static/styleDash.css'})
#=================================
#=======GLOBAL VARIABLES==========
#=================================

fig=go.Figure()

app.title = "Dash PDF Reader"
CONCORD_LOGO = app.get_asset_url("images/concord-logo-dark.png")
API_KEY = '899d52477b7d4b589f808242e8d36cc3' #This client ID only works for localhost


#=====================
#=======DATA==========
#=====================



docTable = [
  {
      "contractId": "DR3215053",
      "data": {
        "key": "DR3215053_00873923_Parent.pdf",
        "fileUrl": "assets/files/DR3215053_00873923_Parent.pdf",
        "fileName": "DR3215053_00873923_Parent",
        "highligtsArr": [
          { "@context": ["https://www.w3.org/ns/anno.jsonld", "https://comments.acrobat.com/ns/anno.jsonld"], "id": "7f79dd7c-265c-4fad-90e8-693e2fa4309e", "type": "Annotation", "motivation": "commenting", "bodyValue": "We think this sentence is important.", "target": { "source": "DR3215053", "selector": { "node": { "index": 0 }, "quadPoints": [59.095872, 673.3267731199998, 336.7232149708801, 673.3267731199998, 59.095872, 665.3595411199998, 336.7232149708801, 665.3595411199998], "opacity": 0.4, "subtype": "highlight", "boundingBox": [0, 0, 595, 842], "strokeColor": "#90EE90", "type": "AdobeAnnoSelector" } }, "creator": { "category": "Clause", "name": "Payment", "type": "Person" }, "created": "2022-07-19T13:52:20Z", "modified": "2022-07-19T13:52:20Z" }
        ],
        "tfc": true,
        "reviewed": false,
        "endUser": "",
        "region": "Americas",
        "fiscalYear": 2021,
        "marketArea": "",
        "revenue": 150000,
        "tfcConfidence": 0.85
      }
  },
  {
      "contractId": "DR3187459",
      "data": {
        "key": "DR3187459_00829261_Parent.pdf",
        "fileUrl": "assets/files/DR3187459_00829261_Parent.pdf",
        "fileName": "DR3187459_00829261_Parent.pdf",
        "highligtsArr":
          [{ "@context": ["https://www.w3.org/ns/anno.jsonld", "https://comments.acrobat.com/ns/anno.jsonld"], "id": "67hrdd7c-265c-4fad-90e8-693e2fa4309e", "type": "Annotation", "motivation": "commenting", "bodyValue": "We think this sentence is important.", "target": { "source": "DR3187459", "selector": { "node": { "index": 0 }, "quadPoints": [59.095872, 673.3267731199998, 336.7232149708801, 673.3267731199998, 59.095872, 665.3595411199998, 336.7232149708801, 665.3595411199998], "opacity": 0.4, "subtype": "highlight", "boundingBox": [0, 0, 595, 842], "strokeColor": "#90EE90", "type": "AdobeAnnoSelector" } }, "creator": { "category": "Clause", "name": "Payment", "type": "Person" }, "created": "2022-07-19T13:52:20Z", "modified": "2022-07-19T13:52:20Z" }],
        "tfc": true,
        "reviewed": false,
        "endUser": "",
        "region": "Americas",
        "fiscalYear": 2021,
        "marketArea": "",
        "revenue": 150000,
        "tfcConfidence": 0.85
      }
  }
]
#=====================
#=======FUNCTIONS=====
#=====================

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

    print(dfNotSampled)
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
        x=max(trueReviewsSamples['total at risk without reviews'])
        , y=0+0.25
        , text=f'Maximum possible revenue'
        , yanchor='bottom'
        , showarrow=False
        , arrowhead=1
        , arrowsize=1
        , arrowwidth=2
        , arrowcolor="#636363"
        , ax=-20
        , ay=-30
        , font=dict(size=11, color="purple", family="Sans Serif")
        , align="left"
        , )
    fig.layout.plot_bgcolor = 'white'
    fig.layout.paper_bgcolor = 'white'
    fig.update_layout(
        showlegend=False,
        margin=dict(l=0, r=0, t=0, b=0),
    )

    return fig


def reviewGraphSlider(df,x1,x2,y1,y2,revX1, revX2, revY1,revY2,type):
    fig = px.scatter(df, x="revenue", y="tfcConfidence",color="reviewed", color_discrete_sequence=[ '#FFA500', '#66c2a5'],
                     labels={
                         "tfcConfidence": "T for C confidence",
                         "revenue": "Contract Value"
                     })
    fig.update_traces(marker_size=5)
    fig.layout.plot_bgcolor = 'white'
    fig.layout.paper_bgcolor = 'white'
    # fig.update_traces(marker=dict(color='#66c2a5')
    #                   ,selector=dict(mode='markers'))

    if type=="hypothetical":
        print("inside hypothetical")
        fig.add_vline(x=revY1, line_width=3, line_dash="dash", line_color="steelblue")
        fig.add_vline(x=revY2, line_width=3, line_dash="dash", line_color="steelblue")
        fig.add_hline(y=revX1, line_width=3, line_dash="dash", line_color="steelblue")
        fig.add_hline(y=revX2, line_width=3, line_dash="dash", line_color="steelblue")
    elif type=="param":
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

def reviewGraph(df):
    fig = px.scatter(df, x="revenue", y="tfcConfidence",color="reviewed",color_discrete_sequence=[ '#FFA500', '#66c2a5'],
                     labels={
                         "tfcConfidence": "T for C confidence",
                         "revenue": "Contract Value"
                     })
    fig.update_traces(marker_size=5)
    fig.add_vline(x=0, line_width=2, line_dash="dash", line_color="steelblue")
    fig.add_vline(x=max(df['revenue']), line_width=2, line_dash="dash", line_color="steelblue")
    fig.add_hline(y=0, line_width=2, line_dash="dash", line_color="steelblue")
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

#=====================
#=======LAYOUT=====
#=====================

app.layout = html.Div(style={"background": "#f6f6f6",'padding':'0px'},children=[
    html.H1(style={"margin-left": "40px"}, children=['Adobe Contract Revenue Interface']),
    dcc.Store(id="testStore"),
    html.Div([
        #AI settings
        html.Div([
            # title
            html.Div([html.Header("Parameters",
                                  style={'margin-bottom': '10px', 'margin-left': '40px', 'font-size': 18,
                                         'text-align': 'center'}),
                    html.Div([
                        dbc.Button("i", id="infoParam", n_clicks=0),
                        dbc.Modal(
                            [
                                dbc.ModalBody(id="featureList", children=[
                                    html.Header("Choose your parameters for the subset of contracts you wish to review. The graphs in the statistics section will help you visualize the parameters.")
                                ]),
                                dbc.ModalFooter(dbc.Button("Ok, got it!", id="close", className="ms-auto", n_clicks=0)),
                            ], id="modal", is_open=False,
                        ),
                    ]),
                      # html.Button('i', id='infoParam', n_clicks=0)
            ], style={'display':'flex','text-align': 'center', 'font-weight':'bold','padding':'10px'}),
            # AI contract confidence
            html.Div(
                [html.Div([html.Header("Contract TFC confidence to review",
                                       style={'margin-bottom': '0px', 'margin-left': '40px', 'font-size': 14})],
                          style={'display': 'inline-block'}),
                 html.Div([dcc.RangeSlider(0, 1, id='slider_confidence', marks=None, step=0.05,value=[0,1],
                                      tooltip={"placement": "bottom", "always_visible": True})],
                          style={'width': '200px', 'display': 'inline-block', 'padding-top': '5px'})],
                style={'display': 'flex', 'padding-top': '5px'}),
            # AI contract revenue
            html.Div(
                [html.Div([html.Header("Contract values to review ($)",
                                       style={'margin-bottom': '0px', 'margin-left': '40px', 'font-size': 14})],
                          style={'display': 'inline-block'}),
                 html.Div([dcc.RangeSlider(0, max(dfContracts['revenue'])+10, id='slider_revenue', marks=None, step=10,value=[0,max(dfContracts['revenue'])+10],
                                      tooltip={"placement": "bottom", "always_visible": True})],
                          style={'width': '200px', 'display': 'inline-block', 'padding-top': '5px'})],
                style={'display': 'flex', 'padding-top': '5px'}),
            #region filter
            html.Div([
                html.Header("Region",
                            style={'margin-top': '20px', 'margin-right': '20px','margin-left': '40px', 'font-size': 14}),
                html.Button('All', id='regionAll', n_clicks=0),
                html.Button('Americas', id='regionAmericas', n_clicks=0),  # Region filter
                html.Button('EMEA', id='regionEMEA', n_clicks=0)
            ],style={'display': 'flex', 'padding-top': '5px'}),
            #fiscalYear dropdown
            html.Div([
                html.Header("Fiscal Year",
                            style={'margin-top': '10px', 'margin-right': '20px','margin-bottom': '0px', 'margin-left': '40px', 'font-size': 14}),
                html.Div([
                    dcc.Dropdown(["All"]+list(np.unique(np.array(dfContracts['fiscalYear']))), "All", id='fiscalYearDropdown',style={'width': '100%','padding-right':'10px'}),
                    html.Div(id='dd-output-container')
                ])
            ], style={'display': 'flex', 'padding': '0px','margin-bottom':'0px'}),
        ],
            id="reviewTab",
            style={'height':'350px','display': 'inline','margin-top': '10px','margin-bottom': '0px','background': 'white','color':'#43464B','padding': '20px','margin-right':'10px','border-radius': '6px 6px 6px 6px'}),
       #stats
        html.Div([
            html.Div([html.Header("Statistics",
                                  style={'margin-bottom': '10px', 'font-size': 18,
                                         'text-align': 'center'})],
                     style={'text-align': 'center', 'font-weight': 'bold', 'padding': '10px'}),
            html.Div([
                html.Div([
                    dbc.Progress(
                        [
                            dbc.Progress(value=0, id="progressReviewed", color="#66c2a5", bar=True),
                            dbc.Progress(value=100, id="progressNotReviewed", color="#FFA500", bar=True)
                        ], style={'height': "8px", "width": "250px", 'padding': "0px", "font-size": "14px",
                                  'border-radius': '12px 12px 12px 12px', 'margin-top': '15px'}),
                    html.Header("{} reviewed".format(
                        dfContracts[(dfContracts['TFC'] == "Y") & (dfContracts['reviewed'] == "1")].shape[0]),
                        id="numReviewed",
                        style={'display': 'inline-block', 'text-align': 'center',
                               'margin-right': '10px', 'color': '#66c2a5',
                               'padding': '0px', 'margin-left':"0px", 'font-size': '14px',
                               'margin-bottom': '0px'}),
                    html.Header("{} not reviewed".format(
                        dfContracts[(dfContracts['TFC'] == "Y") & (dfContracts['reviewed'] == "0")].shape[0]),
                        id="numNotReviewed",
                        style={'display': 'inline-block', 'text-align': 'center',
                               'margin-right': '10px', 'color': '#FFA500',
                               'padding': '0px', 'margin-left':"65px", 'font-size': '14px',
                               'margin-bottom': '0px'})
                ]),
                html.Header("{}".format(dfContracts[dfContracts['TFC'] == "Y"].shape[0]),
                                  id="numReviews",
                                  style={'display': 'inline-block','padding-bottom': '80px',
                                         'margin-right': '0px', 'color': '#7E7E7E',
                                         'margin-left': '10px', 'font-size': '24px'}),
                html.Header("contracts",
                                  style={'display': 'inline-block','padding-top':'9.5px',
                                         'margin-right': '10px', 'color': '#7E7E7E',
                                         'margin-left': '5px', 'font-size': '14px'})
            ],style={"display":"flex",'margin-left':"120px","height":"60px"}),


            html.Div([dcc.Graph(id="reviewGraph", figure=reviewGraph(dfContracts),style={'width': '30vh', 'height': '25vh','margin-left': '90px'}),
                        html.Div([
                            dbc.Button("i", id="infoReviewGraph", n_clicks=0),
                            dbc.Modal(
                                [dbc.ModalBody(id="reviewGraphInfo", children=[
                                    html.Header("Every dot represents a contract in the whole collection. The subset you chose you review by setting parameters are the contracts within the bounds of the blue lines. Green dots are contracts that have already been reviewed and yellow dots still need to be reviewed")
                                ]),
                                    dbc.ModalFooter(dbc.Button("Ok, got it!", id="closeReviewGraph", className="ms-auto", n_clicks=0)),
                                ], id="modalReviewGraph", is_open=False,
                            ),
                        ]),
            ],style={'display':'flex'}),
            html.Div([
                #button 1
                html.Div([
                    dbc.Button("i", id="infoBox1Btn", n_clicks=0),
                    dbc.Modal(
                        [dbc.ModalBody(id="infoBox1", children=[
                            html.Header("This boxplot shows the probabilistic range of total revenue at risk due to T for C for across contracts that have NOT been reviewed yet. This assumes that the likelihood of T for C clauses is the classifier's confidence.")
                        ]),
                         dbc.ModalFooter(
                             dbc.Button("Ok, got it!", id="closeBox1", className="ms-auto", n_clicks=0)),
                         ], id="modalBox1", is_open=False,
                    ),
                ]),
                #button 2
                #button 3
                #button 4
                #button 5
                dcc.Graph(id="graph-Projections",
                          figure=revPlot(dfContracts,
                                         samplingData(dfContracts, dfContracts['tfcConfidence']),
                                         samplingData(dfContracts, dfContracts['tfcProjection']),
                                         samplingData(dfContracts, dfContracts['tfcAllTrue']),
                                         samplingData(dfContracts, dfContracts['tfcAllFalse'])),
                          style={'width': '60vh', 'height': '40vh','align':'left','margin-top':'0px'})
            ],style={'display':'flex'})
        ], style={'display': 'inline','margin-top': '10px','background': 'white','color':'#43464B','padding': '20px','margin-right':'10px','margin-bottom':'10px','border-radius': '6px 6px 6px 6px'}),
      ] ,style={'display':'flex','margin':'20px'}),

        #import pdf viewer component
        DashPdfComponents(
            key = dfContracts['fileUrl'].iloc[0],
            id = 'pdf-view',
            label = 'pdf-view-label',
            apiKey = API_KEY,
            pdfRendered= dfContracts['contractID'].iloc[0],
            docTable=docTable
        )
])

#=====================
#=======CALLBACKS=====
#=====================
#

# @app.callback()
# def displayInfo:
@app.callback(
    Output("modalBox1", "is_open"),
    [Input("infoBox1Btn", "n_clicks"), Input("closeBox1", "n_clicks")],
    [State("modalBox1", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open
@app.callback(
    Output("modal", "is_open"),
    [Input("infoParam", "n_clicks"), Input("close", "n_clicks")],
    [State("modal", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

@app.callback(
    Output("modalReviewGraph", "is_open"),
    [Input("infoReviewGraph", "n_clicks"), Input("closeReviewGraph", "n_clicks")],
    [State("modalReviewGraph", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

#graphs callbacks
@app.callback(
    [ Output('reviewGraph', 'figure'),
     Output('graph-Projections', 'figure'),
     Output('numReviews','children'),
     Output('numReviewed','children'),
      Output('numNotReviewed', 'children'),
      Output('progressReviewed','value'),
     Output('progressNotReviewed', 'value'),

      ],
    [ Input('slider_confidence', 'value'),  #confidence slider
     Input('slider_revenue', 'value'),
     Input('fiscalYearDropdown', 'value'),  #fiscal year dropdown filter
     Input('regionAll', 'n_clicks_timestamp'),
     Input('regionAmericas', 'n_clicks_timestamp'),
     Input('regionEMEA', 'n_clicks_timestamp'),
     Input("pdf-view", "pdfRendered"),
      Input("pdf-view", "pdfRenderedTFC")]
)   #review sliders min and max
def updateGraphs(sliderVal,sliderRev, fiscalYearFilter, regionAll, regionAmericas, regionEMEA,pdfRendered,pdfRenderedTFC):

    global dfContracts

    #update dataframe from reviews
    dfContracts['reviewed'] = np.where(df['contractID'] == pdfRendered, True, dfContracts['reviewed'])
    dfContracts['tfc'] = np.where(df['contractID'] == pdfRendered, pdfRenderedTFC, dfContracts['tfc'])
    dfContracts['tfcConfidence'] = np.where(df['contractID'] == pdfRendered, 1, dfContracts['tfcConfidence'])

    #get original table data
    df=dfContracts

    #==Filters==
    # apply fiscal year filters
    if fiscalYearFilter!="All":
        df = df[df['fiscalYear'] == fiscalYearFilter]
        title = "Total Revenue at Risk for %s" % (fiscalYearFilter)
    else:
        title="Total Revenue at Risk"

    # apply region filters
    button_pressed = np.nanargmax(
        np.array(
            [0, regionAll, regionAmericas,regionEMEA], dtype=np.float64
        ))
    if button_pressed==2:
        df = df[df['region'] == "Americas"]
        title = title + " in the Americas"
    elif button_pressed==3:
        df = df[df['region'] == "EMEA"]
        title = title + " in EMEA"

    #======create sampling data for box plot=====
    #set reviewed contract TFC projection to 1
    df['tfcProjection']=df.apply(lambda x: 1.0 if x['reviewed']=="1" else x['tfcConfidence'], axis=1)
    #all to be reviewed are TFC true - everything else has their TFC_Projection value
    df['tfcAllTrue'] = df.apply(lambda x: x['tfcProjection'] if x['TFC'] == "Y" and ( float(x['revenue']) >= sliderRev[1] or float(x['revenue'] <= sliderRev[0]) or  float(x['tfcProjection']) >= sliderVal[1] or float(x['tfcProjection']) <= sliderVal[0]) else 1.0, axis=1)
    # all to be reviewed are TFC true - everything else has their TFC_Projection value
    df['tfcAllFalse'] = df.apply(lambda x: x['tfcProjection'] if x['TFC'] == "Y" and ( float(x['revenue']) >= sliderRev[1] or float(x['revenue'] <= sliderRev[0]) or  float(x['tfcProjection']) >= sliderVal[1] or float(x['tfcProjection']) <= sliderVal[0]) else 0.0, axis=1)

    #original data
    origData=samplingData(df,df['tfcProjection'])
    #new data
    newDataSampled=samplingData(df,df['tfcProjection'])
    #all true data
    allTrueSampled=samplingData(df,df['tfcAllTrue'])
    allFalseSampled=samplingData(df,df['tfcAllFalse'])

    # ====display quantities for total, reviewed, not reviewed=====
    dfTotalToReview= df[ (df['tfcConfidence']>= sliderVal[0]) & (df['tfcConfidence']<= sliderVal[1])]
    dfTotalToReview= dfTotalToReview[ (dfTotalToReview['revenue']>= sliderRev[0]) & (dfTotalToReview['revenue']<= sliderRev[1])]
    print("size df review is ", dfTotalToReview.shape[0])
    dfTotalToReview['tfcProjection']=dfTotalToReview.apply(lambda x: 1.0 if x['reviewed']=="1" else x['tfcConfidence'], axis=1)
    if dfTotalToReview.empty:
        numReviews=0
    else:
        numReviews=dfTotalToReview.shape[0]
    reviewTitle="{}".format(int(numReviews))

    #num Reviewed
    dfReviewed= dfTotalToReview[dfTotalToReview['reviewed']=="1"]
    if dfReviewed.empty:
        numReviewed=0
    else:
        numReviewed=dfReviewed.shape[0]
    numReviewedText="{} reviewed".format(int(numReviewed))

    dfNotReviewed= dfTotalToReview[dfTotalToReview['reviewed']=="0"]
    if dfNotReviewed.empty:
        numNotReviewed=0
    else:
        numNotReviewed=dfNotReviewed.shape[0]
    numNotReviewedText="{} not reviewed".format(int(numNotReviewed))

    print("num Reviewed is ",numReviewed)

    progressReviewed=(int(numReviewed)/(int(numNotReviewed)+int(numReviewed)))*100
    progressNotReviewed=(int(numNotReviewed)/(int(numNotReviewed)+int(numReviewed)))*100

    # print("num not reviewed is ",numNotReviewed)

    return (reviewGraphSlider(df,sliderVal[0],sliderVal[1],sliderRev[0],sliderRev[1],sliderVal[0],sliderVal[1],sliderRev[0],sliderRev[1],"param"),revPlot(dfTotalToReview,origData,origData,allTrueSampled,allFalseSampled) ,reviewTitle, numReviewedText, numNotReviewedText,progressReviewed,progressNotReviewed)

if __name__ == '__main__':
    app.run_server(debug=True)