import os
from dash import Dash
import dash_bootstrap_components as dbc

from airbnbDashboard.dashboard.callbacks import register_callbacks
from airbnbDashboard.dashboard.layout import setup_layout
from airbnbDashboard.utils.app_initializer import initialize_app, load_and_prepare_data
from airbnbDashboard.data.repo_manager import setup_repo

def main():
    print("Starting the application...")

    # Define your repository URL and the local directory where you want to clone it
    repo_url = 'https://github.com/aleksandar42/webapp.git'
    local_dir = os.path.join(os.path.expanduser('~'), 'webapp')

    # Set up the repository only once
    setup_repo(repo_url, local_dir)

    # Initialize the Dash app
    app = initialize_app()

    # Load and prepare data (only once)
    neighborhoods_geojson, neighborhood_stats, listings_data, city_options, date_marks = load_and_prepare_data()

    # Set up the layout
    app.layout = setup_layout(city_options, date_marks, neighborhoods_geojson, neighborhood_stats)

    # Register the callbacks
    register_callbacks(app, listings_data, neighborhoods_geojson, neighborhood_stats, date_marks)

    # Run the app
    app.run_server(debug=True)

if __name__ == '__main__':
    main()
