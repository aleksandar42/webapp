import plotly.graph_objects as go  # Ensure this is at the top of generate_scatter.py
import warnings

# Suppress FutureWarning messages to avoid console clutter.
# FutureWarning messages often inform about upcoming changes in future library versions.
# They do not affect the current execution of the code, but we suppress them here
# to keep the console output clean and focus on more critical issues.
# If you are developing or updating this code in the future, consider addressing
# the source of these warnings to ensure compatibility with newer versions of the libraries.
#
# The warning was:
#
# The behavior of DatetimeProperties.to_pydatetime is deprecated, in a 
# future version this will return a Series containing python datetime objects instead of 
# an ndarray. To retain the old behavior, call np.array on the result 
# /opt/anaconda3/lib/python3.11/site-packages/_plotly_utils/basevalidators.py:106:

warnings.filterwarnings("ignore", category=FutureWarning)



def update_scatter_plot(selected_city, selected_neighborhood, n_clicks_price, n_clicks_rating, listings_data):
    """
    Generates a plotly figure (fig), based on the selected city and the neighbourhood
    that was selected in the map. With buttons the user can switch
    between a price over time graph and a rating over time graph.

    Parameters
    ----------
    selected_city : str
        The selected city from the dropdown.

    selected_neighborhood : str
        The selected neighbourhood from the map.

    n_clicks_price : int
        The number of times the price button was clicked.

    n_clicks_rating : int
        The number of times the rating button was clicked.

    listings_data : dict
        A dictionary containing the raw listing data for each city.
        The key is the city name while the value is a DataFrame containing the
        raw listing data.
    """
    # Check if the selected city is in the data
    if selected_city not in listings_data:
        return go.Figure(), ""

    # Filter for the selected city
    listings_filtered = listings_data[selected_city][listings_data[selected_city]['neighbourhood_cleansed'] == selected_neighborhood]

    # Either show the price or the rating over time, based on clicked button
    if n_clicks_rating > n_clicks_price:
        ratings_filtered = listings_filtered[~((listings_filtered['date'].dt.year == 2024) & (listings_filtered['date'].dt.month.isin([10, 11])))]

        listings_aggregated = ratings_filtered.groupby('date').agg(
            mean_rating=('review_scores_rating', 'mean')
        ).reset_index()

        fig = go.Figure()

        # Add scatter plot trace that features markers and lines
        fig.add_trace(go.Scatter(
            x=listings_aggregated['date'],
            y=listings_aggregated['mean_rating'],
            mode='markers+lines',
            name='Mean Rating',
            line=dict(color='blue'),
            marker=dict(color='blue', size=8)
        ))

        # Customize layout and appearance of plotly figure (fig) rating over time
        fig.update_layout(
            title=f'Rating Over Time in {selected_neighborhood}',
            xaxis_title='Date',
            yaxis_title='Rating',
            xaxis=dict(
                showgrid=True,
                zeroline=False,
                tickmode='array',
                tickvals=listings_aggregated['date'][listings_aggregated['date'] <= '2024-06-01'],
                ticktext=[date.strftime('%Y-%m') for date in listings_aggregated['date'][listings_aggregated['date'] <= '2024-06-01']],
                gridcolor='rgba(0,0,0,0.3)',
                gridwidth=1,
            ),
            yaxis=dict(
                showgrid=True,
                zeroline=False,
                gridcolor='rgba(0,0,0,0.3)',
                gridwidth=1,
            ),
            template='plotly',
            margin=dict(l=40, r=40, t=40, b=40),
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            xaxis_showspikes=False,
            yaxis_showspikes=False,
            xaxis_showline=True,
            yaxis_showline=True,
            xaxis_linecolor='black',
            yaxis_linecolor='black',
            xaxis_linewidth=2,
            yaxis_linewidth=2,
        )

        return fig, "Rating Over Time"

    else:
        # Group data in listings_aggregated and calculate mean price and confidence interval
        listings_aggregated = listings_filtered.groupby('date').agg(
            mean_price=('price', 'mean'),
            conf_int_lower=('conf_int_lower', 'mean'),
            conf_int_upper=('conf_int_upper', 'mean')
        ).reset_index()

        fig = go.Figure()

        # Add scatter plot trace for historical data
        fig.add_trace(go.Scatter(
            x=listings_aggregated['date'][:-2],  # All dates except the last two (forecasted)
            y=listings_aggregated['mean_price'][:-2],
            mode='markers+lines',
            name='Mean Price',
            line=dict(color='#FF5A5F'),  # Original color for historical data
            marker=dict(color='#FF5A5F', size=8)
        ))

        # Add scatter plot trace for forecasted data (last two points)
        fig.add_trace(go.Scatter(
            x=listings_aggregated['date'][-2:],  # Last two dates (forecasted)
            y=listings_aggregated['mean_price'][-2:],
            mode='markers+lines',
            name='Forecasted Price',
            line=dict(color='orange', dash='solid'),  # Different color and dashed line for forecast
            marker=dict(color='orange', size=8)  # Different marker style
        ))

        # Add connecting line between the last historical point and the first forecasted point
        if len(listings_aggregated) > 2:
            fig.add_trace(go.Scatter(
                x=[listings_aggregated['date'].iloc[-3], listings_aggregated['date'].iloc[-2]],
                y=[listings_aggregated['mean_price'].iloc[-3], listings_aggregated['mean_price'].iloc[-2]],
                mode='lines',
                line=dict(color='orange', dash='solid'),  # Solid blue line
                showlegend=False
            ))

        # Add shape (confidence interval) to plotly figure (fig)
        fig.add_trace(go.Scatter(
            x=listings_aggregated['date'].tolist() + listings_aggregated['date'][::-1].tolist(),
            y=listings_aggregated['conf_int_upper'].tolist() + listings_aggregated['conf_int_lower'][::-1].tolist(),
            fill='toself',
            fillcolor='rgba(255, 90, 95, 0.2)',
            line=dict(color='rgba(255, 90, 95, 0)'),
            hoverinfo="skip",
            showlegend=True,
            name='Confidence Interval'
        ))

        # Set layout and appearance of plotly figure (fig) price over time
        fig.update_layout(
            title=f'Price Over Time in {selected_neighborhood}',
            xaxis_title='Date',
            yaxis_title='Price',
            xaxis=dict(
                showgrid=True,
                zeroline=False,
                tickmode='array',
                tickvals=listings_aggregated['date'],
                ticktext=[date.strftime('%Y-%m') for date in listings_aggregated['date']],
                gridcolor='rgba(0,0,0,0.3)',
                gridwidth=1,
            ),
            yaxis=dict(
                showgrid=True,
                zeroline=False,
                gridcolor='rgba(0,0,0,0.3)',
                gridwidth=1,
            ),
            template='plotly',
            margin=dict(l=40, r=40, t=40, b=40),
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            xaxis_showspikes=False,
            yaxis_showspikes=False,
            xaxis_showline=True,
            yaxis_showline=True,
            xaxis_linecolor='black',
            yaxis_linecolor='black',
            xaxis_linewidth=2,
            yaxis_linewidth=2,
        )

        return fig, "Price Over Time"
