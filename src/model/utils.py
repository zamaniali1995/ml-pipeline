"""
This file contains all utility functions for both the model training and evaluation
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
    Separate the target column out from the training data

    Parameters
    ----------
    data_df : pd.DataFrame
        DataFrame containing data to be separated/split

    Returns
    -------
    tuple [pd.DataFrame, pd.DataFrame]
        DataFrames of the training data and the target data
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
    """
    Selects the best hyper parameters for a given input model using GridSearch

    Parameters
    ----------
    model : Object
        Typically an scikit-learn model or similar which requires hyper-parameter tuning
    X_df : pd.DataFrame
        DataFrame of the training data
    y_df : pd.DataFrame
        DataFrame containing the target data
    candidate_params : Dict
        Dictionary of possible hyperparameter ranges to search through
    num_folds : int, optional
        The number of folds to use during model evaluation, by default 5

    Returns
    -------
    tuple
        Contains the best parameters and a model trained on those best parameters
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
    """Create a model object

    Parameters
    ----------
    model_name : Text
        The name of the model
    params : Dict, optional
        Hyper parameters for the given model, by default None

    Returns
    -------
    Model
        A mode object with the specific name and hyper parameters
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
    """
    Evaluates the model performance using an accuracy scoring

    Parameters
    ----------
    model : Object
        Model to be evaluated
    X_df : pd.DataFrame
        DataFrame of data without the target information
    y_df : pd.DataFrame
        DataFrame with the target data column 
    num_folds : int, optional
        The number of folds to use during model evaluation, by default 5

    Returns
    -------
    pd.DataFrame
        DataFrame containing the performance metrics of the model
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
    """
    Selects the top 'k' features from the total dataset

    Parameters
    ----------
    data_df : pd.DataFrame
        DataFrame of the total dataset
    ranked_features_list : List
        List of the top ranked features 
    num_feature : int
        Number of features to select in the dataset

    Returns
    -------
    pd.DataFrame
        DataFrame of the top ranked features
    """
    return data_df[ranked_features_list[:num_feature]]
