# Creating a Dash app in PyCharm

The following covers how to create a Dash app in the PyCharm IDE. If you are using a different IDE you will need to refer to its documentation to find equivalent functions.

## Dash app structure
In the last exercise you created the dash app in a single file. This may work for a very simple app but not for an app of more complexity.

A more typical structure might be:

```
Dash_App_Name/
  /assets/  # An optional directory that contains CSS stylesheets, images, or custom JavaScript files. Dash will automatically serve all of the files that are included in this folder.
      app.css  
  /data/  # An optional directory that contains the data files (unless this is accessed via an API or database server).
      data.csv
  app.py  # Contains your Dash app code and code to run the server. Sometimes named dash.py or dashboard.py.
  .gitignore  # The files and folders to be ignored in git.
  requirements.txt  # The app's python dependencies.

```
This is not the only structure you will see. For example, Dash runs as a single page app, you may however want a multi-page app in which case you would have a sub-folder for each dash app and extract the function to run the server to a separate file, typically run.py.

We are also only providing one or two config parameters for the server, e.g. `debug=True`, that we are passing in when we run the server. In practice however you are likely to have more parameters that vary depending on where you are running your app (dev, test, production etc). It would then be more typical to manage config parameters in a separate file such as config.py.

Other files you may see as separate files include: data preparation; figure creation; in practice anything that would be simpler to read and maintain as a separate file might be separated.

## Recreate the example from exercise 3
Add the following code to app.py.
There are three changes from the previous code:
1. As we will be running this as a Python app rather than a jupyter notebook we will create a Python main function and no longer require the `use_reloader=False` parameter.
2. The data directory is in a different location relative to the file that is calling it so this has been changed. A further import was also required for this (`import os`)
3. The assets directory contains w3.css, this stylesheet is used in the app
```python
# Import the required libraries.
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import os

# Import the data set
DATA_DIR = 'data'
data_path = os.path.join(DATA_DIR, 'data.csv')
df = pd.read_csv(data_path)
df['spend'] = df['price']*df['quantitiy']
df = df[['date', 'place', 'spend']]
df = df.groupby(['date','place']).sum().reset_index()

# Create the Plotly figure (bar chart from the previous activity)
fig = px.bar(df, x="spend", y="date", color="place", title="Purchases by place")

# Create a Dash app 
app = dash.Dash(__name__)

# Create the app layout and add the bar chart to it
app.layout = html.Div(children=[
    
    html.H1('Lollapalooza experience'),
    
    dcc.Graph(figure=fig)
])

# Run the web app server
if __name__ == '__main__':
    app.run_server(debug=False) 
```

Run the app and then go to URL your IDE gives you, likely to be http://127.0.0.1:8050/ by default.

### Try adding one of the other charts to your app
As a reminder, the code we used for the charts was as follows.

```python
# Where did I go during the festival?

mapbox_token = "" # Go to https://www.mapbox.com/help/define-access-token/ to get your own token then add it here

px.set_mapbox_access_token(mapbox_token)

data_path = os.path.join(DATA_DIR, 'stages.csv')
df = pd.read_csv(data_path)

fig = px.scatter_mapbox(df, 
                        lat="latitude", 
                        lon="longitude", 
                        color="stage",
                        center=dict(lat = -23.701057,lon = -46.6970635),
                        hover_name="stage",
                        zoom=14.5,
                       title='Lollapalooza Brazil 2018 map')

# How did I spend my money?

data_path = os.path.join(DATA_DIR, 'data.csv')
df = pd.read_csv(data_path)
df["hour_int"] = pd.to_datetime(df["hour"], format="%H:%M", errors='coerce').apply(lambda x: int(x.hour))
df_heatmap = df.pivot_table(index="date",values="price",columns="hour", aggfunc="sum").fillna(0)
fig = px.imshow(df_heatmap, title="Purchases by place")

# Which concerts did I watch?
# You will also need to import plotly_graph_ojects for this one

data_path = os.path.join(DATA_DIR, 'concerts_I_attended.csv')
df_table = pd.read_csv(data_path)

def colorFont(x):    
    if x == "Yes":       
        return "rgb(0,0,9)"    
    else:       
        return "rgb(178,178,178)"
    
df_table["color"] = df_table["correct"].apply(lambda x: colorFont(x))

trace_table = go.Table(header=dict(values=["Concert","Date","Correct?"], fill=dict(color=("rgb(82,187,47)"))),
                       cells=dict(values= [df_table.concert, df_table.date,df_table.correct], font=dict(color=([df_table.color]))))

data = [trace_table]

figure = go.Figure(data = data)
```