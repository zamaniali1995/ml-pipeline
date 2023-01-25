"""
This file should contain all required utility functions for the data processing step
"""
from typing import Text

import pandas as pd
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.model_selection import train_test_split


def split_train_test(
    df: pd.DataFrame,
    test_size: float,
    random_state: int,
    shuffle: bool = True
) -> tuple([pd.DataFrame, pd.DataFrame]):
    """
    This function splits the total dataset into training and testing samples

    Parameters
    ----------
    df : pd.DataFrame
        Dataframe of the total dataset to be split into test / train
    
    test_size : float
        Value between 0-1 representing the percentage of data to use for the testing sample

    random_state : int
        Selected random seed to use for the RNG in the model

    shuffle : bool
        Whether to shuffle the data index or not, defaults to True.

    Returns
    -------
    tuple [pd.DataFrame, pd.DataFrame]
        Dataframes for both the training data and testing data
    """
    train_df, test_df = train_test_split(
        df,
        test_size=test_size,
        random_state=random_state,
        shuffle=shuffle
    )
    return train_df, test_df


def rank_features(
    df: pd.DataFrame,
    target_column: Text,
) -> pd.DataFrame:
    """
    Evaluates and ranks the input features using univariate feature regression

    Parameters
    ----------
    df : pd.DataFrame
        Input dataframe containing all features used
    target_column : Text
        Name of target value column that we want to predict

    Returns
    -------
    pd.DataFrame
        Dataframe of ranked selected features
    """
    features = list(df.drop(
        [target_column],
        axis=1,
        errors='ignore'
    ).columns)
    selected_k_best_feature = SelectKBest(f_regression, k='all').fit(
        df[features],
        df[target_column]
    )
    sorted_idx = (-selected_k_best_feature.scores_).argsort()
    df_selected_features = pd.DataFrame({
        'feature': df[features].columns[sorted_idx],
        'score': selected_k_best_feature.scores_[sorted_idx]
    })
    df_selected_features = df_selected_features.dropna()
    return df_selected_features
