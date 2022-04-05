# Data Manipulation
import pandas as pd
import numpy as np
import os
import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

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
spark = SparkSession \
    .builder \
    .appName("how to read csv file") \
    .getOrCreate()
df_spark_data= spark.read.csv(str(files[2]),header="true")

df_spark_data = df_spark_data.withColumnRenamed("energy","actual")


#data visualisation

#print schema of the data frame
df_spark_data.printSchema()

#print first few rows of the data frame
df_spark_data.show(10)

# change schema of the df
#change the timestamp str dtype to datetime dtype
df_schema_changed = df_spark_data.withColumn("timestamp",to_timestamp("timestamp"))

#change the actual column to float dtype
def convert_schema_col_to_double(dframe, col_name):
    df_schema_changed=dframe.withColumn(col_name,col(col_name).cast('double'))
    return df_schema_changed

def convert_schema_col_to_int(dframe, col_name):
    df_schema_changed=dframe.withColumn(col_name,col(col_name).cast('int'))
    return df_schema_changed

df_schema_changed=convert_schema_col_to_double(df_schema_changed, "actual")
df_schema_changed=convert_schema_col_to_double(df_schema_changed, "temperature")
df_schema_changed=convert_schema_col_to_double(df_schema_changed, "irradiance")
df_schema_changed=convert_schema_col_to_double(df_schema_changed, "relative_humidity")
df_schema_changed=convert_schema_col_to_double(df_schema_changed, "time_of_day")
df_schema_changed = convert_schema_col_to_int(df_schema_changed,"business_day")
df_schema_changed = convert_schema_col_to_int(df_schema_changed,"day_of_week")
df_schema_changed = convert_schema_col_to_int(df_schema_changed,"day_of_year")


df_schema_changed.printSchema()


#task 1
# 1d line plot of column-actual
#task 2
# a pie chart of the data for unique years


# def _plot_pie_chart_yearwise(data_to_plot,data_years):
#     plt.pie(data)
    
def _plot_timeseris_data(data_to_plot,label):
    plt.figure()
    plt.plot(data_to_plot["actual"])
    plt.title(label)
    plt.xlabel("Timestamp")
    plt.ylabel("Actual Energy")
    
    plt.show()

