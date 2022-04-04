# Data Manipulation
import pandas as pd
import numpy as np
import os

# Modeling
from sklearn.base import BaseEstimator
from sklearn.ensemble import GradientBoostingRegressor

#Ingestion
from pathlib import Path

#Visualisation
import matplotlib.pyplot as plt

PATH_TESTS_DATA = Path(__file__).resolve().parents
Data_path = PATH_TESTS_DATA[1] / "data"

files =[ csvfile for csvfile in Data_path.iterdir() if csvfile.is_file() and csvfile.suffix == ".csv"]

data = pd.read_csv(files[2], parse_dates=['timestamp'],index_col=["timestamp"]).sort_index()
#%%
data = data.rename(columns={"energy": "actual"})
data_years = pd.DatetimeIndex(data.index).year.unique()
data_to_plot = data.loc[f"{data_years[0]}"]

def _plot_pie_chart_yearwise(data_to_plot,data_years):
    plt.pie(data)
    
def _plot_timeseris_data(data_to_plot,label):
    plt.figure()
    plt.plot(data_to_plot["actual"])
    plt.title(label)
    plt.xlabel("Timestamp")
    plt.ylabel("Actual Energy")
    # ax = plt.gca()
    #plt.draw()

    plt.gca().set_xticklabels(rotation = 45)

    plt.show()
_plot_timeseris_data(data_to_plot,label=f"{data_years[0]}")
#%%
plt.show()
data.loc['2015-01-01':'2015-07-01', "actual"]
data.resample('12 H')["actual"].mean()

# Train and test sets
X_train = data.loc["2015":"2016"].copy()
X_test = data.loc["2017":].copy()
y_train = X_train.pop("actual")
y_test = X_test.pop("actual")
X_train.tail()
X_test.head()
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

plt.figure()
plt.plot(predictions['lower'])
plt.plot(predictions['mod'])
plt.show()