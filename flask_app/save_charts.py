"""
Creates the choropleth maps from activity 2 and saves to HTML files in the `flask_app/static/charts' directory.
You can run this file as a standalone python file.
"""

import os
import matplotlib.pyplot as plt

import plotly.express as px


def save_plt_as_png(plt, chart_name):
    """ Takes a matplotlip plot and a name and saves as png"""
    file_name = chart_name + ".png"
    file_loc = os.path.join(os.getcwd(), "static/charts", file_name)
    try:
        plt.savefig(file_loc, format='png')
        print("Filename saved as {}".format(file_loc))
    except OSError as err:
        print("OS error: {0}".format(err))


def save_px_as_html(px_figure, chart_name):
    """ Takes a plotly express chart and saves as html"""
    file_name = chart_name + ".html"
    file_loc = os.path.join(os.getcwd(), "static/charts", file_name)
    try:
        px_figure.write_html(file_loc)
        print("Filename saved as {}".format(file_loc))
    except OSError as err:
        print("OS error: {0}".format(err))


def create_election_chart():
    df = px.data.election()
    geojson = px.data.election_geojson()
    fig = px.choropleth_mapbox(df,
                               geojson=geojson,
                               color="Bergeron",
                               locations="district",
                               featureidkey="properties.district",
                               center={"lat": 45.5517, "lon": -73.7073},
                               mapbox_style="carto-positron",
                               zoom=9)
    return fig


def create_gapminder_chart():
    gapminder = px.data.gapminder()
    fig = px.choropleth(gapminder,
                        locations="iso_alpha",
                        color="lifeExp",
                        hover_name="country",
                        animation_frame="year",
                        color_continuous_scale='Plasma',
                        height=600
                        )
    return fig


def create_line_chart():
    data = [1, 2, 3, 4]

    fig, axes = plt.subplots(figsize=(12, 6))

    axes.plot(data)
    axes.set_xlabel('x-axis label')
    axes.set_ylabel('y-axis label')
    axes.set_title('This is a title')
    return fig


if __name__ == '__main__':
    election = create_election_chart()
    gapminder = create_gapminder_chart()
    plot = create_line_chart()
    save_px_as_html(election, 'election_choropleth')
    save_px_as_html(gapminder, 'gapminder_choropleth')
    save_plt_as_png(plot, 'plot_line')
