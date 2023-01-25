"""
The file should implement model training pipeline.
It should select the best hyper parameters and the model and save them.
"""
import warnings
from typing import List

import pandas as pd

from src.model.training.utils import Model
from src.utils import load_parquet, load_yaml, parse_arguments, write_parquet

warnings.filterwarnings('ignore')


def main(arguments_list: List = None):
    """Main method"""
    arguments = parse_arguments(arguments_list=arguments_list)
    config = load_yaml(arguments.config_path)
    main_config = load_yaml(arguments.main_config_path)
    train_data_df = load_parquet(path=main_config.path.train_data_path)
    test_data_df = load_parquet(path=main_config.path.test_data_path)

    ranked_feature_df = load_parquet(
        path=main_config.path.feature_score_path
    )

    model = Model(
        models=config.get('models'),
        candidate_params=config.get('candidate_params'),
        target_column=main_config.target_column,
        ranked_features_df=ranked_feature_df,
        train_data_df=train_data_df,
    )

    model.select(
        num_folds=config.num_folds,
    )
    model.save(
        model_path=main_config.path.trained_model_path,
        config_path=main_config.path.config_model_path
    )
    model.save_full(
        path=main_config.path.trained_full_model_path,
        test_data_df=test_data_df
    )


if __name__ == '__main__':
    main()
