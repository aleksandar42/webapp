"""
utils: This module provides helper functions for processing and filtering data, as well as functions to initialize the Dash app and load necessary data.

Imports:
--------
get_city_options
    A function to generate options for the city dropdown menu.

get_neighborhood_options
    A function to generate unique neighborhood options for a dropdown menu.

filter_listings
    A function to filter listings data based on selected city, month, and neighborhood.

initialize_app
    A function to initialize the Dash app with Bootstrap styling.

load_and_prepare_data
    A function to load data and prepare necessary variables for the app.


Usage:
------
To generate city options:
>>> from utils import get_city_options
>>> city_options = get_city_options(city_paths)

To generate neighborhood options:
>>> from utils import get_neighborhood_options
>>> neighborhood_options = get_neighborhood_options(listings_data, selected_city)

To filter listings data:
>>> from utils import filter_listings
>>> filtered_data = filter_listings(listings_data, selected_city, selected_month, selected_neighborhood)

To initialize the Dash app:
>>> from utils import initialize_app
>>> app = initialize_app()

To load and prepare data:
>>> from utils import load_and_prepare_data
>>> neighborhoods_geojson, neighborhood_stats, listings_data, city_options, date_marks = load_and_prepare_data()
"""

from airbnbDashboard.utils.helpers import get_city_options, get_neighborhood_options, filter_listings
from airbnbDashboard.utils.app_initializer import initialize_app, load_and_prepare_data

__all__ = [
    'get_city_options', 
    'get_neighborhood_options', 
    'filter_listings',
    'initialize_app',
    'load_and_prepare_data'
]
