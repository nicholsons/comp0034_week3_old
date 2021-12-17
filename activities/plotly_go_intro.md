# Introduction to Plotly Go

# Overview of `plotly.graph_objects`

You have already seen how to use Plotly Express to build charts. Plotly Express is a module with Plotly.py and provides
a high level API for creating charts.

You may need to change features of a visualisation that are not exposed in Express, in which case you would need to use
Plotly.py graph objects instead. The following is a brief overview of using graph objects.

For most, Express will be sufficient for the coursework, so you may skip this activity if you find it confusing to learn
too many ways to create charts.

## Plotly.py overview

There are 3 main concepts in Plotly’s philosophy:

1. Data
2. Layout
3. Figure

### Data

The Data object defines what we want to display in the chart (that is, the data). We define a collection of data and the
specifications to display them as a trace. A Data object can have many traces. Think of a line chart with two lines
representing two different categories: each line is a trace.

### Layout

The Layout object defines features that are not related to data (like title, axis titles, and so on). We can also use
the Layout to add annotations and shapes to the chart.

### Figure

The Figure object creates the final object to be plotted. It's an object that contains both data and layout.

Plotly visualizations are built with plotly.js. This means that the Python API is just a package to interact with the
plotly.js library. The plotly.graph_objs module contains the functions that will generate graph objects for us.

### Example chart

In the following code you can see how the layout is updated

```python
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv(
    'https://raw.githubusercontent.com/plotly/datasets/718417069ead87650b90472464c7565dc8c2cb1c/coffee-flavors.csv')

fig = go.Figure()

fig.add_trace(go.Sunburst(
    ids=df.ids,
    labels=df.labels,
    parents=df.parents,
    domain=dict(column=1),
    maxdepth=2,
    insidetextorientation='radial'
))

fig.update_layout(
    margin=dict(t=10, l=10, r=10, b=10)
)

fig.show()
```

The code in [/examples/go.py](/examples/go.py) creates the above plot using code
from [Plotly.](https://plotly.com/python/sunburst-charts/#controlling-text-orientation-inside-sunburst-sectors)

### Further information

Please refer to the [Plotly Graph Objects documentation](https://plotly.com/python/graph-objects/).
[Examples](https://plotly.com/python/) for creating many different chart types in Plotly Express and Plotly Go.


## Adding plotly go charts to the Lollapalooza dashboard

This activity assumes you have already completed the 'Introduction to plotly express' activities as it continues the
Lollapalooza dashboard by addressing the final two questions:

- Where did she go during the festival?
- Which concerts did she watch?

## Add a map to answer 'Where did she go during the festival?'

"The data only tells us the name of the location where I made the purchase, and the festival took place at Autódromo de
Interlagos.

I took the map with the stages from here and used the georeferencer tool from georeference.com to get the latitude and
longitude coordinates for the stages.

We need to display a map and the markers for each purchase, so we will use Mapbox and the scattermapbox trace.

You will need to [generate a mapbox token from the mapbox site](https://www.mapbox.com/help/define-access-token/) and
then place your token in the first line of code after the import statements in the code below. You will need to create
an account to do this. If you don't feel comfortable in signing up then you can skip this chart."

```python
mapbox_token = ""  # Add your mapbox token here

df = pd.read_csv("../data/stages.csv")

trace = go.Scattermapbox(lat=df["latitude"], lon=df["longitude"], text=df["stage"], marker=go.Marker(size=10),
                         mode="markers+text", textposition="top left")

data = [trace]

layout = go.Layout(mapbox=dict(accesstoken=mapbox_token, center=dict(lat=-23.701057, lon=-46.6970635), zoom=14.5))

figure = go.Figure(data=data, layout=layout)

```

## Add a table to guess the concerts she attended based only on purchases

"Ideally, when we are watching a show, we are watching the show (and not buying stuff), so the purchases should be made
before or after each concert. I then made a list of each concert happening one hour before, one hour after, and
according to the time the purchase was made.

To find out which one of these shows I attended, I calculated the distance from the location of the purchase to each
stage. The shows I attended should be the ones with the shortest distance to the concessions.

As we want to show each data point, the best choice for a visualization is a table."

The data file is `data/concerts_I_attended.csv`

The code to prepare the data is in the function `prepare_data.prepare_concert_data(df)`

Add the code to create the figure using the data from the data file to `dash_app.py`.

```python
file_path_concert = Path(__file__).parent.joinpath('data', 'concerts_I_attended.csv')
df_table = pd.read_csv(file_path_concert)
df_table = prepare_data.prepare_concert_data(df_table)

trace_table = go.Table(header=dict(values=["Concert", "Date", "Correct?"], fill=dict(color=("rgb(82,187,47)"))),
                       cells=dict(values=[df_table.concert, df_table.date, df_table.correct],
                                  font=dict(color=([df_table.color]))))

data = [trace_table]
fig_table = go.Figure(data=data)
```

Write the code to create the table in the app layout.

Re-run the Dash app.

