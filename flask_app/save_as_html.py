"""
Creates the choropleth maps from activity 2.10 and saves to HTML file in the current working directory.
You will then need to move the files into the templates directory
You can run this file as a standalone python file if you are not using the Flask app
You do not need to use this if you run the Flask app and access the home page
The flask app generates the charts when the home page is accessed.
"""

import os
from os.path import join

import plotly.express as px

# Get the current working directory
currentDirectory = os.getcwd()


def save_as_html():
    """ Creates the choropleth maps from activity 2.10 and saves to HTML file in the current folder"""
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
    fig1.write_html("election.html")

    gapminder = px.data.gapminder()
    fig2 = px.choropleth(gapminder,
                         locations="iso_alpha",
                         color="lifeExp",
                         hover_name="country",
                         animation_frame="year",
                         color_continuous_scale='Plasma',
                         height=600
                         )
    fig2.write_html("gapminder.html")

    print('Files saved to ', currentDirectory)


if __name__ == '__main__':
    save_as_html()
