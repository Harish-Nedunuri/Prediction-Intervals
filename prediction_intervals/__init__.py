
import pandas as pd
import numpy as np
import os


from sklearn.base import BaseEstimator
from sklearn.ensemble import GradientBoostingRegressor
from pyspark.sql.functions import *

from pathlib import Path

def example_function():
    return 1 + 1
def _data_cleaning(data):
    # convert the timestamp column to timestamp and sort the timestamp column
    data = data.withColumn('timestamp',to_timestamp('timestamp'))
    data=data.sort('timestamp')
    # rename the energy column
    output_data=data.withColumnRenamed("energy","actual")
    data_2015=data.where(data.timestamp.Year == "2015")

    return output_data
def get_intervals(data, model_configs):
    
    cleaned_data = _data_cleaning(data)
    prediction_intervals={}
    outputs ={}
    return prediction_intervals,outputs
