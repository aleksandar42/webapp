# Airbnb Dashboard Web Application

## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Installation](#installation)
5. [Data Sources](#data-sources)
6. [Project Structure](#project-structure)

## Overview
The Airbnb Dashboard is a web application designed to provide insightful visualizations of Airbnb listings across various cities. Built using the Dash framework, the application allows users to interactively explore data on average prices, neighborhood statistics, and other useful information to facilitate informed decisions for travelers and hosts alike.

This application is suitable for data analysts, or anyone interested in understanding Airbnb market dynamics.

## Features
- **Choropleth Map Visualization**: Visualize average prices per neighborhood for the selected city, with detailed hover information.
- **Interactive Data Tables**: Display listings data with options for sorting, filtering, and selecting additional viewable columns.
- **Dynamic Scatter Plots**: Analyze trends in price and review ratings over time with the ability to switch between visualizations.
- **Custom Date Slider**: Enable users to select specific months for data visualization, enhancing the analytical experience.

## Technologies Used
- **Dash**: A rapid web application framework for Python, ideal for building data visualization interfaces.
- **Plotly**: An open-source graphing library that powers the interactive plots within the application.
- **Pandas**: A library that provides data manipulation and analysis tools using data frames.
- **Dash Bootstrap Components**: A library that offers Bootstrap components for better layout and design.
- **Git Large File Storage (LFS)**: Manages large files efficiently in the Git repository.
- **NumPy**: A library for numerical computations, often used with Pandas.
- **Flask**: The underlying web framework for managing server-side logic.
- **JSON**: Used for data interchange, especially with GeoJSON files.
- **Plotly Express**: A high-level interface for quick and easy visualizations.
- **Dash Core Components**: Standard UI components for creating interactive elements.
- **Dash HTML Components**: Allows for custom layouts using HTML tags.
- **Git**: Version control system for tracking changes in the codebase.

## Installation
Follow these detailed steps to set up the project on your local machine:

### Prerequisites
Make sure you have the following installed:
- **Python 3.6 or higher**: You can download and install Python from [Python's official website](https://www.python.org/downloads/).
- **Git**: Download and install Git from [Git's official website](https://git-scm.com/downloads).
- **Git Large File Storage (LFS)**: Follow the installation instructions from the [Git LFS official site](https://git-lfs.github.com/).

### Step-by-Step Installation

1. **Open a Terminal:**
   - On **Windows**: Press `Win + R`, type `cmd`, and press `Enter`.
   - On **macOS**: Open `Finder`, go to `Applications`, then `Utilities`, and open `Terminal`, or use `Ctrl + Space`, search for `Terminal`, and press `Enter`.
   - On **Linux**: Open your terminal from the applications menu.

2. **Select Your Repository Location:**
   Navigate to the directory where you want to clone the project:
   `cd /path/to/your/repository`

3. **Initialize a New Repository:**
    `git init`

4. **Set up GitLFS:**
    `git lfs install`

5. **Fetch Large Files:**
Use the following command to download the large data files managed by Git LFS
    `git lfs pull`

6. **Create a Virtual Environment (skip if you already have one setup):**
It's good practice to create a virtual environment to manage dependencies. Run the following command if you are using Python 3:
    `python -m venv venv`

Activate the virtual environment:

On Windows:
    Type: `venv\Scripts\activate`

On macOS and Linux:
    Type: `source venv/bin/activate`

7. **Install Required Packages:**
With the virtual environment activated, install the necessary libraries using

Type: `pip install -r requirements.txt`

8. **Run the Application:**
Start the application by running

Type: `python app.py`

9. **Access the Application:**
A local URL will be provided:
`Ctrl`/`Strg` + `click`on the link or open your browser and go to http://127.0.0.1:8050 (or localhost:8050) to view the Airbnb Dashboard.

10. **Explore the Dashboard:**
Select a city from the dropdown menu.
Use the date slider to choose specific months of data for visualisation.
Interact with the choropleth maps and tables for deeper insights into listings.


## Data Sources
The application utilises datasets downloaded from the website of [insideairbnb](https://insideairbnb.com), which contains listings
and geographic boundaries for neighbourhoods. The data files are stored utilizing Git LFS due to their large sizes.

CSV files: Found in the data/combined/ directory, these files contain detailed listings data.
GeoJSON files: Located in the data/geojson/ directory, these files define the geographical boundaries of neighborhoods.


## Project Structure
This repository follows a structured format to separate concerns and facilitate maintainability:

```bash
.
├── README.md
├── airbnbDashboard
│   ├── assets
│   │   └── slider.css
│   ├── dashboard
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   ├── callbacks.py
│   │   └── layout.py
│   ├── data
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   ├── loader.py
│   │   ├── paths.py
│   │   └── repo_manager.py
│   ├── plots
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   ├── generate_map.py
│   │   ├── generate_scatter.py
│   │   ├── generate_table.py
│   │   └── slider.py
│   └── utils
│       ├── __init__.py
│       ├── __pycache__
│       ├── app_initializer.py
│       └── helpers.py
├── app.py
├── data
│   ├── combined
│   │   ├── Barcelona_combined_data_final.csv
│   │   ├── Lisbon_combined_data_final.csv
│   │   ├── Madrid_combined_data_final.csv
│   │   ├── Mallorca_combined_data_final.csv
│   │   ├── Milan_combined_data_final.csv
│   │   ├── florence_combined_data_final.csv
│   │   └── rome_combined_data_final.csv
│   └── geojson
│       ├── neighbourhoods_barcelona.geojson
│       ├── neighbourhoods_florence.geojson
│       ├── neighbourhoods_lisbon.geojson
│       ├── neighbourhoods_madrid.geojson
│       ├── neighbourhoods_mallorca.geojson
│       ├── neighbourhoods_milan.geojson
│       └── neighbourhoods_rome.geojson
└── requirements.txt

14 directories, 63 files  files in __pycache__ folders excluded from tree to improve readability

