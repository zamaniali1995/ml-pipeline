"""
This file should contain all required utility functions for the data acquisition step
"""
from typing import List, Text

import pandas as pd
from sklearn import datasets


def load_data(target_column: Text) -> pd.DataFrame:
    """Loads data from the iris database into panda dataframes

    Parameters
    ----------
    target_column : Text
        The name of the column that is the target of prediction 

    Returns
    -------
    pd.DataFrame
        Dataframe containing all of the data with the target column at the very end
    """
    iris_dataset = datasets.load_iris()
    X = iris_dataset.data
    y = iris_dataset.target
    y_df = pd.DataFrame(y, columns=[target_column])
    X_df = pd.DataFrame(X, columns=iris_dataset.feature_names)
    iris_dataset_df = pd.concat([X_df, y_df], axis=1, join='inner')
    return iris_dataset_df