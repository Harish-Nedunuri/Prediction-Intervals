import argparse
from pathlib import Path
import json
import pandas as pd

from prediction_intervals import get_intervals

  
def load_processed_data(input_data_filename) -> list:

    print(f"Reading input file: {input_data_filename}")
    try:
        with open(input_data_filename) as data_file:

            data = pd.read_csv(files[3], parse_dates=['timestamp'],
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
    model_configs,
    output_directory,

):

    data = load_data(input_moisture_filename)

    model_configs = load_config_json(setting_filename)
    prediction_intervals, outputs = get_intervals(
        data, model_configs
    )

    print(f"{prediction_intervals=}")
    print(f"{outputs=}")


def main():
    args = parse_arguments()
    forecast_intervals_full(args.energy_data_filename,
                            args.model_configs, args.outdir)
    
if __name__ == "__main__":
    main()
