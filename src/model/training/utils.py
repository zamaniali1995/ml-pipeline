"""Complete me
"""
from pathlib import Path
from typing import Dict, List, Text

import pandas as pd
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.ensemble import AdaBoostClassifier, RandomForestClassifier
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.inspection import DecisionBoundaryDisplay
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

from src.model.utils import (evaluate_model, split_train_target,
                             tune_hyperparameter)
from src.utils import Log, write_pickle


class Model():
    """Model evaluation
    """

    def __init__(
        self,
        models: List,
        candidate_params: Dict,
        ranked_features_df: pd.DataFrame,
        train_data_df: pd.DataFrame,
        target_column: Text,
    ) -> None:
        """Complete me
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
        """Complete me
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
                    self.best_model = model
                    self.best_params = best_params
                    self.best_num_features = num_feature

    def save(self, path: Path) -> None:
        """Complete me
        """
        write_pickle(file=self.best_model, path=path)


def get_model(model_name: Text, params: Dict = None):
    """
    Get an object of a model

    :param model_name: The model name
    :param params: hyper parameters

    :return: An object of a model
    """
    try:
        if params != None:
            model = eval(model_name+'(**params)')
        else:
            model = eval(model_name+'()')
    except ValueError as error:
        Log.error(error)
    return model


def select_k_feature(
    data_df: pd.DataFrame,
    ranked_features_list: List,
    num_feature: int,
) -> pd.DataFrame:
    """Complete me
    """
    return data_df[ranked_features_list[:num_feature]]
