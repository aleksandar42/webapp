import os
from .repo_manager import clone_or_update_repo

# Set your directory, where the input data is stored
#dataset_dir = '/Users/aleks/Desktop/citydata/dashboard/'
repo_url = 'https://github.com/aleksandar42/webapp.git'
local_dir = os.path.join(os.path.expanduser('~'), 'webapp')

# Clone or update the repository
clone_or_update_repo(repo_url, local_dir)

# Locate where curent file is in the directory
base_dir = os.path.dirname(os.path.abspath(__file__))

# Set up your paths using the local directory
dataset_dir = os.path.join(local_dir, 'data')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Dictionaries
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# Dictionary: Key = city name, Value = dictionary with paths to CSV and GeoJSON files
city_paths = {
    'Madrid, Spain': {
        'listings': os.path.join(dataset_dir, 'combined','Madrid_combined_data_final.csv'),
        'geojson': os.path.join(dataset_dir, 'geojson','neighbourhoods_madrid.geojson')
    },
    'Barcelona, Spain': {
        'listings': os.path.join(dataset_dir, 'combined','Barcelona_combined_data_final.csv'),
        'geojson': os.path.join(dataset_dir, 'geojson','neighbourhoods_barcelona.geojson')
    },
    'Mallorca, Spain': {
        'listings': os.path.join(dataset_dir, 'combined','Mallorca_combined_data_final.csv'),
        'geojson': os.path.join(dataset_dir, 'geojson','neighbourhoods_mallorca.geojson')
    },
    'Florence, Italy': {
        'listings': os.path.join(dataset_dir, 'combined','florence_combined_data_final.csv'),
        'geojson': os.path.join(dataset_dir, 'geojson','neighbourhoods_florence.geojson')
    },
    'Milan, Italy': {
        'listings': os.path.join(dataset_dir, 'combined','Milan_combined_data_final.csv'),
        'geojson': os.path.join(dataset_dir, 'geojson','neighbourhoods_milan.geojson')
    },
    'Rome, Italy': {
        'listings': os.path.join(dataset_dir, 'combined','rome_combined_data_final.csv'),
        'geojson': os.path.join(dataset_dir, 'geojson','neighbourhoods_rome.geojson')
    },
    'Lisbon, Portugal': {
        'listings': os.path.join(dataset_dir, 'combined','Lisbon_combined_data_final.csv'),
        'geojson': os.path.join(dataset_dir, 'geojson','neighbourhoods_lisbon.geojson')
    }
}

# Dictionary: Key = city name, Value = dictionary with center coordinates and zoom level
# To initialize starting point of map when selecting a city
city_data = {
    'Madrid, Spain': {"center": {"lat": 40.472775, "lon": -3.703790}, "zoom_level": 9.80},
    'Barcelona, Spain': {"center": {"lat": 41.389785, "lon": 2.166775}, "zoom_level": 10.9},
    'Mallorca, Spain': {"center": {"lat": 39.695262, "lon": 3.017571}, "zoom_level": 8.85},
    'Florence, Italy': {"center": {"lat": 43.769562, "lon": 11.255814}, "zoom_level": 11.0},
    'Milan, Italy': {"center": {"lat": 45.464204, "lon": 9.189982}, "zoom_level": 10.8},
    'Rome, Italy': {"center": {"lat": 41.902782, "lon": 12.496366}, "zoom_level": 9.6},
    'Lisbon, Portugal': {"center": {"lat": 38.936946, "lon": -9.242685}, "zoom_level": 9.0},
}

# color dictionary 
colors = {
    'background': '#F5F5F5',
    'text': '#333333',
    'primary': '#FF5A5F'
    }

# Dictionary: Key = column name, Value = display name
# Change display name of variables in the table
column_display_names = {
    'neighbourhood_cleansed': 'Neighbourhood',
    'name': 'Name',
    'host_id': 'Host ID',
    'host_name': 'Host',
    'room_type': 'Room Type',
    'number_of_reviews': 'Reviews',
    'reviews_per_month': 'Reviews/Month',
    'id': 'ID',
    'minimum_nights': 'Min. Nights',
    'price': 'Price',
    'review_scores_rating': 'Rating',
    'month': 'Month',
}

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Lists
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

default_columns = ['id', 'price', 'name', 'review_scores_rating']  

# additional columns to be included in the dropdown of table
additional_columns_list = [
    'host_name', 
    'room_type', 
    'number_of_reviews', 
    'minimum_nights'
]