from pathlib import Path

import dash
from dash import html
from dash import dcc
import prepare_data


app = dash.Dash(__name__)

app.layout = html.Div(children=[

    html.H1('Lollapalooza experience'),

])

if __name__ == '__main__':
    app.run_server(debug=True)
