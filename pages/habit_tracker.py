from dash import html, dcc
import dash_bootstrap_components as dbc

# Layout
layout = html.Div([
    html.H2("Track Habits", className="mb-4"),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4("Nicotine Use", className="card-title"),
                    dbc.Button("ZYN 3mg", color="primary", outline=True, className="mt-2", id="log-3mgzyn-button"),
                ])
            ], className="mb-3"),
        ], width=12, lg=6),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4("Cannabis Vape", className="card-title"),
                    dbc.Input(id="CannabisVape-input", placeholder="Enter Amount", type="number"),
                    dbc.Button("Submit", color="primary", className="mt-3", id="log-cannabisvape-button"),
                ])
            ], className="mb-3"),
        ], width=12, lg=6),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4("Work Habits", className="card-title"),
                    dbc.Label("Enter Hours Worked"),
                    dbc.Input(id="WorkHours-input", placeholder="Enter Hours Worked", type="number"),
                    dbc.Button("Submit", color="primary", className="mt-3", id="log-hoursworked-button"),
                ])
            ], className="mb-3"),
        ], width=12, lg=6),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4("Health Events", className="card-title"),
                    dbc.Label("Migraine Event"),
                    dbc.RadioItems(
                        options=[
                            {"label": "Right", "value": "Right"},
                            {"label": "Left", "value": "Left"},
                        ],
                        value=None,
                        id="MigraineEvent-input",
                        inline=True
                    ),
                    dcc.DatePickerSingle(id="MigraineDate-input", placeholder="Datetime of Onset"),
                    dbc.Button("Submit", color="primary", className="mt-3", id="log-migrain-button"),
                ])
            ], className="mb-3"),
        ], width=12, lg=6),
    ])
])