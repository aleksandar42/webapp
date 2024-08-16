from dash import dcc, html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import plotly.graph_objects as go  # Import for go.Figure

from airbnbDashboard.plots import update_map, update_scatter_plot, get_sort_options, generate_sorted_table
from airbnbDashboard.utils.helpers import get_neighborhood_options, filter_listings
from airbnbDashboard.plots.generate_scatter import update_scatter_plot



def register_callbacks(app, listings_data, neighborhoods_geojson, neighborhood_stats, date_marks):
    """
    Registers all the callback functions for the Dash application.

    This function connects various inputs and outputs of the Dash app to update
    different components like tables, dropdowns, maps, and plots based on user interaction.

    Parameters
    ----------
    app : dash.Dash
        The Dash app instance where callbacks are registered.
    listings_data : dict
        A dictionary containing the raw listing data for each city.
        The key is the city name, and the value is a DataFrame containing the
        raw listing data.
    neighborhoods_geojson : dict
        GeoJSON data for neighborhoods, used to update the map visualization.
    neighborhood_stats : dict
        Aggregated statistics for each neighborhood.
    date_marks : dict
        A dictionary mapping slider positions to date labels.

    Notes
    -----
    - Each callback function handles a specific aspect of the application's interactivity.
    - The callback functions rely on user input through dropdowns, sliders, and other UI elements.

    Exceptions
    ----------
    - If `selected_city` is not in `listings_data`, some callbacks return default or empty values.
    - This prevents the app from crashing due to invalid user inputs.
    """

    @app.callback(
        Output('table-container', 'children'),
        [
            Input('city-dropdown', 'value'), 
            Input('month-slider', 'value'), 
            Input('sort-dropdown', 'value'), 
            Input('columns-dropdown', 'value'), 
            Input('order-asc', 'n_clicks'), 
            Input('order-desc', 'n_clicks'), 
            Input('neighborhood-dropdown', 'value')
        ]
    )
    def update_table(selected_city, selected_date_index, sort_by, selected_columns, n_clicks_asc, n_clicks_desc, selected_neighborhood):
        """
        Updates the Dash table figure based on selected city, month, neighborhood, 
        sort by, and additional columns options.

        Parameters
        ----------
        selected_city : str
            The selected city from the dropdown.

        selected_date_index : int
            The selected date index from the date slider.

        sort_by : str
            The selected column to sort by.

        selected_columns : list
            The selected columns to display in the table.

        n_clicks_asc : int
            The number of times the ascending button was clicked.

        n_clicks_desc : int
            The number of times the descending button was clicked.

        selected_neighborhood : str
            The selected neighborhood from the dropdown.

        Returns
        -------
        html.Div
            A table figure containing the sorted listings data.

        Raises
        ------
        KeyError
            If the selected city is not in the listings data.
        """
        if selected_city not in listings_data:
            return html.Div("Invalid city selected")

        selected_month = int(date_marks[selected_date_index].split('-')[1])
        listings_filtered = filter_listings(listings_data, selected_city, selected_month, selected_neighborhood)
        return generate_sorted_table(listings_filtered, sort_by, selected_columns, n_clicks_asc, n_clicks_desc)

    @app.callback(
        Output('sort-dropdown', 'options'),
        [Input('city-dropdown', 'value')]
    )
    def update_sort_options(selected_city):
        """
        Generates and returns sorting options for the dropdown menu in the table figure.

        Parameters
        ----------
        selected_city : str
            The selected city from the dropdown.

        Returns
        -------
        list
            A list of sorting options for the dropdown menu.

        Raises
        ------
        KeyError
            If the selected city is not in the listings data.
        """
        return get_sort_options(listings_data, selected_city)

    @app.callback(
        Output('columns-dropdown', 'options'),
        [Input('city-dropdown', 'value')]
    )
    def update_column_options(selected_city):
        """
        Generates and returns column options for the dropdown menu in the table figure.

        Parameters
        ----------
        selected_city : str
            The selected city from the dropdown.

        Returns
        -------
        list
            A list of column options for the dropdown menu.
        """
        return get_sort_options(listings_data, selected_city)

    @app.callback(
        Output('map-container', 'children'),
        [Input('city-dropdown', 'value'), Input('month-slider', 'value')]
    )
    def update_map_callback(selected_city, selected_date_index):
        """
        Updates the map based on the selected city and date.

        Parameters
        ----------
        selected_city : str
            The selected city from the dropdown.

        selected_date_index : int
            The selected date index from the date slider.

        Returns
        -------
        dash_html_components.Div
            A div containing the updated map figure.
        """
        selected_month = int(date_marks[selected_date_index].split('-')[1])
        return update_map(selected_city, selected_month, neighborhoods_geojson, neighborhood_stats)

    @app.callback(
        Output('neighborhood-dropdown', 'value'),
        Input('clicked-neighborhood', 'data'),
    )
    def update_neighborhood_dropdown(clicked_neighborhood):
        """
        Updates the neighborhood dropdown based on the clicked neighborhood in the map.

        Parameters
        ----------
        clicked_neighborhood : str
            The neighborhood clicked on the map.

        Returns
        -------
        str
            The updated neighborhood value for the dropdown.
        """
        return clicked_neighborhood

    @app.callback(
        Output("modal", "is_open"),
        Output('clicked-neighborhood', 'data'),
        [Input('map', 'clickData')],
        [State("modal", "is_open")],
    )
    def toggle_modal(clickData, is_open):
        """
        Toggles the modal visibility and updates the clicked neighborhood data.

        Parameters
        ----------
        clickData : dict
            Data from the map click event.

        is_open : bool
            Current state of the modal (open or closed).

        Returns
        -------
        bool
            The new state of the modal (open or closed).
        str
            The neighborhood clicked on the map.
        """
        if clickData:
            neighborhood = clickData['points'][0]['location']
            return not is_open, neighborhood
        return is_open, None

    @app.callback(
        Output('scatter-plot', 'figure'),
        Output('plot-title', 'children'),
        [
            Input('city-dropdown', 'value'), 
            Input('neighborhood-dropdown', 'value'), 
            Input('price-over-time', 'n_clicks'), 
            Input('rating-over-time', 'n_clicks')
        ]
    )
    def update_scatter_plot_callback(selected_city, selected_neighborhood, n_clicks_price, n_clicks_rating):
        """
        Updates the scatter plot figure and title based on the selected city, neighborhood, 
        and the number of clicks on the price or rating buttons.

        Parameters
        ----------
        selected_city : str
            The selected city from the dropdown.

        selected_neighborhood : str
            The selected neighborhood from the dropdown.

        n_clicks_price : int
            The number of times the price button was clicked.

        n_clicks_rating : int
            The number of times the rating button was clicked.

        Returns
        -------
        plotly.graph_objs.Figure
            The updated scatter plot figure.

        str
            The updated plot title.

        Raises
        ------
        KeyError
            If the selected city is not in the listings data.
        """
        if selected_city not in listings_data:
            return go.Figure(), ""

        listings_filtered = filter_listings(listings_data, selected_city, None, selected_neighborhood)
        return update_scatter_plot(selected_city, selected_neighborhood, n_clicks_price, n_clicks_rating, listings_data)

    @app.callback(
        Output('neighborhood-dropdown', 'options'),
        [Input('city-dropdown', 'value')]
    )
    def update_neighborhood_options(selected_city):
        """
        Generates and returns neighborhood options for the dropdown menu.

        Parameters
        ----------
        selected_city : str
            The selected city from the dropdown.

        Returns
        -------
        list
            A list of neighborhood options for the dropdown menu.
        """
        return get_neighborhood_options(listings_data, selected_city)
