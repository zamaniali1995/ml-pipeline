"""Complete me
"""
from typing import Text

import pandas as pd


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
