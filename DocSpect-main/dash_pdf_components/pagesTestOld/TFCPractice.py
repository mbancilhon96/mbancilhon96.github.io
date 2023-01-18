import dash
from dash import html, dcc, Input, Output, State, callback
import dash_bootstrap_components as dbc

dash.register_page(__name__, path='/TFCPractice')

layout = html.Div(children=[
    html.H1(children='Practice: Termination for Convenience'),
    # false
    # html.Div(children=
    #     '''Now that you better understand what a Termination for Convenience is, let's practice. Read each of the clauses below and indicate whether it is a T for C clause or not.
    #    '''),
    # html.Br(),
    # # false
    # html.Div(children=
    #          '''"The Manufacturer hereby appoints the Customer to be the sole and exclusive agent for the promotion, sales, marketing, distribution and administration of the products listed in schedule A of this agreement based on minimum annual product purchase requirements as listed in Schedule B of this agreement.'"'''),
    # dbc.Button("T for C",color="primary", className="me-2",style={"width":"80px"}),
    # dbc.Button("Other",color="primary", className="me-2",style={"width":"80px"}),
    # html.Br(),
    # html.Br(),
    # true
    html.Header("Read each sentence carefully and indicate whether it is a Termination for Convenience clause or another type of clause. Please answer all four questions to access the next step."
                " Click on the button below if you need to review T for C definition and examples"),
    dbc.Button("Help", id="modalOpen", color="secondary", className="me-2", style={"width": "80px"}),
    dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle("Termination for Convenience : Definition and Examples")),
                dbc.ModalBody(
                    html.Div([
                        html.Div(children=
                                 '''In agreements, Termination for Convenience (T for C) clauses are intended to provide the agreeing party with the option to terminate the contract without any just cause. While Termination for Convenience provides both parties the freedom to exit the arrangement at any point in time without breaching the contract, it creates revenue uncertainty whenever payments are involved.
                                '''),
                        html.Br(),
                        html.Div(children=
                                 ''' To familiarize yourself with T for C clauses, please read the following examples. On the next page, you will be tested on T for C.'''),
                        html.Br(),
                        html.Div(children='''Termination for Convenience Clauses''', style={'font-weight': 'bold'}),
                        html.Br(),
                        html.Div(
                            children='''"Notwithstanding any other provision of this Agreement, [company name] may terminate this Agreement, at any time, upon sixty (60) days' prior written notice to Licensor."'''),
                        html.Br(),
                        html.Div(
                            children='''"This Agreement may be terminated by either party for any reason or no reason, whether or not extended beyond the initial term, by giving the other party written notice ninety (90) days in advance."'''),
                        html.Br(),
                        html.Div(children='''NOT Termination for Convenience Clauses''', style={'font-weight': 'bold'}),
                        html.Br(),
                        html.Div(
                            children='''"This Agreement may be terminated by either party at the expiration of its term or any renewal term upon thirty (30) days written notice to the other party."'''),
                        html.Br(),
                        html.Div(
                            children='''"...[company name] agrees that for a period of ninety (90) days prior to the expiration of the Term (unless the Agreement is terminated by Wade as permitted hereunder), [company name] shall have the exclusive right to negotiate for continued endorsement by Athlete of the [company name] Products.'"'''),
                        html.Br(),
                        html.Div(
                            children='''"Thereafter, this Agreement shall automatically continue in effect until either party gives the other at least six (6) months prior written notice of termination."'''),
                        html.Br()
                    ])
                ),
                dbc.ModalFooter( dbc.Button(
                                                "Close", id="modalClose", className="ms-auto", n_clicks=0
                                            )),
            ],
            id="TFCDefinitionModal",
            is_open=False,
        ),
    html.Br(),
    html.Br(),
    html.Div(children=[
                 html.Header("Q1: ",style={"font-weight":"bold"}),
                 html.Header(" Client has the unilateral right to cancel this agreement at any time within a 7-day notice period.",style={"margin-left": "10px"})
    ],style={"display":"flex"}),
    dbc.Button("T for C",id="q1Yes", color="primary", className="me-2", style={"width": "80px"}),
    dbc.Button("Other", id="q1No",color="primary", className="me-2", style={"width": "80px"}),
    html.Span(id="q1Answer", style={"verticalAlign": "middle"}),
    html.Br(),
    html.Br(),
    # false

    html.Div(children=[
        html.Header("Q2: ", style={"font-weight": "bold"}),
        html.Header(
            "The Term shall automatically renew thereafter for successive 5-year terms unless either party provides prior written notice of termination not less than 90 days prior to the end of such five-year term.",style={"margin-left": "10px"})
    ], style={"display": "flex"}),
    dbc.Button("T for C", id="q2Yes",color="primary", className="me-2", style={"width": "80px"}),
    dbc.Button("Other",  id="q2No",color="primary", className="me-2", style={"width": "80px"}),
    html.Span(id="q2Answer", style={"verticalAlign": "middle"}),
    html.Br(),
    #false

    html.Br(),
    html.Div(children=[
        html.Header("Q3: ", style={"font-weight": "bold"}),
        html.Header(
             "In the event that Distributor terminates this Agreement pursuant to either Section 7.2 or 7.3 above, Distributor will notify Subscribers that the Programming is no longer available."
            , style={"margin-left": "10px"})
    ], style={"display": "flex"}),
    dbc.Button("T for C",  id="q3Yes",color="primary", className="me-2", style={"width": "80px"}),
    dbc.Button("Other",  id="q3No",color="primary", className="me-2", style={"width": "80px"}),
    html.Span(id="q3Answer", style={"verticalAlign": "middle"}),
    html.Br(),
    html.Br(),
    # true

    html.Div(children=[
        html.Header("Q4: ", style={"font-weight": "bold"}),
        html.Header(
            "Either party may cancel this Agreement at any time, with or without supplying a reason, through written notification or by making suitable settings in the respective Control Panel",
           style={"margin-left": "10px"})
    ], style={"display": "flex"}),
    dbc.Button("T for C",  id="q4Yes",color="primary", className="me-2", style={"width": "80px"}),
    dbc.Button("Other",  id="q4No",color="primary", className="me-2", style={"width": "80px"}),
    html.Span(id="q4Answer", style={"verticalAlign": "middle"}),
    html.Br(),
    html.Br(),
    # html.Div(children=
    #          '''"Any Participant will have the right to voluntarily withdraw from the Joint Venture at any time"'''),
    # dbc.Button("T for C", color="primary", className="me-2", style={"width": "80px"}),
    # dbc.Button("Other", color="primary", className="me-2", style={"width": "80px"}),
    # html.Br(),
    # html.Br(),
    
    html.H1(children='Score: 0/4',id="TFCScore"),
    html.Br(),
    html.Div(children=[
        html.A(dbc.Button("Next",id="nextBtn",style={"display":"none"}), href='\docSpectInstructions1'),
    ],style={"display":"flex"}),
    html.Br(),

],style={'margin-left':'150px','margin-right':'150px','margin-top':'50px'})

@callback(Output('TFCDefinitionModal', 'is_open'),
    [Input('modalOpen', 'n_clicks'),Input("modalClose", "n_clicks")],
    [State("TFCDefinitionModal", "is_open")])
def showStatsModal(modalOpen,modalClose,is_open):
        if modalClose or modalOpen:
            return not is_open
        return is_open

@callback([Output('q1Answer', 'children'),
          Output('q2Answer', 'children'),
          Output('q3Answer', 'children'),
          Output('q4Answer', 'children'),
          Output('q1Yes', 'disabled'), Output('q1No', 'disabled'),
           Output('q2Yes', 'disabled'), Output('q2No', 'disabled'),
           Output('q3Yes', 'disabled'), Output('q3No', 'disabled'),
           Output('q4Yes', 'disabled'), Output('q4No', 'disabled'),
           Output('TFCScore', 'children'),
           Output('nextBtn', 'style')],
        [Input('q1Yes', 'n_clicks'),Input("q1No", "n_clicks"),
         Input('q2Yes', 'n_clicks'),Input("q2No", "n_clicks"),
         Input('q3Yes', 'n_clicks'),Input("q3No", "n_clicks"),
         Input('q4Yes', 'n_clicks'),Input("q4No", "n_clicks")])

def showAnswers(q1Yes, q1No, q2Yes, q2No, q3Yes, q3No,q4Yes, q4No):
        q1ans =""
        q2ans =""
        q3ans =""
        q4ans =""
        q1YesDisabled=False
        q1NoDisabled=False
        q2YesDisabled = False
        q2NoDisabled = False
        q3YesDisabled = False
        q3NoDisabled = False
        q4YesDisabled = False
        q4NoDisabled = False
        nextBtnDisplay = "none"
        score=0

        # which btn was clicked
        if q1Yes is not None:
            q1ans= "Correct. This clause is a T for C clause. "
            q1YesDisabled= True
            q1NoDisabledDisabled= True
            score+=1
        elif q1No is not None:
            q1ans= "Incorrect. This clause is a T for C clause."
            q1YesDisabled = True
            q1NoDisabled = True

        if q2Yes is not None:
            q2ans= "Incorrect. Even though it contains the word 'termination', this is a renewal clause and not a T for C. "
            q2YesDisabled = True
            q2NoDisabled = True
        elif q2No is not None:
            q2ans= "Correct. This is not a T for C clause. "
            q2YesDisabled = True
            q2NoDisabled = True
            score+=1

        if q3Yes is not None:
            q3ans= "Incorrect. Even though it contains the word 'termination', this is a post termination service clause and not a T for C. "
            q3YesDisabled = True
            q3NoDisabled = True
        elif q3No is not None:
            q3ans= "Correct. This is not a T for C clause. "
            q3YesDisabled = True
            q3NoDisabled = True
            score+=1

        if q4Yes is not None:
            q4ans= "Correct. This clause is a T for C clause. "
            q4YesDisabled = True
            q4NoDisabled = True
            score+=1

        elif q4No is not None:
            q4ans= "Incorrect. This clause is a T for C clause. "
            q4YesDisabled = True
            q4NoDisabled = True

        if q1ans and q2ans and q3ans and q4ans != "":
            nextBtnDisplay= "block"

        return (q1ans, q2ans, q3ans,q4ans,q1YesDisabled,q1NoDisabled,q2YesDisabled ,q2NoDisabled,q3YesDisabled,q3NoDisabled,q4YesDisabled,q4NoDisabled, "Score: "+str(score)+"/4",{'display': nextBtnDisplay})




