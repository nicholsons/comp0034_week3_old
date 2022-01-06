# COMP0034 Lab 3 Activities

## Introduction

It is assumed that you have completed the activities designed to introduce you to Plotly Express and Plotly Go on
Moodle. If you have not completed these then you will need to do so before attempting this lab session.

This activity continues with the dataset created in COMP0035 related to paralympic events.

There is no defined target audience, however for the purpose of this activity try to decide on a target audience and
then design charts that will appeal to them, the following are some suggestions:

- 18 to 25-year-old university students interested in paralympics events. Assume they have limited knowledge of the
  paralympics however they make extensive use of a range of technologies and are capable of understanding more complex
  data and charts.
- 30 to 60-year-old para-sport volunteers and officials
- 11 to 16-year-olds who need to find out about the paralympics for a school project

The starter code and data for the activities are in the [/paralympic_app/](/paralympic_app) directory of the repository.

- `/paralympic_app/data/all_medals.csv` contains the medal table results from all paralympics.
- `/paralympic_app/data/paralympics.csv` contains data about the paralympic events such as dates, location, number of
  participants, events, countries and sports.

You are advised to work through the tasks sequentially as they increase in complexity and there is less guidance given
for the later tasks. This is a challenging lab; you are unlikely to complete all tasks within the 2 hours if you haven't
already had some practice at creating charts.

## Task 1: Create a line chart using Plotly Express

**Create one or more line charts using Plotly Express to answer all or part of the following question for your chosen
target audience:**

1. Has the number of athletes, nations, events and sports changed over time?

You could explore the above for either, or both, of the winter and summer events.

Use the Plotly documentation to help you:

- [Plotly Express line chart guide](https://plotly.com/python/line-charts/)
- [Styling figures with Plotly Express](https://plotly.com/python/styling-plotly-express/)

The line chart example in the Plotly documentation is given as:

```python
import plotly.express as px

df = px.data.gapminder().query("country=='Canada'")
fig = px.line(df, x="year", y="lifeExp", title='Life expectancy in Canada')
fig.show()
```

There is also an example in [/paralympic_app/create_charts.py](../paralympic_app/create_charts.py). To see this example
in Dash add the following code to the Dash app:

```python
# Add an import
import create_charts

# Before the app.layout section of the NOC_code add the code to create the figure variable
fig_line_sports = create_charts.line_chart_sports()

# Within the app.layout NOC_code add the following:
dcc.Graph(
    id='line-sports',
    figure=fig_line_sports
),
```

Steps:

1. In `paralympic_app.py` add the imports:
   ```python
    import pandas as pd
    import plotly.express as px
    import plotly.graph_objs as go
    from pathlib import Path
    ```
2. In `paralympic_app.py` before you create the Dash app object, write code that:
    1. Creates a dataframe variable with the data needed for the chart
    2. Creates a figure variable using the Plotly Express line chart function (`figure_name = px.line()`)
3. In `paralympic_app.py` in the `app.layout` code section add the figure as a dash core components
   graph (`dcc.Graph()`). Provide values for the `id` and `figure` parameters. The `id` isn't strictly necessary to
   display the chart now, however you will need it when we move on to adding interactivity next week so it is a good
   habit to create one. Remember that `id` must be unique on any given web page. The value for `figure` should be the
   variable that creates the line chart.
4. Run the Dash app.

Alternatively, you can add the code to prepare the data and create the chart to `create_charts.py` or another file and
then import the function to `paralympic_app.py`. This helps to keep the code in `paralympic_app.py` to create the Dash
app separate from the code to create the charts and might make the Dash app code file easier to read.

If you add the code to create the charts in the paralympic_app.py you will likely need the following imports:

### Styling

Once you have created the chart, try and make the styling appropriate for your target audience. Consider titles, labels,
colours, etc.

## Task 2: Create stacked bar using Plotly Express

**Create one or more stacked bar charts to show whether the ratio of male and female athletes has changed over time for
the winter and summer paralympics.**

1. Has the ratio of male and female athletes changed over time?

Steps:

1. Add the code to create the chart in paralympic_app.py before the Dash app is created.
    - You will need to these columns from the `paralympics.csv`
      file: `['TYPE', 'YEAR', 'LOCATION', 'MALE', 'FEMALE', 'PARTICIPANTS']`
    - Add two new columns that calculate the % of male and female participants e.g. Add new columns that each contain
      the result of calculating the % of male and female participants e.g.
      `df_events['M%'] = df_events['MALE'] / df_events['PARTICIPANTS']`
    - Sort the values by Type and Year ascending using the `df.sort_values()` function.
    - Create a new column that combines Location and Year to use as the x-axis e.g.
      `df_events['xlabel'] = df_events['LOCATION'] + ' ' + df_events['YEAR'].astype(str)`
    - Create the figure e.g. `fig = px.bar()`.
      See [Plotly documentation](https://plotly.com/python/bar-charts/#bar-chart-with-plotly-express). You can pass
      multiple columns to the `y=` parameter, e.g. `y=['M%', 'F%']`
2. Add a `dcc.Graph` element to the layout section of the code to display the chart you created.
3. Re-run the Dash app.
4. Style the chart.

Challenge: Create a different chart type for this question (i.e. not line or bar). See
the [list of Plotly Express chart types](https://plotly.com/python/plotly-express/) at the end of the 'Overview'
section.

## Task 3: Create a scatter mapbox using Plotly Express

Create a scatter mapbox to answer the question:

1. Where in the world have the Paralympics have been held?

For this you can adapt
the [OpenStreetMap tiles example](https://plotly.com/python/mapbox-layers/#openstreetmap-tiles-no-token-needed) in the
Plotly documentation. Unlike the Lollapalooza example, this does not require a token.

The example given in the Plotly documentation is:

```python
import pandas as pd

us_cities = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/us-cities-top-1k.csv")

import plotly.express as px

fig = px.scatter_mapbox(us_cities, lat="lat", lon="lon", hover_name="City", hover_data=["State", "Population"],
                        color_discrete_sequence=["fuchsia"], zoom=3, height=300)
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
fig.show()
```

By now you should be able to work out the general steps without being explicitly told. A couple of hints though:

- follow the example code above replacing it with the paralympics data and passing the relevant column names to `lat=`
  , `lon=`, `hover_name=`, `hover_data=`
- change zoom to `zoom=1` and delete the `height=300` parameter.
- use the following columns from `paralympics.csv`:  `['TYPE', 'YEAR', 'LOCATION', 'LAT', 'LON']`

You could try using the [USGS mapbox](https://plotly.com/python/mapbox-layers/#base-tiles-from-the-usgs-no-token-needed)
instead (or as well and see which you prefer).

## Task 4: Create a table using Plotly Express and Graph Objects (Go)

Create a table to answer the following:

1. What are the top 10 countries that has won the highest number of gold medals in total over all of the paralympic
   events?

You will need to refer to the [Plotly Go table documentation](https://plotly.com/python/table/#use-a-pandas-dataframe)

Alternatively, you can create the table directly in Dash. There
is [an example here](https://plotly.com/python/table/#tables-in-dash).

The pandas `groupby` and `sort_values` functions may be useful here e.g.:

```python
df_gold = df_gold.groupby(by='Country', as_index=False).sum()
df_gold = df_gold.sort_values(by='Gold', ascending=False)
df_gold_ten = df_gold[0:10]
```

## Task 5: Create a choropleth map using Plotly Express

Create
a [choropleth map using GeoPandas](https://plotly.com/python/mapbox-county-choropleth/#using-geopandas-data-frames) to
answer the question.

1. How many medals did each country win in London 2012?

The geojson is in a zip file in the data directory that you will need to extract first (the unzipped file size is too
large for GitHub).

Hints:

- The medals data for London 2021 is in the `all_medals.csv`

```python
import pandas as pd
from pathlib import Path

medals_data_filepath = Path(__file__).parent.joinpath('data', 'all_medals.csv')
df_medals = pd.read_csv(medals_data_filepath)
df_medals_event = df_medals[(df_medals['Event'] == 'London') & (df_medals['Year'] == '2012')]
```

- When you create the choropleth you need to specify parameters that indicate which fields in the medals data and
  geojson match. In this case it is the `NPC` column in the medals data and the `properties.ISO_A3`. You could have
  worked this out for yourself by printing the contents of the geojson and the medals dataframe. The values of the
  relevant parameters for the `px.choropleth()` function are:

```
geojson=df_geojson,
locations='NPC',
featureidkey="properties.ISO_A3",
```
