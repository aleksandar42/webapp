"""
plots: This package generates maps, tables, scatter plots, and sliders.

The choropleth map is generated based on the selected city and the aggregated statistics for each city.
The table is generated and customized to show the listings data for the selected neighborhood.
The scatter plot is generated based on the selected city and neighborhood, showing price or rating over time.
The slider is created for selecting the date range for the data displayed.

Imports:
--------
update_map
    A function to generate the choropleth map based on the selected city and the aggregated statistics for each city.

generate_table
    A function to generate and customize the table that is embedded in the modal which pops up after clicking a neighborhood in the map.

generate_sorted_table
    A function to process and sort the filtered listings data and then generate a table figure.

get_sort_options
    A function to generate the sorting options for the dropdown menu in the table figure.

get_column_options
    A function to generate the column options for the dropdown menu in the table figure.

update_scatter_plot
    A function to generate a Plotly figure based on the selected city and the neighborhood that was selected in the map.

create_date_slider
    A function to create a Dash slider using the dcc.slider component.

generate_date_marks
    A function to create a dictionary for the marks of the date slider.

get_unique_dates
    A function to iterate through all the cities and return a sorted list of unique dates.

Usage
-----
To generate the choropleth map:
>>> from plots import update_map
>>> fig = update_map(selected_city, listings_data)

To generate the table:
>>> from plots import generate_table
>>> table = generate_table(dataframe)

To generate the scatter plot:
>>> from plots import update_scatter_plot
>>> fig, title = update_scatter_plot(selected_city, selected_neighborhood, n_clicks_price, n_clicks_rating, listings_data)

To create a date slider:
>>> from plots import create_date_slider
>>> slider = create_date_slider(date_marks)

To generate date marks:
>>> from plots import generate_date_marks
>>> date_marks = generate_date_marks(unique_dates)

The `__all__` list specifies the public API of the package, indicating that only
`update_map`, `generate_table`, `generate_sorted_table`, `get_sort_options`, `get_column_options`, `update_scatter_plot`, `create_date_slider`, `generate_date_marks`, and `get_unique_dates` should be accessible when the package is imported.
"""

from airbnbDashboard.plots.generate_map import update_map
from airbnbDashboard.plots.generate_table import generate_table, generate_sorted_table, get_sort_options, get_column_options
from airbnbDashboard.plots.generate_scatter import update_scatter_plot
from airbnbDashboard.plots.slider import get_unique_dates, generate_date_marks, create_date_slider

__all__ = [
    'update_map', 
    'generate_table', 
    'generate_sorted_table', 
    'get_sort_options', 
    'get_column_options', 
    'update_scatter_plot', 
    'create_date_slider', 
    'generate_date_marks', 
    'get_unique_dates'
]
