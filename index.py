#%%
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

# Connect to main app.py file
from app import app
from app import server

# Connect to your app pages
from apps import datatable2, datatable12,datatable11, datatable3

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div([
        dbc.Col([
        dcc.Link(html.Button('Bölgesel İlçe Verileri (Karşılastırmalı)'), href='/apps/datatable2',
        # target='_blank'
        ),
        ],
           xs=12, sm=12, md=12, lg=3, xl=3,
        ),
        # html.Br(),
        dbc.Col([
        dcc.Link(html.Button('Ulusal İlçe Verileri-Grafik Gösterimi'), href='/apps/datatable12',),
        ],
           xs=12, sm=12, md=12, lg=3, xl=3,
        ),
        # html.Br(),
        dbc.Col([
        dcc.Link(html.Button('Ulusal İlçe Verileri-İki Farklı Veriye göre Saçılım Grafiği'), href='/apps/datatable3',
        ),
        ],
           xs=12, sm=12, md=12, lg=3, xl=3,
        ),
        dbc.Col([
        dcc.Link(html.Button('Ulusal İlçe Verileri-Harita Gösterimi'), href='/apps/datatable11',),
        ],
           xs=12, sm=12, md=12, lg=3, xl=3,
        ),
        html.Br(),
        html.Hr(),
    ], className="row text-start font-weight-bold mt-3 ml-2"),
    html.Div(id='page-content',
        children=[],
    )
],
        style={
            # "position": "fixed",
            #  "z-index": "999",
            #  "background": "#F0F8FF",
            #  "width": "100%",
                },
)

# app.validation_layout = html.Div([app.layout,datatable.layout, datatablee.layout])

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/datatable2':
        return datatable2.layout
    elif pathname == '/apps/datatable12':
        return datatable12.layout
    elif pathname == '/apps/datatable3':
        return datatable3.layout
    elif pathname == '/apps/datatable11':
        return datatable11.layout
    else:
        return html.Br(),html.Hr(),"*** Lütfen Yukarıdan Bir Seçenek Seçiniz ***",html.Br(),html.Br(),"*** Daha Hızlı Çalışmak için Sayfaları Farklı Sekmelerde Açabilirsiniz ***"


if __name__ == '__main__':
    app.run_server(debug=False)

# %%