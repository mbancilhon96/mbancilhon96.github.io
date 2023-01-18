import os
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
import dash_daq as daq
import numpy as np
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
import dash_bootstrap_components as dbc
# import dash_extensions
# import dash_defer_js_import as dji

app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    # external_scripts=['https://documentcloud.adobe.com/view-sdk/main.js']
    external_scripts=['https://documentservices.adobe.com/view-sdk/viewer.js']
    # assets_ignore='embed.js'
    
)

CONCORD_LOGO = app.get_asset_url("images/concord-logo-dark.png")

navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(html.Img(src=CONCORD_LOGO, height="30px"),
                                id="col-logo"),
                        # dbc.Col(dbc.NavbarBrand("", className="ms-2")),
                    ],
                    align="center",
                    className="navbar-logo-row",
                ),
                href="#"
            ),
            # dbc.NavItem(dbc.NavLink("Scroll to Top", href="javascript:scrollToTop()")),
            # dbc.NavItem(dbc.NavLink("Page 1", href="#"))
        ],
        id="navbar-container"
    ),
    color="dark",
    dark=True,
)

pdf_viewer = dbc.Col(
    html.Div(id='pdf-viewer'), 
    width=9,
    id='pdf-viewer-col',
)

accordion = html.Div(
    dbc.Accordion(
        [
            dbc.AccordionItem(
                [
                    html.P("Section 1"),

                    dbc.Button("Load PDF", 
                    id="loadBtn",
                    size="lg"), 

                    dbc.Button("Scroll to Top", 
                    # onClick = "scrollToTop()",
                    id="scrollTopBtn",
                    # href="javascript:scrollToTop()",
                    size="lg"), 
                ],
                title="Item 1"
                # id="scrollTopBtn"
            ),
            dbc.AccordionItem(
                "Section 2",
                title="Item 2",
            ),
        ],
    )
)

insights_panel = dbc.Col(
    # html.Div("Panel"), 
    accordion, width=3,
    id='insights-panel'
)

row = html.Div(
    [
        dbc.Row(
            [ pdf_viewer, insights_panel ]
        ),
    ]
)
testRecord =  {
  "userID": "thirdTest",
  "timeRemaining": "thirdTest",
  "estimateInput": "thirdTest",
  "confidenceInput": "thirdTest",
  "contractsOpened": "thirdTest",
  "contractsReviewed": "thirdTest"
}

app.layout = html.Div([
    dcc.Store(id="appDataStore",data=testRecord),
    dcc.Location(id="url"), 
    navbar, 
    row
])


if __name__ == "__main__":
    app.run_server(debug=True, port="8060")
