# Adding matplotlib and plotly express charts to a Flask app

You need to know how to do this for coursework 1. This activity gives you an opportunity to learn and practice.

The Flask app is similar **but not identical** to the template provided for coursework 1. In particular it does not
contain the Dash elements. Do not use this in place of the template for coursework 1!

Pre-requisites:

- You need to have an understanding of HTML (covered in week 2)
- You need to have set-up your development environment for this project to run Flask (see the `readme.md` in this repo)

## Save your matplotlib charts as graphic files

There is a method in matplotlib to save a
fig, [matplotlib.pyplot.savefig](https://matplotlib.org/3.3.3/api/_as_gen/matplotlib.pyplot.savefig.html)

Here is an example:

```python
import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
plt.savefig('plot_line.png', format='png')
```

You will then need to move the 'plot_line.png' into the flask_app/static/charts folder.

If you look at the code in `flask_app/save_charts.py` you will see that I have created a function that saves my charts
to this folder.

### Try it!

Now save at least one matplotlib chart that you have created e.g. in the week 1 activities as `png` and save it to the
flask_app/static/charts directory.

## To save your plotly express charts as html

There is a method in plotly express that allows you to do
this [write_html](https://plotly.github.io/plotly.py-docs/generated/plotly.io.write_html.html).

Here is an example:

```python
import plotly.express as px

gapminder = px.data.gapminder()
fig = px.choropleth(gapminder,
                    locations="iso_alpha",
                    color="lifeExp",
                    hover_name="country",
                    animation_frame="year",
                    color_continuous_scale='Plasma',
                    height=600
                    )
fig.write_html('gapminder_choropleth.html')
```

You will then need to move the 'gapminder_choropleth.html' into the flask_app/static/charts folder.

If you look at the code in `flask_app/save_charts.py` you will see that I have created a function that saves my charts
to this folder.

This may seem strange to some of you as html files are usually saved in the templates folder, however for marking
purposes it would be easier if you can place all your charts in the same directory i.e. static/charts.

### Try it: save your own px chart as `.html`

Now save at least one plotly express chart that you have created as `html` and save it to the flask_app/static/charts
directory.

## Add a matplotlib chart to a Flask app

You will need to edit `.html` files which you should have some understanding of from week 2 activities.

If you open flask_app/templates/matplotlib.html you will see that the code starts like this:

```jinja
{% extends "layout.html" %}
{% block content %}
    <h1>Matplotlib charts</h1>
```

Ignore the lines of code that look like this ``{% %}``. This is Jinja templating language which we will not cover until
later in the course. For now ignore those lines and do not change them.

You should edit the section that starts:

```html
<h1>Matplotlib charts</h1>
<h2>Chart name</h2>
```

To add the `plot_line.png` that we created earlier, you could add html like this to the file. Note that the syntax for the
image is Jinja again. When you add your own charts you just need to edit the last part of the filename so it matches
your chart filename.

```jinja
<h2>Matplotlib example chart</h2>
<img alt="Matplotlib line chart example" src="{{ url_for('static', filename='/charts/plot_line.png') }}">
<p>Text explanation. See the coursework spec on Moodle for details of what to write here.</p>
```

To view the page you will need to run the Flask app. How you do this will depend on your IDE.

In PyCharm you can open flask_app.py and select the green arrow to run the main code:

```python
if __name__ == '__main__':
    app.run()
```

Open a web browser and go to the URL for your Flask app, this usually defaults to http://127.0.0.1:5000/

You should be able to go to http://127.0.0.1:5000/matplotlib to see the changes you just made to matplotlib.html

## Add a plotly express chart to a Flask app

As your plotly express charts may have dynamic elements then you may prefer to include these as html rather than static
.png images.

Open `flask_app/templates/express.html` and you will see the file starts as follows:

```Jinja
{% extends "layout.html" %}
{% block content %}
    <h1>Plotly express charts</h1>
    <h2>Chart name</h2>
```

As before, don't edit the lines that start and end `{% %}`, just edit the html tags.

To add a link to the `gapminder_choropleth.html` file saved in charts:

```jinja
h1>Plotly express charts</h1>
<h2>Gapminder choropleth</h2>
<p><a href="{{ url_for('static', filename='/charts/gapminder_choropleth.html') }}">gapminder_choropleth chart</a></p>p>
<p>Your text about the chart</p>
```

If you Flask app is already running then you don't need to start it again, however if it isn't then you will need to
start it to view the page.

In PyCharm you can open flask_app.py and select the green arrow to run the main code:

```python
if __name__ == '__main__':
    app.run()
```

Open a web browser and go to the URL for your Flask app, this usually defaults to http://127.0.0.1:5000/

You should be able to go to http://127.0.0.1:5000/express to see the changes you just made to matplotlib.html

## Add your coursework charts to your GitHub classroom repo

You should be able to use the information above to add the charts to your coursework 1 in the github classroom repo.

