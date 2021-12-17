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
