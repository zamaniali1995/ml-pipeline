"""Complete me
"""
from typing import Dict, Text

import pandas as pd
from sklearn.model_selection import GridSearchCV, cross_val_score


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
