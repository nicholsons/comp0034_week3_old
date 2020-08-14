# Introduction to Plotly Dash
## Overview
>"Dash is a Python framework for building analytical web applications. No JavaScript required. Dash is ideal for building data visualization apps with highly custom user interfaces in pure Python. It’s particularly suited for anyone who works with data in Python.” — Plotly’s site

Dash is written on top of Flask, Plotly.js, and React.js. 

## How does Dash work? 
#### Structure
Dash is comprised of:
- Frontend generated in Python
- Component class for every HTML tag as well as keyword arguments for all of the HTML arguments implemented in dash_html_components package
- Interactive html elements implemented in dash-core-components
- Plotly python API implemented in dash-core-components available through Graph class

#### Declare app layout 
THe app layout will generate react code that will be run in the browser. 

As the layout will generate HTML then it contains elements and each element has attributes.

Each element has attributes that describe its state. 

#### Interaction using Input and Output and the callback decorator
Elements and attributes can be changed by interaction with the user in the browser which makes the app re-render itself. 

You can listen on any changes to those attributes and run callbacks. 

The frontend in the browser sends an HTTP request every time an input is changed. 

Backend recalculates the graph of dependencies and sends back the list of changes to frontend.

These so-called "inputs" and "outputs" of our application interface are described declaratively through the app.callback decorator. 

The inputs and outputs of our application are simply the properties of a particular component. 

Any "Output" can have multiple "Input" components. 

@app.callback(Output('indicator-graphic', 'figure'), 
[Input('xaxis-column', 'value'), Input('yaxis-column', 'value'), Input('year--slider', 'value')]) def update_graph(xaxis_value, yaxis_value, year_slider_value): … ● Each Dash callback function can only update a single Output property. ○ To update multiple Outputs, you have to write multiple functions. ● "State" allows you to pass along extra values without firing the callbacks. ○ @app.callback(Output('indicator-graphic', 'figure'), [Input('xaxis-column', 'value'), Input('yaxis-column', 'value')], [State('year--slider', 'value')]) def update_graph(xaxis_value, yaxis_value, year_slider_value): … ● There are no intermediate values in the reactive graph. ○ You have to add hidden div with intermediate data (as suggested by plotly) ○ Or you have to use redis to store intermediate values (as suggested by plotly)



Displaying charts in Dash
```
import plotly.graph_objects as go # or plotly.express as px
fig = go.Figure() # or any Plotly Express function e.g. px.bar(...)
# fig.add_trace( ... )
# fig.update_layout( ... )

import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()
app.layout = html.Div([
    dcc.Graph(figure=fig)
])

app.run_server(debug=True, use_reloader=False)  # Turn off reloader if inside Jupyter

```