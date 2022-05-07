import argparse
from pathlib import Path
import json
import pandas as pd

from prediction_intervals import get_intervals

  
def load_data(input_data_filename: str) -> list:

    print(f"Reading input file: {input_data_filename}")
    try:
        data = pd.read_csv(input_data_filename, parse_dates=['timestamp'],
                        index_col='timestamp').sort_index()
            
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


    model_configs = load_config_json(model_configs_filename)
    prediction_intervals, outputs = get_intervals(
        data, model_configs
    )

    print(f"{prediction_intervals=}")
    print(f"{outputs=}")


def main():
    args = parse_arguments()
    forecast_intervals_full(args.energy_data_filename,
                            args.model_configs, args.outdir)
                            
    # energy_data_filename="/personal/personal/git_repos/Prediction-Intervals/tests/data/raw/building_2_energy_data.csv"
    # model_configs_filename="/personal/personal/git_repos/Prediction-Intervals/tests/data/raw/configs.json"
    # outdir="/personal/personal/git_repos/Prediction-Intervals/tests/data"

    # forecast_intervals_full(energy_data_filename,model_configs_filename, outdir)
    
if __name__ == "__main__":
    main()
