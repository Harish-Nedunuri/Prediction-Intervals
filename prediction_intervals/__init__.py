# Data Manipulation
import pandas as pd
import numpy as np
import os
import display_functions
# Modeling
from sklearn.base import BaseEstimator
from sklearn.ensemble import GradientBoostingRegressor
# from ipywidgets import interact, widgets
#Ingestion
import plotly.graph_objs as go
from plotly.offline import iplot, plot, init_notebook_mode
init_notebook_mode(connected=True)
import plotly_express as px
from pathlib import Path
#Visualisation
from display_functions import plot_array,plot_prediction_intervals


PATH_PARENT = Path(__file__).parents[1]
DATA_PATH = PATH_PARENT / "data"
def example_function():
    return 1 + 1


def _get_file_names(path):
    files =[ csvfile for csvfile in DATA_PATH .iterdir() if csvfile.is_file() and csvfile.suffix == ".csv"]
    return files

files = _get_file_names(DATA_PATH) 

data = pd.read_csv(files[3], parse_dates=['timestamp'], index_col='timestamp').sort_index()

data = data.rename(columns={"energy": "actual"})
# data.loc['2015-01-01':'2015-07-01', "actual"]


plot_array(data.loc["2015"].copy())


# Train and test sets
X_train = data.loc["2015":"2016"].copy()
X_test = data.loc["2017":].copy()
y_train = X_train.pop("actual")
y_test = X_test.pop("actual")

assert X_train.index.max() < X_test.index.min()



# Set lower and upper quantile
LOWER_ALPHA = 0.15
UPPER_ALPHA = 0.85

N_ESTIMATORS = 100
MAX_DEPTH = 5

# Each model has to be separate

lower_model = GradientBoostingRegressor(
    loss="quantile", alpha=LOWER_ALPHA, n_estimators=N_ESTIMATORS, max_depth=MAX_DEPTH
)
# The mid model will use the default
mid_model = GradientBoostingRegressor(loss="ls", n_estimators=N_ESTIMATORS, max_depth=MAX_DEPTH)

upper_model = GradientBoostingRegressor(
    loss="quantile", alpha=UPPER_ALPHA, n_estimators=N_ESTIMATORS, max_depth=MAX_DEPTH
)



_ = lower_model.fit(X_train, y_train)
_ = mid_model.fit(X_train, y_train)
_ = upper_model.fit(X_train, y_train)

predictions = pd.DataFrame(y_test)
predictions['lower'] = lower_model.predict(X_test)
predictions['mid'] = mid_model.predict(X_test)
predictions['upper'] = upper_model.predict(X_test)

assert (predictions['upper'] > predictions['lower']).all()



plot_prediction_intervals(predictions['upper'] ,predictions['lower'],predictions['mid'] )

# def plot_intervals(predictions, mid=False, start=None, stop=None, title=None):
#     """
#     Function for plotting prediction intervals as filled area chart.
    
#     :param predictions: dataframe of predictions with lower, upper, and actual columns (named for the target)
#     :param whether to show the mid prediction
#     :param start: optional parameter for subsetting start of predictions
#     :param stop: optional parameter for subsetting end of predictions
#     :param title: optional string title
    
#     :return fig: plotly figure
#     """
#     # Subset if required
#     predictions = (
#         predictions.loc[start:stop].copy()
#         if start is not None or stop is not None
#         else predictions.copy()
#     )
#     data = []

#     # Lower trace will fill to the upper trace
#     trace_low = go.Scatter(
#         x=predictions.index,
#         y=predictions["lower"],
#         fill="tonexty",
#         line=dict(color="darkblue"),
#         fillcolor="rgba(173, 216, 230, 0.4)",
#         showlegend=True,
#         name="lower",
#     )
#     # Upper trace has no fill
#     trace_high = go.Scatter(
#         x=predictions.index,
#         y=predictions["upper"],
#         fill=None,
#         line=dict(color="orange"),
#         showlegend=True,
#         name="upper",
#     )

#     # Must append high trace first so low trace fills to the high trace
#     data.append(trace_high)
#     data.append(trace_low)
    
#     if mid:
#         trace_mid = go.Scatter(
#         x=predictions.index,
#         y=predictions["mid"],
#         fill=None,
#         line=dict(color="green"),
#         showlegend=True,
#         name="mid",
#     )
#         data.append(trace_mid)

#     # Trace of actual values
#     trace_actual = go.Scatter(
#         x=predictions.index,
#         y=predictions["actual"],
#         fill=None,
#         line=dict(color="black"),
#         showlegend=True,
#         name="actual",
#     )
#     data.append(trace_actual)

#     # Layout with some customization
#     layout = go.Layout(
#         height=900,
#         width=1400,
#         title=dict(text="Prediction Intervals" if title is None else title),
#         yaxis=dict(title=dict(text="kWh")),
#         xaxis=dict(
#             rangeselector=dict(
#                 buttons=list(
#                     [
#                         dict(count=1, label="1d", step="day", stepmode="backward"),
#                         dict(count=7, label="1w", step="day", stepmode="backward"),
#                         dict(count=1, label="1m", step="month", stepmode="backward"),
#                         dict(count=1, label="YTD", step="year", stepmode="todate"),
#                         dict(count=1, label="1y", step="year", stepmode="backward"),
#                         dict(step="all"),
#                     ]
#                 )
#             ),
#             rangeslider=dict(visible=True),
#             type="date",
#         ),
#     )

#     fig = go.Figure(data=data, layout=layout)

#     # Make sure font is readable
#     fig["layout"]["font"] = dict(size=20)
#     fig.layout.template = "plotly_white"
#     return fig


# # Example plot subsetted to one week
# fig = plot_intervals(predictions, start="2017-03-01", stop="2017-03-08")
