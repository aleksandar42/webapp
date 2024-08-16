import json
import pandas as pd

from airbnbDashboard.data.paths import city_paths

def load_data(city_paths):
    """
    Load the GeoJSON and CSV data for each city.
    
    Parameters
    ----------
    city_paths : dict
        Dictionary containing the paths to the CSV and GeoJSON files for each city.
        The key is the city name while the value is another dictionary that contains
        the paths to the GeoJSON and CSV files.

    Returns
    -------
    neighbourhoods_geojson : dict
        Dictionary containing the GeoJSON data for each city.
        The key is the city name while the value is the GeoJSON data.

    neighbourhood_stats : dict
        Dictionary containing the aggregated statistics for each city.
        The key is the city name while the value is a DataFrame containing the 
        statistics.

    listings_data : dict
        Dictionary containing the raw listing data for each city.
        The key is the city name while the value is a DataFrame containing the
        raw listing data.

    Raises
    ------
    FileNotFoundError
        If the GeoJSON or CSV file for a city is not found.
    """
    neighborhoods_geojson = {}
    neighborhood_stats = {}
    listings_data = {}

    # Iterate through each city and load the corresponding CSV and GeoJSON file
    for city, paths in city_paths.items():
        try:
            with open(paths['geojson'], 'r') as file:
                neighborhoods_geojson[city] = json.load(file)
        except FileNotFoundError:
            print(f"GeoJSON file for {city} not found at {paths['geojson']}") 
            continue

        try:
            # Manually variable types for certain variables
            dtype_spec = {  
                'bathrooms': float,  
                'bedrooms': float,  
                'city': str,  
                'best_model': str   
            }
            with open(paths['listings'], 'r', encoding='utf-8', errors='replace') as file:
                listings = pd.read_csv(file, parse_dates=['date'], dtype=dtype_spec, low_memory=False).dropna(subset=['neighbourhood_cleansed', 'price'])
        except FileNotFoundError:
            print(f"Listings CSV file for {city} not found at {paths['listings']}")
            continue

        listings['month'] = listings['date'].dt.month

        # Columns to aggregate and their aggregation functions
        # Dictionary: Key = column name, Value = aggregation function
        agg_columns = {
            'price': 'mean',
            'review_scores_rating': 'mean',
            'number_of_reviews': 'mean',
            'name': 'count'
        }

        # Check if columns from agg_columns exist in listings data of each city
        available_columns = [col for col in agg_columns.keys() if col in listings.columns]
        if not available_columns:
            print(f"No columns to aggregate in listings for {city}")
            continue

        # Group and aggregate listings data & rename columns for map tooltip
        neighborhood_stats[city] = listings.groupby(['neighbourhood_cleansed', 'month'])[available_columns].agg(agg_columns).reset_index()
        if 'price' in neighborhood_stats[city].columns:
            neighborhood_stats[city] = neighborhood_stats[city].rename(columns={'price': 'avg_price'})
        if 'review_scores_rating' in neighborhood_stats[city].columns:
            neighborhood_stats[city] = neighborhood_stats[city].rename(columns={'review_scores_rating': 'avg_ratings'})

        # Create a copy of listings data for each city containing the relevant columns
        listings_data[city] = listings[['date', 'month', 'price', 'neighbourhood_cleansed', 'review_scores_rating', 'name', 'host_total_listings_count',
                                        'number_of_reviews', 'id', 'room_type', 'host_name', 'minimum_nights', 'host_id', 'reviews_per_month',
                                        'conf_int_upper', 'conf_int_lower', 'city', 'best_model']].copy()

    return neighborhoods_geojson, neighborhood_stats, listings_data
