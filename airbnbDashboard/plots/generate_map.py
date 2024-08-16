import plotly.express as px
from dash import dcc, html

from airbnbDashboard.data.paths import colors, city_data

def update_map(selected_city, selected_month, neighborhoods_geojson, neighborhood_stats):
    """
    Generates an interactive map visualization for a selected city and month using Plotly.

    This function creates a choropleth map of neighborhood average prices within a city, filtered by the selected month.
    The map is centered and zoomed based on predefined city data, and the color scale represents the average price in 
    each neighborhood.

    Parameters
    ----------
    selected_city : str
        The name of the city for which to generate the map.
    
    selected_month : str
        The month (in "YYYY-MM" format) for which to filter neighborhood statistics.
    
    neighborhoods_geojson : dict
        A dictionary containing GeoJSON data for neighborhoods, keyed by city name.
    
    neighborhood_stats : dict
        A dictionary containing DataFrames with neighborhood statistics (including 'avg_price' and 'avg_ratings'), 
        keyed by city name.

    Returns
    -------
    dcc.Graph or html.Div
        A Dash `dcc.Graph` component containing the generated map, or an `html.Div` element with an error message 
        if the city is invalid.

    Raises
    ------
    KeyError
        If the selected city is not found in the `neighborhoods_geojson` or `city_data` dictionaries.
    """
    if selected_city not in neighborhoods_geojson:
        return html.Div("Invalid city selected")
    
    neighborhoods_geojson_selected = neighborhoods_geojson[selected_city]
    neighborhood_stats_selected = neighborhood_stats[selected_city]
    
    # Filter by the selected month
    neighborhood_stats_filtered = neighborhood_stats_selected[neighborhood_stats_selected['month'] == selected_month]

    # Use the city_data dictionary to get center and zoom level
    if selected_city in city_data:
        center = city_data[selected_city]["center"]
        zoom_level = city_data[selected_city]["zoom_level"]
    else:
        return html.Div("Invalid city selected")

    fig = px.choropleth_mapbox(
        neighborhood_stats_filtered,
        geojson=neighborhoods_geojson_selected,
        locations='neighbourhood_cleansed',
        featureidkey="properties.neighbourhood",
        color="avg_price",
        mapbox_style="carto-positron",
        zoom=zoom_level,
        center=center,
        opacity=0.6,
        title=" ",
        hover_data={ # tooltip
            'neighbourhood_cleansed': True,
            'avg_price': ':.2f', #display avg_price in tooltips
            'avg_ratings': ':.2f', #displayavg_ratings in tooltip
            'name': True, # name is declared in loader.py:72 and counts number of names in filtered data
        },
        labels={
            'avg_price': 'Average Price',
            'neighbourhood_cleansed': 'Neighborhood',
            'avg_ratings': 'Average Ratings',
            'name': 'Number of Listings', # rename name to Number of Listings, as it is the count of names
        }
    )

    fig.update_layout(
        hoverlabel=dict(
            bgcolor="#F5F5F5",
            font_size=12,
            font_family="Arial",
            font_color="#7F7F7F"
        ),
        margin={"r": 0, "t": 0, "l": 0, "b": 0},
        coloraxis_colorbar=dict(
            title="Average Price",
            tickvals=[neighborhood_stats_filtered['avg_price'].min(), neighborhood_stats_filtered['avg_price'].max()],
            ticktext=["Low", "High"],
            tickcolor="#7F7F7F",
            tickfont=dict(
                color="#7F7F7F"
            ),
            title_font=dict(
                color="#7F7F7F"
            ),
            lenmode="fraction",
            len=1,
            thicknessmode="pixels",
            thickness=20,
            bgcolor="#FFFFFF",
            outlinecolor="#7F7F7F",
            outlinewidth=1
        ),
    )

    return dcc.Graph(
        id='map',
        figure=fig,
        style={'width': '100%', 'height': '750px', 'borderRadius': '10px', 'boxShadow': '0px 4px 10px #0000001A'}
    )
