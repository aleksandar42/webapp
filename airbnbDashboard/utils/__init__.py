"""
utils: This module provides helper functions for processing and filtering data.

Imports:
--------
get_city_options
    A function to generate options for the city dropdown menu.

get_neighborhood_options
    A function to generate unique neighborhood options for a dropdown menu.

filter_listings
    A function to filter listings data based on selected city, month, and neighborhood.

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
"""

from airbnbDashboard.utils.helpers import get_city_options, get_neighborhood_options, filter_listings

__all__ = [
    'get_city_options', 
    'get_neighborhood_options', 
    'filter_listings'
]
