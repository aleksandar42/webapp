"""
dashboard: This module provides the layout and callback functions for the Dash application.

Imports:
--------
register_callbacks : function
    A function to register all the callback functions for the Dash app.

setup_layout : function
    A function to set up the layout of the Dash app.

Usage
-----
To set up the layout and register the callbacks for the Dash app:

>>> from dashboard import register_callbacks, setup_layout
>>> app = initialize_app()
>>> app.layout = setup_layout()
>>> register_callbacks(app)

The `__all__` list specifies the public API of the package, indicating that only
`register_callbacks` and `setup_layout` should be accessible when the package is imported.
"""

from airbnbDashboard.dashboard.callbacks import register_callbacks
from airbnbDashboard.dashboard.layout import setup_layout

__all__ = ['register_callbacks', 'setup_layout']
