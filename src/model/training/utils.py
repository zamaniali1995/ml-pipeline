"""Complete me
"""
from pathlib import Path
from typing import Dict, List, Text

import pandas as pd

from src.model.utils import (evaluate_model, get_model, select_k_feature,
                             split_train_target, tune_hyperparameter)
from src.utils import Log, write_pickle, write_yaml


class Model():
    """
    A class to describe a model object
    """
    def __init__(
        self,
        models: List,
        candidate_params: Dict,
        ranked_features_df: pd.DataFrame,
        train_data_df: pd.DataFrame,
        target_column: Text,
    ) -> None:
        """
        Constructor for the model class

        Parameters
        ----------
        models : List
            List of models that will be used and compared
        candidate_params : Dict
            Dictionary of potential parameters for the models to try
        ranked_features_df : pd.DataFrame
            Dataframe of the ranked features
        train_data_df : pd.DataFrame
            Dataframe containing the training data portion of the total data
        target_column : Text
            Dataframe containing the target data for the models 
        """
        self.models_name = models
        self.candidate_params = candidate_params
        self.target_column = target_column
        self.ranked_features_df = ranked_features_df
        self.train_data_df = train_data_df

    def select(
        self,
        num_folds: int = 5,
    ) -> None:
        """
        Selects the best model from all of the models after training, 
        evaluating, and comparing the results.

        Parameters
        ----------
        num_folds : int, optional
            The number of folds to use during model evaluation, by default 5
        """
        best_metric = 0
        X_train_df, y_train_df = split_train_target(
            data_df=self.train_data_df,
            target_column=self.target_column
        )
        for model_name in self.models_name:
            model = get_model(model_name=model_name)
            for num_feature in self.candidate_params.num_features:
                X_k_feature_train_df = select_k_feature(
                    data_df=X_train_df,
                    num_feature=num_feature,
                    ranked_features_list=list(
                        self.ranked_features_df['feature'])
                )

                best_params, best_model = tune_hyperparameter(
                    model=model,
                    X_df=X_k_feature_train_df,
                    y_df=y_train_df,
                    num_folds=num_folds,
                    candidate_params=dict(
                        self.candidate_params.get(str(model_name)))
                )

                df_metrics = evaluate_model(
                    model=best_model,
                    X_df=X_k_feature_train_df,
                    y_df=y_train_df,
                    num_folds=num_folds,
                )

                if best_metric < df_metrics['accuracy'].values[0]:
                    best_metric = df_metrics['accuracy'].values[0]
                    self.best_model = best_model
                    self.best_model_name = model_name
                    self.best_params = best_params
                    self.best_num_features = num_feature

    def save(self, model_path: Path, config_path: Path, best_params_path: Path) -> None:
        """
        Saves a model with its best parameters after is is trained and has been scored

        Parameters
        ----------
        model_path : Path
            Path to save the model
        config_path : Path
            Path to the configuration file for model training
        best_params_path : Path
            Path to store the best parameters for the models
        """
        write_pickle(file=self.best_model, path=model_path)
        model_config = {
            'num_features': self.best_num_features,
            'model': self.best_model_name,
        }
        write_yaml(file=model_config, path=config_path)
        write_pickle(file=self.best_params, path=best_params_path)

    def save_full(self, path: Path, test_data_df: pd.DataFrame) -> None:
        """
        Saves a model after training on the full dataset

        Parameters
        ----------
        path : Path
            Path to save the model trained on the full dataset
        test_data_df : pd.DataFrame
            DataFrame of the test data to be combined with the training data
        """
        data_df = pd.concat([
            self.train_data_df,
            test_data_df
        ])

        X_df, y_df = split_train_target(
            data_df=data_df,
            target_column=self.target_column
        )

        X_k_feature_df = select_k_feature(
            data_df=X_df,
            num_feature=self.best_num_features,
            ranked_features_list=list(
                self.ranked_features_df['feature'])
        )

        model_full = self.best_model.fit(X_k_feature_df, y_df)
        write_pickle(file=model_full, path=path)
