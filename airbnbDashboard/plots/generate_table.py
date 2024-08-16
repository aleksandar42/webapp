import plotly.graph_objects as go
from dash import dcc

from airbnbDashboard.data.paths import colors, default_columns, column_display_names, additional_columns_list

def generate_table(dataframe, width=1000, height=600):
    """
    Generate, customize, and return a Plotly table that is embedded in
    the modal which pops up after clicking a neighbourhood on the map.

    Parameters
    ----------
    dataframe : pd.DataFrame
        Data frame that contains the listings data for the selected neighbourhood.
    
    width : int, optional
        The width of the table in pixels. The default is 1000.

    height : int, optional
        The height of the table in pixels. The default is 600.
    
    Returns
    -------
    dcc.Graph
        A Plotly table that is embedded in the modal, containing the listings data for the selected neighbourhood.

    Raises
    ------
    KeyError
        If the column names in the data frame are not as expected.
    """
    # Colorcoding for the table
    headerColor = colors['primary']
    rowEvenColor = colors['light']
    rowOddColor = colors['background']

    # Rename columns for more professional look
    dataframe.columns = ['Price' if col == 'price' else 
                         'Rating' if col == 'review_scores_rating' else 
                         'Name' if col == 'name' else
                         'Room Type' if col == 'room_type' else
                         'Reviews' if col == 'number_of_reviews' else
                         'Min. Nights' if col == 'minimum_nights' else
                         'Host' if col == 'host_name' else
                         'ID' if col == 'id' else
                         col for col in dataframe.columns]

    # Create Plotly table & customize style and layout
    fig = go.Figure(data=[go.Table(
        header=dict(
            values=[f'<b>{col}</b>' for col in dataframe.columns],
            line_color=headerColor,
            fill_color=headerColor,
            align=['left', 'center'],
            font=dict(color='white', size=12)
        ),
        cells=dict(
            values=[dataframe[col] for col in dataframe.columns],
            line_color=rowOddColor,
            fill_color=[[rowOddColor, rowEvenColor]*len(dataframe)],
            align=['left', 'center'],
            font=dict(color=colors['text'], size=12),
            height=30,
        )
    )])

    # Update colors of the table
    fig.update_layout(
        width=width, 
        height=height,
        paper_bgcolor='white',
        plot_bgcolor='white'
    )

    return dcc.Graph(figure=fig)

def generate_sorted_table(listings_filtered, sort_by, selected_columns, n_clicks_asc, n_clicks_desc):
    """
    Processes the filtered listings, sorts the data, and generates a table.

    Parameters
    ----------
    listings_filtered : pd.DataFrame
        A DataFrame containing the filtered listings data.
    sort_by : str
        The variable/column to sort the data by.
    selected_columns : list
        A list of column names to display in the table.
    n_clicks_asc : int
        The number of times the ascending button was clicked.
    n_clicks_desc : int
        The number of times the descending button was clicked.

    Returns
    -------
    html.Table
        A table figure containing the sorted listings data.

    Raises
    ------
    KeyError
        If the selected city is not in the listings data.
    """
    if sort_by is None:
        sort_by = 'review_scores_rating'
    
    if selected_columns is None:
        selected_columns = []

    columns_to_display = list(dict.fromkeys(default_columns + selected_columns))

    order = 'asc' if n_clicks_asc > n_clicks_desc else 'desc'
    table_listings = listings_filtered.sort_values(by=sort_by, ascending=(order == 'asc'))
    table_listings = table_listings[columns_to_display]
    return generate_table(table_listings)

def get_sort_options(listings_data, selected_city):
    """
    Generates sorting options for the dropdown menu in the table figure.

    Parameters
    ----------
    listings_data : dict
        A dictionary containing the raw listing data for each city.
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
    if selected_city in listings_data:
        columns = ['price', 'review_scores_rating', 'name'] + additional_columns_list
        available_columns = [col for col in columns if col in listings_data[selected_city].columns]
        return [{'label': column_display_names.get(col, col), 'value': col} for col in available_columns]
    return []

def get_column_options(listings_data, selected_city):
    """
    Generates column options for the dropdown menu in the table figure.

    Parameters
    ----------
    listings_data : dict
        A dictionary containing the raw listing data for each city.
    selected_city : str
        The selected city from the dropdown.

    Returns
    -------
    list
        A list of column options for the dropdown menu.
    """
    if selected_city in listings_data:
        all_columns = listings_data[selected_city].columns
        additional_columns = [col for col in additional_columns_list if col in all_columns]
        return [{'label': column_display_names.get(col, col), 'value': col} for col in additional_columns]
    return []
