"""
The file should implement data processing pipeline.
It should clean the data and split it to train and test.
"""
from typing import List

import pandas as pd
from sklearn import datasets

from src.data.processing.utils import rank_features, split_train_test
from src.utils import (Log, load_parquet, load_yaml_config, parse_arguments,
                       write_parquet)


def main(arguments_list: List = None):
    """Main method"""
    arguments = parse_arguments(arguments_list=arguments_list)
    config = load_yaml_config(arguments.config_path)
    main_config = load_yaml_config(arguments.main_config_path)

    Log.info(main_config.log_msg.process_data_start_msg)

    Log.info(main_config.log_msg.load_dataset_start_msg)
    data_df = load_parquet(path=main_config.path.raw_data_path)
    Log.info(main_config.log_msg.load_dataset_end_msg)

    Log.info(main_config.log_msg.split_train_test_start_msg)
    train_df, test_df = split_train_test(
        df=data_df,
        test_size=config.test_siz,
        random_state=main_config.random_state
    )
    Log.info(main_config.log_msg.split_train_test_end_msg)

    Log.info(main_config.log_msg.save_data_as_parquet_start_msg)
    write_parquet(
        df=train_df,
        path=main_config.path.train_data_path
    )
    write_parquet(
        df=test_df,
        path=main_config.path.test_data_path
    )
    Log.info(main_config.log_msg.save_data_as_parquet_end_msg)

    Log.info(main_config.log_msg.rank_feature_start_msg)
    ranked_features_df = rank_features(
        df=train_df,
        target_column=main_config.target_column,
        ignore_column=main_config.ignore_column
    )
    write_parquet(
        df=ranked_features_df,
        path=main_config.path.feature_score_path
    )
    Log.info(main_config.log_msg.rank_feature_end_msg)

    Log.info(main_config.log_msg.process_data_end_msg)


if __name__ == '__main__':
    main()
