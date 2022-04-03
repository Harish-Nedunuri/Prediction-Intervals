# Data Manipulation
import pandas as pd
import numpy as np
import os

# Modeling
from sklearn.base import BaseEstimator
from sklearn.ensemble import GradientBoostingRegressor

# File finding
from pathlib import Path
PATH_TESTS_DATA = Path(__file__).resolve().parents
Data_path = PATH_TESTS_DATA[1] / "data"
print(Data_path)
files =[ csvfile for csvfile in Data_path.iterdir() if csvfile.is_file() and csvfile.suffix == ".csv"]
# files = glob.glob('D:\personal\GITHUB_project_prediction_interval')

# Interactivity
from ipywidgets import interact, widgets

# Visualization

# Plotly
import plotly.graph_objs as go
from plotly.offline import iplot, plot, init_notebook_mode
init_notebook_mode(connected=True)
import plotly_express as px

# cufflinks is a wrapper on plotly
import cufflinks as cf
cf.go_offline(connected=True)

data = pd.read_csv(files[2], parse_dates=['timestamp'], index_col='timestamp').sort_index()
print(data.columns)

# data = data.rename(columns={"energy": "actual"})

# data.columns
# data_to_plot = data.loc["2015"].copy()
# def plot_timescale(timescale, selection, theme):
#     """
#     Plot the energy consumption on different timescales (day, week, month).
    
#     :param timescale: the timescale to use
#     :param selection: the numeric value of the timescale selection (for example the 15th day
#     of the year or the 1st week of the year)
#     :param theme: aesthetics of plot
#     """
#     # Subset based on timescale and selection
#     subset = data_to_plot.loc[
#         getattr(data_to_plot.index, timescale) == selection, "actual"
#     ].copy()

#     if subset.empty:
#         print("Choose another selection")
#         return
    
#     # Make an interactive plot
#     fig = subset.iplot(
#             title=f"Energy for {selection} {timescale.title()}", theme=theme, asFigure=True
#     )
#     fig['layout']['height'] = 900
#     fig['layout']['width'] = 1400
#     iplot(fig)

# _ = interact(
#     plot_timescale,
#     timescale=widgets.RadioButtons(
#         options=["dayofyear", "week", "month"], value="dayofyear"
#     ),
#     # Selection 
#     selection=widgets.IntSlider(value=16, min=0, max=365),
#     theme=widgets.Select(options=cf.themes.THEMES.keys(), value='ggplot')
# )