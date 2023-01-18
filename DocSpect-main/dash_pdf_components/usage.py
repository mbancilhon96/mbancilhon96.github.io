import dash_pdf_components
import dash
from dash import dcc
from dash import html, Input, Output, callback_context
from dash import html
import dash_bootstrap_components as dbc
import json

app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    external_scripts=['https://documentcloud.adobe.com/view-sdk/viewer.js']
)
app.title = "Dash PDF Reader"

CONCORD_LOGO = app.get_asset_url("images/concord-logo-dark.png")
API_KEY = '899d52477b7d4b589f808242e8d36cc3' #This client ID only works for localhost

def load_annotations(json_file_path):
    ### read Json file
    # json_file_path = "assets/highlights.json"
    # json_file_path = "assets/highlightsTest.json"
    # arr = []
    # with open(json_file_path, 'r') as json_file:
    #     arr.append(json.loads(json_file.read()))
    # print(arr)

    ### read jsonlines
    # json_file_path = "assets/pdfembed_highlight.jsonlines" 
    arr = []
    with open(json_file_path, 'r') as file:
        for line in file:
            arr.append(json.loads(line))
    print(len(arr))

    return arr

doc_test = {
    "fileName": "Demo PDF.pdf",
    "fileUrl": "https://documentcloud.adobe.com/view-sdk-demo/PDFs/Bodea Brochure.pdf",
    "fileId": '0d07d124-ac85-43b3-a867-36930f502ac6',
    "highlightsArr": []
}
doc1 = {
    "fileName": "Cleaning Services Agreement.pdf",
    "fileUrl": "https://dl.dropboxusercontent.com/s/zgjf3rg3gi9rylr/Control_Service-A_Cleaning.pdf",
    "fileId": '0d07d124-ac85-43b3-a867-36930f502ac6',
    "highlightsArr": []
}
# html.Img(src=app.get_asset_url('my-image.png'))
doc2 = {
    "fileName": "Electrical Services Agreement.pdf",
    "fileUrl": "https://dl.dropboxusercontent.com/s/5ui4jwcvfitbscu/Control_Service-B_Electrical.pdf",
    "fileId": '0d07d124-ac85-43b3-a867-36930f502ac6',
    "highlightsArr": []
    # "highlightsArr": load_annotations("assets/DeltathreeInc_19991102_S-1A_EX-10.19_6227850_EX-10.19_Co-Branding Agreement_ Service Agreement_annotated_highlights.jsonlines")
}

doc3_annotations = load_annotations("assets/pdfembed_highlight.jsonlines")
# doc3_annotations = load_annotations("assets/highlightsTest/e3e17df0-d44e-4688-b3b1-5857aefd9d6c_annotated_highlights.jsonlines")
doc3 = {
    "fileName": "Supply Agreement.pdf",
    # "fileUrl": "https://dl.dropboxusercontent.com/s/us5molx0nglmjsi/Reynolds.pdf",
    "fileUrl": "assets/files/Reynolds.pdf",
    # "fileUrl": "assets/files/highlightsTest/e3e17df0-d44e-4688-b3b1-5857aefd9d6c.pdf",
    # "fileUrl": "assets/files/electricalsigned2.pdf", #protected and signed doc sample
    "fileId": '0d07d124-ac85-43b3-a867-36930f502ac6',
    "highlightsArr": doc3_annotations
}

doc4 = {
    "fileName": "Delta Services Agreement.pdf",
    # "fileUrl": "assets/DeltathreeInc.pdf",
    "fileUrl": "assets/files/Reynolds.pdf",
    "fileId": '0d07d124-ac85-43b3-a867-36930f502ac6',
    "highlightsArr": load_annotations("assets/DeltathreeInc_highlights.jsonlines")
}

doc1_btn = dbc.Button(
            "Load Cleaning Services Agreement", 
            color="primary", 
            className="me-1",
            id="btn-load-doc1",
            n_clicks = 0
        )

doc2_btn = dbc.Button(
            "Load Electrical Services Agreement", 
            color="primary", 
            className="me-1",
            id="btn-load-doc2",
            n_clicks = 0
        )

doc3_btn = dbc.Button(
            "Load Supply Agreement", 
            color="primary", 
            className="me-1",
            id="btn-load-doc3",
            n_clicks = 0
        )

doc4_btn = dbc.Button(
            "Load Delta Service Agreement", 
            color="primary", 
            className="me-1",
            id="btn-load-doc4",
            n_clicks = 0
        )

open_file_btns = dbc.ButtonGroup(
    [doc1_btn, doc2_btn, doc3_btn, doc4_btn],
    className = "btn-load"
)

pdf_viewer = dbc.Col(
    [    
        dash_pdf_components.DashPdfComponents(
            key = doc1["fileUrl"],
            id = 'pdf-view',
            label = 'pdf-view-label',
            apiKey = API_KEY, 
            fileUrl = doc1["fileUrl"],
            fileName = doc1["fileName"],
            fileId = doc1["fileId"],
            highlightsArr = []
            # highlightsArr = doc3["highlightsArr"]
        )
    ], 
    width=9,
)

@app.callback(
    Output('pdf-view', component_property='key'), 
    Output('pdf-view', component_property='fileUrl'), 
    Output('pdf-view', component_property='fileName'), 
    Output('pdf-view', component_property='highlightsArr'), 
    Input('btn-load-doc1', 'n_clicks'),
    Input('btn-load-doc2', 'n_clicks'),
    Input('btn-load-doc3', 'n_clicks'),
    Input('btn-load-doc4', 'n_clicks')
)
def update_file1(btn1, btn2, btn3, btn4):
    changed_id = [p['prop_id'] for p in callback_context.triggered][0]
    # url = doc1["fileUrl"]
    # name = doc1["fileName"]
    # arr = []
    url = doc1["fileUrl"]
    name = doc1["fileName"]
    arr = doc1["highlightsArr"]
    if 'btn-load-doc2' in changed_id:
        url = doc2["fileUrl"]
        name = doc2["fileName"]
    elif 'btn-load-doc3' in changed_id:
        url = doc3["fileUrl"]
        name = doc3["fileName"]
        arr = doc3["highlightsArr"]
    elif 'btn-load-doc4' in changed_id:
        url = doc4["fileUrl"]
        name = doc4["fileName"]
        arr = doc4["highlightsArr"]
    print(name)
    key = url
    return [key, url, name, arr]

navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(html.Img(src=CONCORD_LOGO, height="30px"), id="col-logo"),
                        # dbc.Col(dbc.NavbarBrand("", className="ms-2")),
                    ],
                    align="center",
                    className="navbar-logo-row",
                ),
                href="#"
            )
        ],
        id="navbar-container"
    ),
    color="dark",
    dark=True,
)

app.layout = html.Div([
    html.Div(
        [
            dbc.Row(navbar),
            dbc.Row(open_file_btns),
            dbc.Row(
                pdf_viewer
            ),
        ]
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
