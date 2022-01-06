from pathlib import Path

import dash
from dash import html
from dash import dcc
import dash_bootstrap_components as dbc

DATA_PATH = Path(__file__).parent.joinpath('data')

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SKETCHY])

app.layout = dbc.Container(
    [
        html.H1("Paralympic Medals Dashboard"),

    ],
    fluid=True,
)

if __name__ == '__main__':
    app.run_server(debug=True, port=8888)
