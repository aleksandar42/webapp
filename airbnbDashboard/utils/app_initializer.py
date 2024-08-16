import os
from dash import Dash
import dash_bootstrap_components as dbc

from airbnbDashboard.data.loader import load_data
from airbnbDashboard.data.paths import city_paths
from airbnbDashboard.utils.helpers import get_city_options
from airbnbDashboard.plots.slider import get_unique_dates, generate_date_marks

def initialize_app():
    """Initialize the Dash app."""
    assets_folder = os.path.join(os.path.dirname(__file__), '..', 'assets')
    app = Dash(
        __name__,
        external_stylesheets=[dbc.themes.BOOTSTRAP],
        suppress_callback_exceptions=True,
        assets_folder=assets_folder
    )
    return app

def load_and_prepare_data():
    """Load data and prepare necessary variables for the app."""
    # Load data
    neighborhoods_geojson, neighborhood_stats, listings_data = load_data(city_paths)

    # Get city options for the dropdown
    city_options = get_city_options(city_paths)

    # Get unique dates for the date slider
    unique_dates = get_unique_dates(city_paths)
    date_marks = generate_date_marks(unique_dates)

    return neighborhoods_geojson, neighborhood_stats, listings_data, city_options, date_marks