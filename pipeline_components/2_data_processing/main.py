"""
The file should implement data processing pipeline.
It should clean the data and split it to train and test.
"""
from typing import List

import pandas as pd
from sklearn import datasets

from src.data_processing.utils import split_train_test
from src.utils import (load_parquet, load_yaml_config, parse_arguments,
                       write_parquet)


def main(arguments_list: List = None):
    """Main method"""
    arguments = parse_arguments(arguments_list=arguments_list)
    config = load_yaml_config(arguments.config_path)
    main_config = load_yaml_config(arguments.main_config_path)
    data_df = load_parquet(path=main_config.get('raw_data_path'))
    train_df, test_df = split_train_test(
        df=data_df,
        test_size=config.get('test_size'),
        random_state=main_config.get('random_state')
    )
    write_parquet(df=train_df, path=main_config.get(
        'processed_train_data_path'))
    write_parquet(df=test_df, path=main_config.get('processed_test_data_path'))


if __name__ == '__main__':
    main()
