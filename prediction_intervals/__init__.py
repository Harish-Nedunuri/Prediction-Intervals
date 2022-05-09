
import pandas as pd
import numpy as np
import os


from sklearn.base import BaseEstimator
from sklearn.ensemble import GradientBoostingRegressor


from pathlib import Path

def example_function():
    return 1 + 1

def get_intervals(data, model_configs):
    data = data.withColumn('timestamp', to_date('timestamp'))
    data=data.sort('timestamp')
    data=data.withColumnRenamed("energy","actual")
    
    prediction_intervals={}
    outputs ={}
    return prediction_intervals,outputs
