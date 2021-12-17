import plotly.express as px

if __name__ == '__main__':
    gapminder = px.data.gapminder()
    fig = px.choropleth(gapminder,
                        locations="iso_alpha",
                        color="lifeExp",
                        hover_name="country",
                        animation_frame="year",
                        color_continuous_scale="Plasma",
                        title="Life expectancy by country over time",
                        template="plotly_dark"
                        )
    fig.show()
