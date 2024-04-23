from dash import html, dcc
import dash_bootstrap_components as dbc

# Define the layout for this page
layout = dbc.Container([
    dbc.Row(dbc.Col(html.H1("Page One", className='text-center mb-4'))),
    dbc.Row([
        dbc.Col([
            html.H2("Welcome to Page One"),
            html.P("This is the content of page one. You can use Bootstrap components to style your app."),
            dcc.Graph(
                id='example-graph',
                figure={
                    'data': [
                        {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                        {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': 'Montreal'},
                    ],
                    'layout': {
                        'title': 'Dash Data Visualization'
                    }
                }
            )
        ], width=12)
    ])
], fluid=True)
