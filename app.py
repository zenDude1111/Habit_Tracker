# Import necessary libraries
import dash
from dash import html, dcc, Input, Output
import dash_bootstrap_components as dbc

# Import pages
from pages import page_one

# Initialize the Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.FLATLY])
app.title = 'Multi-Page Dash App'

# Define the layout of the app
app.layout = dbc.Container([
    dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Home", href="/")),
            dbc.NavItem(dbc.NavLink("Page One", href="/page-one")),
            # Add more NavItem components here for additional pages
        ],
        brand="Demo Multi-Page App",
        brand_href="/",
        color="primary",
        dark=True,
        fluid=True,
    ),
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
], fluid=True)

# Define callback for multi-page setup
@app.callback(
    Output('page-content', 'children'),
    Input('url', 'pathname')
)
def display_page(pathname):
    if pathname == '/page-one':
        return page_one.layout
    else:
        # This is the default main page content
        return dbc.Container([
            dbc.Row([
                dbc.Col(html.H1('Welcome to the Main Page', className='text-center'), width=12),
                dbc.Col(html.P("This is the default view when no specific paths are matched.", className="text-center")),
                dbc.Col(html.P("Navigate to 'Page One' to see more detailed content.", className="text-center")),
            ], align="center", className='mt-5')
        ], fluid=True, className='py-3')

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
