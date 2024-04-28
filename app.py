from flask import Flask
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
import dash
import dash_bootstrap_components as dbc
from dash import html, dcc, Input, Output, State, callback_context

# Import the page layouts
from pages.habit_tracker import layout as page_one


# Initialize the Flask server
server = Flask(__name__)
server.secret_key = 'your_secret_key'  # Change this for production

# Configure Flask-Login
login_manager = LoginManager()
login_manager.init_app(server)
login_manager.login_view = '/'

# User class
class User(UserMixin):
    # Hardcoded user credentials
    user_database = {
        "admin": ("admin", "adminpassword")
    }

    def __init__(self, username):
        self.id = username

    @classmethod
    def get(cls, id):
        if id in cls.user_database:
            return cls(id)
        return None

# User loader for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

# Initialize the Dash app with exceptions suppressed
app = dash.Dash(__name__, server=server, external_stylesheets=[dbc.themes.DARKLY, dbc.icons.FONT_AWESOME], suppress_callback_exceptions=True)

# Define the layout of the app
app.layout = dbc.Container([
    dbc.NavbarSimple(
        children=[
            dbc.DropdownMenu(
                children=[
                    dbc.DropdownMenuItem("Home", href="/"),
                    dbc.DropdownMenuItem("Another Page", href="/another-page"),
                ],
                nav=True,
                in_navbar=True,
                label="Navigate",
            ),
            dbc.NavItem(dbc.NavLink("Logout", href="/logout")),
        ],
        brand="Habit Tracker",
        brand_href="/",
        color="secondary",
        dark=True,
        fluid=True,
    ),
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content', children=[])
], fluid=True)

@app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname')]
)
def display_page(pathname):
    if pathname == '/page-one':
        if current_user.is_authenticated:
            return page_one
        else:
            return login_page
    elif pathname == '/logout':
        logout_user()
        return login_page
    else:
        return login_page

login_page = dbc.Container(
    [
        html.H1("Please log in to continue", className="text-center"),
        dcc.Location(id='redirect', refresh=True),
        dbc.Input(id="username", placeholder="Username", type="text", style={"marginBottom": "5px"}),
        dbc.Input(id="password", placeholder="Password", type="password"),
        dbc.Button("Login", id="login-button", n_clicks=0),
        html.Div(id="login-status")
    ],
    className="py-3",
    fluid=True,
    style={"maxWidth": "500px"}
)

@app.callback(
    [Output('redirect', 'pathname'), Output('login-status', 'children')],
    [Input('login-button', 'n_clicks')],
    [State('username', 'value'), State('password', 'value')],
    prevent_initial_call=True
)
def login(n_clicks, username, password):
    if n_clicks > 0:
        user = User.get(username)
        if user and user.user_database[username][1] == password:
            login_user(user)
            return '/page-one', ""  # Redirect to Page One on successful login and clear any status messages
        else:
            return '/', "Invalid credentials"  # Stay on the login page and show an error message
    return '/', ""  # Default return on initial call or no action


if __name__ == '__main__':
    app.run_server(debug=True)
