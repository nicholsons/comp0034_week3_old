import os

import plotly.express as px
from flask import Flask, render_template, url_for

app = Flask(__name__)
app.debug = True


@app.route('/')
def index():
    # Creates the charts and saves them as HTML files in the templates folder
    create_charts()
    return render_template('index.html')


@app.route('/gapminder')
def gapminder():
    return render_template('gapminder.html')


@app.route('/election')
def election():
    return render_template('election.html')


def create_charts():
    df = px.data.election()
    geojson = px.data.election_geojson()
    fig1 = px.choropleth_mapbox(df,
                                geojson=geojson,
                                color="Bergeron",
                                locations="district",
                                featureidkey="properties.district",
                                center={"lat": 45.5517, "lon": -73.7073},
                                mapbox_style="carto-positron",
                                zoom=9)
    fig1.write_html(os.path.join(app.root_path, 'templates', 'election.html'))

    gapminder = px.data.gapminder()
    fig2 = px.choropleth(gapminder,
                         locations="iso_alpha",
                         color="lifeExp",
                         hover_name="country",
                         animation_frame="year",
                         color_continuous_scale='Plasma',
                         height=600
                         )
    fig2.write_html(os.path.join(app.root_path, 'templates', 'gapminder.html'))


if __name__ == '__main__':
    app.run()
