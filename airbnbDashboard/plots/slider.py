from dash import dcc
import pandas as pd
from datetime import datetime

def get_unique_dates(city_paths):
    """
    Iterates through all the cities and returns a sorted list of unique dates.

    Parameters:
    -----------
    city_paths : dict
        A dictionary containing the paths to the data for each city.
        The key is the city name, while the value is a dictionary containing the
        paths to the listings and calendar data for the city.

    Returns:
    --------
    unique_dates : pd.DatetimeIndex
        A sorted list of unique dates in the dataset.

    Raises:
    -------
    TypeError
        If the `date` column in the listings data is not a date-like object.
    """
    unique_dates = []
    for city, paths in city_paths.items():
        listings = pd.read_csv(paths['listings'], encoding='utf-8', parse_dates=['date'], low_memory=False)  # utf-8 encoding for foreign alphabets
        unique_dates.extend(listings['date'].unique())
    unique_dates = pd.to_datetime(unique_dates).drop_duplicates().sort_values()
    return unique_dates

def generate_date_marks(unique_dates):
    """
    Create a dictionary for the marks of the date slider.
    Sort unique dates in chronological order and create a dictionary.
    Generate a pair of index and date for each date in the list.
    Format the date as 'YYYY-MM' and return the dictionary.

    Parameters
    ----------
    unique_dates : list
        List of unique dates in the dataset.

    Returns
    -------
    date_marks : dict
        Dictionary containing the marks for the slider.
        The key is the index of the mark, while the value is the date.

    Raises
    ------
    TypeError
        If `unique_dates` contains elements that are not date-like objects.
    
    AttributeError
        If elements in `unique_dates` do not have a `strftime` method.

    ValueError
        If `unique_dates` contains elements that cannot be compared for sorting.
    """
    date_marks = {i: date.strftime('%Y-%m') for i, date in enumerate(sorted(unique_dates))}
    return date_marks

def create_date_slider(date_marks):
    """
    Create a Dash slider using the dcc.slider component.
    After a month is selected using the slider, the
    callback functions will update the plots so that only
    the data for the selected month is shown.

    Parameters
    ----------
    date_marks : dict
        Dictionary containing the marks for the slider.
        The key is the index of the mark, while the value is the date.
    
    Returns
    -------
    dcc.Slider
        A Dash slider that allows the user to select a month.
    
    Raises
    ------
    KeyError
    
    """
    return dcc.Slider(
        id='month-slider',
        min=0,
        max=len(date_marks) - 3,  # The last two months in the data only contain 2 rows with the forecasts
        marks=date_marks,
        value=0,
        step=1,
        className='slider-style'
    )
