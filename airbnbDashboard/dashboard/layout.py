from dash import dcc, html
import dash_bootstrap_components as dbc

from airbnbDashboard.plots.generate_map import generate_map
from airbnbDashboard.plots.slider import create_date_slider
from airbnbDashboard.data.paths import colors

def setup_layout(city_options, date_marks, neighborhoods_geojson, neighborhood_stats):
    """
    This functions defines the layout of the Dash application.
    It uses Dash and Dash Bootstrap Components (dbc) libraries to
    create a structured layout for the Airbnb Dashboard.

    Parameters
    ----------
    city_options : list
        A list of dictionaries. Each dictionary contains the label and value
        for a city. The label is the city name and the value is the city name.

    date_marks : dict
        Dictionary containing the marks for the slider.
        The key is the index of the mark while the value is the date.

    neighborhoods_geojson : dict
        A GeoJSON dictionary containing the neighborhood boundaries and properties.

    neighborhood_stats : dict
        A dictionary containing the aggregated statistics for each neighborhood.

    Returns
    -------
    html.Div
        A Dash HTML div element containing the layout for the Airbnb Dashboard.

    Raises
    ------
    KeyError
        If the selected city is not in the listings data.

    Generative AI
    -------------
    Generative AI was used to help set the structure of the layout
    and help bug fixing when certain containers were not correctly positioned.
    It also helped to use correct the syntax and add the buttons. 
    """
    return html.Div([
        # Navbar with Header and City Dropdown
        dbc.Navbar(
            dbc.Container(
                [
                    dbc.Row(
                        [
                            # Column for and title
                            dbc.Col(dbc.NavbarBrand("Airbnb Dashboard", className="ml-2", style={"font-size": "30px", "font-weight": "bold", "color": "white"})),
                        ],
                        align="center",  
                        className="g-0",  # Remove gaps between columns
                    ),
                    dbc.Row(
                        [
                            # Column for "Select City" label
                            dbc.Col(html.Div("Select City:", style={'fontSize': '22px', 'fontWeight': '580', 'color': 'white', 'textAlign': 'left'})),
                            # Column for dropdown menu
                            dbc.Col(
                                dcc.Dropdown(
                                    id='city-dropdown',
                                    options=city_options,
                                    value='Madrid, Spain',
                                    style={'width': '200px', 'margin': '10px auto', 'borderRadius': '10px', 'padding': '1px', 'fontSize': '17px', 'textAlign': 'left'},
                                    clearable=True,
                                    searchable=True
                                ),
                                width={"size": "auto"}  
                            ),
                        ],
                        align="center",  
                        className="g-0",  # Remove gaps between columns
                    ),
                ],
                fluid=True,  # Use full width of the container
            ),
            color=colors['primary'],
            dark=True,
            className="mb-4",
            style={"padding": "15px 20px"}
        ),

        # City selection section
        html.Div(
            [
                # Slider
                html.H2("SELECT MONTH", style={'fontSize': '19px', 'fontWeight': '580', 'textAlign': 'center', 'color': '#7F7F7F'}),
                html.Div(
                    create_date_slider(date_marks),
                    style={'width': '85%', 'margin': '0 auto'}  
                ),
                html.Div(id='map-container', children=generate_map('Madrid, Spain', 1, neighborhoods_geojson, neighborhood_stats), 
                style={'transition': 'transform 1s', 'width': '80%', 'margin': '0 auto', 'display': 'flex', 'justify-content': 'center', 'boxShadow': '0px 4px 10px #0000001A', 'borderRadius': '10px'}),
            ],
            style={'padding': '10px', 'backgroundColor': colors['background']}
        ),
        # holds clicked neighborhood value
        dcc.Store(id='clicked-neighborhood'),

        # Modal for Table with Listings
        dbc.Modal(
            [
                dbc.ModalHeader(
                    dbc.ModalTitle(
                        "Neighbourhood Insights",
                        style={'fontSize': '24px', 'fontWeight': 'bold', 'color': 'white'}
                    ),
                    style={'backgroundColor': '#FF5A5F'}  
                ),
                dbc.ModalBody(
                    [
                        # Buttons to switch between plots
                        dbc.Row([
                            dbc.Col([
                                # button froms generative AI -> n_clicks method
                                dbc.Button("Price Over Time", id='price-over-time', n_clicks=0, className='mr-2', style={'backgroundColor': '#FFFFFF','color': '#FF5A5F','border': '1px solid #FF5A5F','outline': 'none','boxShadow': 'none'}),
                                dbc.Button("Rating Over Time", id='rating-over-time', n_clicks=0, style={'backgroundColor': '#FF5A5F','color': '#FFFFFF','border': '1px solid #FFFFFF','outline': 'none','boxShadow': 'none'})
                            ], width=12, style={'textAlign': 'center', 'marginBottom': '20px'}),
                        ]),
                        # Scatter Plot Section
                        html.Div([
                            html.H4("Price Over Time", id='plot-title', style={'fontSize': '18px', 'marginTop': '20px', 'textAlign': 'center', 'color': colors['text']}),
                            dcc.Dropdown(
                                id='neighborhood-dropdown',
                                style={'width': '50%', 'margin': '10px auto', 'borderRadius': '10px', 'padding': '1px', 'fontSize': '15px'},
                                clearable=False,
                                searchable=True
                            ),
                            dcc.Graph(id='scatter-plot'),
                        ], style={'padding': '20px', 'boxShadow': '0px 4px 10px #0000001A', 'borderRadius': '10px', 'marginTop': '20px'}),
                        dbc.Row([
                            dbc.Col([
                                html.H4("Sort Table By", style={'fontSize': '18px', 'marginTop': '10px', 'textAlign': 'center', 'color': colors['text']}),
                                dcc.Dropdown(
                                    id='sort-dropdown',
                                    style={'width': '100%', 'margin': '10px auto', 'borderRadius': '10px', 'padding': '1px', 'fontSize': '15px'},
                                    clearable=False,
                                    searchable=False
                                ),
                            ], width=4),
                            dbc.Col([
                                html.H4("Additional Columns", style={'fontSize': '18px', 'marginTop': '10px', 'textAlign': 'center', 'color': colors['text']}),
                                dcc.Dropdown(
                                    id='columns-dropdown',
                                    multi=True,
                                    style={'width': '100%', 'margin': '10px auto', 'borderRadius': '10px', 'padding': '1px', 'fontSize': '15px'}
                                ),
                            ], width=4),
                            dbc.Col([
                                html.H4("Order", style={'fontSize': '18px', 'marginTop': '10px', 'textAlign': 'center', 'color': colors['text']}),
                                html.Div(
                                    children=[
                                        # button froms generative AI -> n_clicks method
                                        dbc.Button("Ascending", id='order-asc', n_clicks=0, className='mr-2', style={'backgroundColor': '#FFFFFF','color': '#FF5A5F','border': '1px solid #FF5A5F','outline': 'none','boxShadow': 'none'}),
                                        dbc.Button("Descending", id='order-desc', n_clicks=0, style={'backgroundColor': '#FF5A5F','color': '#FFFFFF','border': '1px solid #FFFFFF','outline': 'none','boxShadow': 'none'})
                                    ],
                                    style={'width': '100%', 'textAlign': 'center'}
                                ),
                            ], width=4),
                        ], style={'margin': '20px 0'}),
                        html.Div(id='table-container', style={'padding': '20px', 'boxShadow': '0px 4px 10px #0000001A', 'borderRadius': '10px'})
                    ]
                ),
            ],
            id="modal",
            size="xl",  
            is_open=False,
        ),
    ], style={'fontFamily': 'Arial, sans-serif', 'padding': '0px', 'backgroundColor': colors['background']})
