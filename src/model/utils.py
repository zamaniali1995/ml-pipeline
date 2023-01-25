"""Complete me
"""
from statistics import mean
from typing import Dict, List, Text

import pandas as pd
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.ensemble import AdaBoostClassifier, RandomForestClassifier
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.inspection import DecisionBoundaryDisplay
from sklearn.model_selection import GridSearchCV, cross_val_score
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

from src.utils import Log


def split_train_target(
    data_df: pd.DataFrame,
    target_column: Text
) -> tuple([pd.DataFrame, pd.DataFrame]):
    """
    Separate train and target

    :param data_df: Data
    :param target_column: Column to use as target

    :return X_df: Train and target dataframe
    :return y_df: Target dataframe
    """
    X_df = data_df.drop(target_column, axis=1)
    y_df = data_df[target_column]
    return X_df, y_df


def tune_hyperparameter(
    model,
    X_df: pd.DataFrame,
    y_df: pd.DataFrame,
    candidate_params: Dict,
    num_folds=5,
):
    """Complete me
    """
    # create a grid search object
    gs = GridSearchCV(model, candidate_params,
                      scoring='accuracy', cv=num_folds)
    # fit model using grid search
    gs = gs.fit(X_df, y_df)

    best_model = gs.best_estimator_
    best_params = best_model.get_params()
    best_model = best_model.fit(X_df, y_df)

    return best_params, best_model


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


def evaluate_model(
    model,
    X_df: pd.DataFrame,
    y_df: pd.DataFrame,
    num_folds: int = 5,
) -> pd.DataFrame:
    """Complete me
    """
    metric_df = pd.DataFrame()
    scores_list = cross_val_score(
        model,
        X_df,
        y_df,
        cv=num_folds,
        scoring='accuracy'
    )
    metric_df = pd.DataFrame({
        'accuracy': [mean(scores_list)]
    })

    return metric_df


def select_k_feature(
    data_df: pd.DataFrame,
    ranked_features_list: List,
    num_feature: int,
) -> pd.DataFrame:
    """Complete me
    """
    return data_df[ranked_features_list[:num_feature]]
