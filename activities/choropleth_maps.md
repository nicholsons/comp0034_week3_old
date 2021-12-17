# Choropleth maps

## Introduction to choropleth maps with plotly express

Choropleth maps display divided geographical areas or regions that are coloured, shaded or patterned in relation to a
data variable. [Read the description of their use](https://datavizcatalogue.com/methods/choropleth.html) before moving
on to the next code cell.

The following example is copied from the [Plotly documentation](https://plotly.com/python/plotly-express/#maps).

You may also need to read:

- [Plotly express API documentation for choropleth_mapbox](https://plotly.com/python-api-reference/generated/plotly.express.choropleth_mapbox.html#plotly.express.choropleth_mapbox)
- [A definition of geojson](https://geojson.org)

The first example shows election data in Montreal.
Open [/examples/choropleth_election.py](../examples/choropleth_election.py) and run the code.

The second example shows the gapminder data.
Open [/examples/choropleth_gapminder.py](../examples/choropleth_gapminder.py) and run the code. This example also
applies a template called 'plotly_dark'.

## Create a choropleth map using England 2011 census data and local authority boundaries

### Data source

The census boundary data was downloaded
from [UK data service](https://census.ukdataservice.ac.uk/get-data/boundary-data.aspx)

You can also get geo boundary data from
the [office for national statistics (ONS)](https://geoportal.statistics.gov.uk/datasets/census-merged-local-authority-districts-december-2011-generalised-clipped-boundaries-in-great-britain)
.

The geodata was converted to geojson using an [online conversion tool](https://odileeds.github.io/CSV2GeoJSON/).

The 2011 census data was downloaded from [InFuse](https://infuse.ukdataservice.ac.uk).

## geojson data

In the previous examples we used default geo data using iso_alpha, for this example we only want UK local authorities
drawn with boundaries as at the 2011 census.

To do this we need to provide our own geojson.

Plotly expects the geojson to have an id field, however if you run the next cell you will see that our data is indexed
on LAD19CD.

You could rename the JSON so LAD19CD is renamed as 'id'. Note: when converting the data using the csv to geodata
converter there was also an option to change the field name.

Plotly allows you to use a different name for the id field, however if you do that then you have to have a column of the
same name in your dataframe. This is the approach taken in the code
in [/examples/choropleth_england_la_geojson.py](../examples/choropleth_england_la_geojson.py), where the index of the
age dataframe is set to LAD19CD.

Run the code in [/examples/choropleth_england_la_geojson.py](../examples/choropleth_england_la_geojson.py)

## Challenge 1: Create your own choropleth map

Try to create a choropleth map for another area, e.g. Wales, showing under 5's in the 2011 census. You will need to
download and format the data as well as creating the map.

If you don't want to download data then try a different area of England which should be in the `la_age_data.csv` file.

## Challenge 2: Create a plotly Dash app containing the choropleth maps

Use one or more of the choropleth maps in the examples, or one you created.

Create a new Dash app.

Display the maps in the Dash app.