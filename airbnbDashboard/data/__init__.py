"""
data: This module provides functionality for loading listings and GeoJSON data for each city, 
as well as managing the repository to ensure the latest data is always used.

Imports:
--------
load_data : function
    A function to load the GeoJSON and CSV data for each city, grouping and 
    aggregating the data before creating a copy of the relevant columns
    for later use.
    
city_paths : dict
    A dictionary that contains the city name as key and another 
    dictionary as value that contains the paths to the GeoJSON and CSV files.

clone_or_update_repo : function
    A function to clone the GitHub repository or update it if it already exists 
    locally. Ensures that the latest data is always used.

setup_repo : function
    A function to initialize the repository setup process, ensuring all necessary 
    data is downloaded and updated before being used in the application.

Usage
-----
To load data for a specific city:

>>> from data import load_data, city_paths, clone_or_update_repo
>>> clone_or_update_repo()  # Ensure the latest data is available
>>> data = load_data(city_paths)

The `__all__` list specifies the public API of the package, indicating that only
`load_data`, `city_paths`, `clone_or_update_repo`, and `setup_repo` should be accessible when the package is imported.
"""

from .loader import load_data
from .paths import city_paths
from .repo_manager import clone_or_update_repo, setup_repo

__all__ = ['load_data', 'city_paths', 'clone_or_update_repo', 'setup_repo']
