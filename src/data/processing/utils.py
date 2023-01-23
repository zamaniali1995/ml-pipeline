"""Complete me
"""
from typing import List, Text

import pandas as pd
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.model_selection import train_test_split


def split_train_test(
    df: pd.DataFrame,
    test_size: float,
    random_state: int,
    shuffle: bool = True,
) -> tuple([pd.DataFrame, pd.DataFrame]):
    """Complete me
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
    ignore_column: List
) -> pd.DataFrame:
    """Evaluates and ranks the input features using univariate feature regression

    :param pd.DataFrame df: input dataframe containing all features used
    :param Text target_column: name of target value column that we want to predict
    :param List ignore_column: names of any columns to be ignored
    :return pd.DataFrame: dataframe of ranked selected features
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
