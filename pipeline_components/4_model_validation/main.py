"""
This file should implement the model validation step in the pipeline.
It should evaluate the model performance and store the accuracy values.
"""
from typing import List

from sklearn.metrics import accuracy_score

from src.model.utils import select_k_feature, split_train_target
from src.utils import load_parquet, load_pickle, load_yaml, parse_arguments


def main(arguments_list: List = None):
    """Main method"""
    arguments = parse_arguments(arguments_list=arguments_list)
    config = load_yaml(arguments.config_path)
    main_config = load_yaml(arguments.main_config_path)
    test_data_df = load_parquet(path=main_config.path.test_data_path)
    model_config = load_yaml(path=main_config.path.config_model_path)
    X_test_df, y_test_df = split_train_target(
        data_df=test_data_df,
        target_column=main_config.target_column
    )
    ranked_features_df = load_parquet(
        path=main_config.path.feature_score_path
    )
    X_k_feature_test_df = select_k_feature(
        data_df=X_test_df,
        num_feature=model_config.num_features,
        ranked_features_list=list(
            ranked_features_df['feature'])
    )
    model = load_pickle(path=main_config.path.trained_model_path)

    X_predicted_list = model.predict(X_k_feature_test_df)
    print(accuracy_score(y_test_df, X_predicted_list))


if __name__ == '__main__':
    main()
