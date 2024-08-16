import pandas as pd

def get_city_options(city_paths):
    """
    Generates options for the city dropdown.

    Parameters
    ----------
    city_paths : dict
        A dictionary containing the paths to the data for each city.

    Returns
    -------
    list
        A list of dictionaries containing label-value pairs for each city.
    """
    return [{'label': city, 'value': city} for city in city_paths.keys()]

def get_neighborhood_options(listings_data, selected_city):
    """
    Generates unique neighborhood options for the dropdown menu.

    Parameters
    ----------
    listings_data : dict
        A dictionary containing the raw listing data for each city.
    selected_city : str
        The selected city from the dropdown.

    Returns
    -------
    list
        A list of dictionaries containing label-value pairs for neighborhood options.

    Raises
    ------
    KeyError
        If the selected city is not in the listings data.
    """
    if selected_city in listings_data:
        neighborhoods = listings_data[selected_city]['neighbourhood_cleansed'].unique()
        return [{'label': neighborhood, 'value': neighborhood} for neighborhood in neighborhoods]
    return []

def filter_listings(listings_data, selected_city, selected_month, selected_neighborhood):
    """
    Filters listings based on the selected city, month, and neighborhood.

    Parameters
    ----------
    listings_data : dict
        A dictionary containing the raw listing data for each city.
    selected_city : str
        The selected city from the dropdown.
    selected_month : int
        The selected month from the slider.
    selected_neighborhood : str
        The selected neighborhood from the dropdown.

    Returns
    -------
    pd.DataFrame
        A filtered DataFrame of listings data.

    Raises
    ------
    KeyError
        If the selected city is not in the listings data.
    """
    return listings_data[selected_city][
        (listings_data[selected_city]['month'] == selected_month) &
        (listings_data[selected_city]['neighbourhood_cleansed'] == selected_neighborhood)
    ]
