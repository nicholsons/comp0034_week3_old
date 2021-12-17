# Create a Covid-19 dashboard using Dash
It is likely to be easier if you create a new project for this activity. This will give you practice in structuring a Dash project from scatch.

The task is to create a Covid dashboard with a chart visualising the data from the [COVID-19 Data Repository by the Center for Systems Science and Engineering (CSSE) at Johns Hopkins University](https://github.com/CSSEGISandData/COVID-19).

Have a look at [their dashboard](https://www.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6) and try to recreate one of the charts.

You might want to start with a more straightforward chart such as the bar chart of the daily cases from February to August, and then try one of the more complex charts.

A guide as to the likely steps:

1. Create a new project in your IDE
2. Create a venv
3. Install required packages in the venv e.g. Dash, pandas
4. Download the data and save in a 'data' directory
5. Find css to use (e.g. add a css file to the assets, use a CDN hosted version, use the dash-bootstrap-components library)
6. Create an app.py in which you:
- Import the required libraries
- Import the dataset
- Create the app instance
- Create the Plotly figure(s)
- Create the layout
- Run the server

Note: You might want to create an initial app.py with no CSS, data or figures and simply an html p element with 'Hello, World' in the layout. This would allow you to test your app runs with minimal coding.

If you develop your app incrementally it may help you to pinpoint errors.  For example, next add CSS and stop and restart the app. Then add data and figure and the restart the app again. 

...and so on...


