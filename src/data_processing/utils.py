"""Complete me
"""
import pandas as pd
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
