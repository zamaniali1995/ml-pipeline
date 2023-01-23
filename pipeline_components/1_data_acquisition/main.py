"""
The file should implement data acquisition pipeline.
It should load the raw data from any data source and save it.
"""
from typing import List

import pandas as pd
from sklearn import datasets

from src.utils import Log, load_yaml_config, parse_arguments, write_parquet


def load_data() -> pd.DataFrame:
    """Complete me"""
    iris_dataset = datasets.load_iris()
    X = iris_dataset.data
    y = iris_dataset.target
    y_df = pd.DataFrame(y, columns=['target'])
    X_df = pd.DataFrame(X, columns=iris_dataset.feature_names)
    iris_dataset_df = pd.concat([X_df, y_df], axis=1, join='inner')
    return iris_dataset_df


def main(arguments_list: List = None):
    """Main method"""
    arguments = parse_arguments(arguments_list=arguments_list)
    config = load_yaml_config(arguments.config_path)
    main_config = load_yaml_config(arguments.main_config_path)

    Log.info(main_config.log_msg.acquire_data_start_msg)

    Log.info(main_config.log_msg.load_dataset_start_msg)
    dataset_df = load_data()
    Log.info(main_config.log_msg.load_dataset_end_msg)

    Log.info(main_config.log_msg.save_dataset_start_msg)
    write_parquet(df=dataset_df, path=main_config.get('raw_data_path'))
    Log.info(main_config.log_msg.save_dataset_end_msg)

    Log.info(main_config.log_msg.acquire_data_end_msg)


if __name__ == '__main__':
    main()
