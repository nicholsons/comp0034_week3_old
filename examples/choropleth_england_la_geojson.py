from pathlib import Path
import plotly.express as px
import pandas as pd
import json

if __name__ == '__main__':

    # open the geojson
    file_path = Path(__file__).parent.joinpath('data', 'england_lad_2011.geojson')

    with open(file_path) as json_file:
        la_geojson = json.load(json_file)

    # Read the data for the over 100's (F105) into a data frame skipping the second heading row
    age_data_path = Path(__file__).parent.joinpath('data', 'la_age_data.csv')
    age_data = pd.read_csv(age_data_path, usecols=["GEO_CODE", "GEO_LABEL", "F105"], skiprows=[1])

    # Reduce the data London
    london = ['E09000002', 'E09000003', 'E09000004', 'E09000005', 'E09000006', 'E09000007', 'E09000008', 'E09000009',
              'E09000010', 'E09000011', 'E09000012', 'E09000013', 'E09000014', 'E09000015', 'E09000016', 'E09000017',
              'E09000018', 'E09000019', 'E09000020', 'E09000021', 'E09000022', 'E09000023', 'E09000024', 'E09000025',
              'E09000026', 'E09000027', 'E09000028', 'E09000029', 'E09000030', 'E09000031', 'E09000032', 'E41000324']

    age_data = age_data[age_data['GEO_CODE'].isin(london)]

    # Create the choropleth mapbox
    fig = px.choropleth_mapbox(age_data,
                               geojson=la_geojson,
                               locations="GEO_CODE",
                               featureidkey="properties.LAD19CD",
                               color="F105",
                               color_continuous_scale='Viridis',
                               range_color=(0, 200),
                               mapbox_style="carto-positron",
                               zoom=8,
                               center={"lat": 51.5074, "lon": 0.0000},
                               opacity=0.5,
                               hover_name="GEO_LABEL",
                               labels={'GEO_LABEL': 'Local authority'},
                               title="London residents over 100 in the 2011 Census"
                               )

    fig.show()
