
import pandas as pd
import numpy as np
import os

from sklearn.base import BaseEstimator
from sklearn.ensemble import GradientBoostingRegressor
from pyspark.sql.functions import *

from pathlib import Path

LOWER_ALPHA = 0.15
UPPER_ALPHA = 0.85

N_ESTIMATORS = 100
MAX_DEPTH = 5

def example_function():
    return 1 + 1
def _data_spliting(data):
    # convert the timestamp column to timestamp and sort the timestamp column
    data = data.withColumn('timestamp',to_timestamp('timestamp'))
    data=data.sort('timestamp')
    # rename the energy column
    output_data=data.withColumnRenamed("energy","actual")
    output_data = output_data.withColumn('Year', year(col('timestamp')))
    X_train=output_data.where((output_data.Year == "2015") | (output_data.Year == "2016"))
    X_test=output_data.where(output_data.Year == "2017")

    

    return X_train,X_test,output_data
def get_intervals(data, model_configs):
    
    X_train,X_test,output_data = _data_spliting(data)
    y_train = X_train.select(col("actual"))
    y_test = X_test.select(col("actual"))
    # Each model has to be separate

    lower_model = GradientBoostingRegressor(
        loss="quantile", alpha=LOWER_ALPHA, n_estimators=N_ESTIMATORS, max_depth=MAX_DEPTH
    )
    # The mid model will use the default
    mid_model = GradientBoostingRegressor(loss="ls", n_estimators=N_ESTIMATORS, max_depth=MAX_DEPTH)

    upper_model = GradientBoostingRegressor(
        loss="quantile", alpha=UPPER_ALPHA, n_estimators=N_ESTIMATORS, max_depth=MAX_DEPTH
    )
    """
    The models are trained based on optimizing for the specific loss function. 
    This means we have to build 3 separate models to predict the different objectives. 
    A downside of this method is that it's a little slow, particularly because we can't 
    parallelize training on the Scikit-Learn Gradient Boosting Regresssor. If you wanted, you could re-write this code to train each model on a separate processor (using multiprocessing.)
    """
    _ = lower_model.fit(X_train, y_train)
    _ = mid_model.fit(X_train, y_train)
    _ = upper_model.fit(X_train, y_train) 
    prediction_intervals={}
    outputs ={}
    return prediction_intervals,outputs
