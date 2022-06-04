import argparse
from pathlib import Path
import json
import pandas as pd
import pyspark 
 
from pyspark.sql import SparkSession

from prediction_intervals import get_intervals
from pyspark import SparkContext


def load_data(input_data_filename: str) -> list:

    print(f"Reading input file: {input_data_filename}")
    try:
        session = SparkSession.builder.appName('First App').getOrCreate() 
        #TODO define a explicit schema, auto schema on read is not recommended
        data = session.read.options(header='True', inferSchema='True', delimiter=',') \
                .csv(input_data_filename)
    except TypeError:
        print(f"Could NOT load file: {input_data_filename}")
        data = []

    return data
def load_config_json(load_config_json_filename: dict) -> dict:
    configs={}
    return configs


def parse_arguments():

    parser = argparse.ArgumentParser(
        description="Estimate prediction intervals"
    )
    parser.add_argument(
        "-e",
        "--energy-data",
        default=None,
        type=Path,
        help="Path to input energy json file",
    )
    parser.add_argument(
        "-c",
        "--config-data",
        default=None,
        type=Path,
        help="Path to input config json file",
    )
    parser.add_argument(
        "-o",
        "--outdir",
        default=None,
        type=Path,
        help="Path to output file",
    )

    return parser.parse_args()


def forecast_intervals_full(
    energy_data_filename,
    model_configs_filename,
    output_directory,

):

    data=load_data(energy_data_filename)
    model_configs = load_config_json(model_configs_filename)
    prediction_intervals, outputs = get_intervals(
        data, model_configs
    )
    
    print(f"{prediction_intervals=}")
    print(f"{outputs=}")


def main():
    # args = parse_arguments()
    # forecast_intervals_full(args.energy_data_filename,
    #                         args.model_configs, args.outdir)
                            
    energy_data_filename="/personal/personal/git_repos/Prediction-Intervals/tests/data/raw/building_2_energy_data.csv"
    model_configs_filename="/personal/personal/git_repos/Prediction-Intervals/tests/data/raw/configs.json"
    outdir="/personal/personal/git_repos/Prediction-Intervals/tests/data"

    forecast_intervals_full(energy_data_filename,model_configs_filename, outdir)
    
if __name__ == "__main__":
    main()
