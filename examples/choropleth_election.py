import plotly.express as px

if __name__ == '__main__':
    # Create a variable that contains the data using the election dataset provided by PlotlyExpress
    df = px.data.election()

    # Create a variable that contains the geojson data for the election dataset
    geojson = px.data.election_geojson()

    # Create a choropleth mapbox using plotly express
    fig = px.choropleth_mapbox(df,
                               geojson=geojson,
                               color="Bergeron",
                               locations="district",
                               featureidkey="properties.district",
                               center={"lat": 45.5517, "lon": -73.7073},
                               mapbox_style="carto-positron",
                               zoom=9)
    fig.show()
