"""
The file should implement data acquisition pipeline.
It should load the raw data from any data source and save it.
"""
import pandas as pd
from sklearn import datasets


def load_data() -> pd.DataFrame:
    """Complete me"""
    iris_dataset = datasets.load_iris()
    X = iris_dataset.data
    y = iris_dataset.target
    y_df = pd.DataFrame(y, columns=['target'])
    X_df = pd.DataFrame(X, columns=iris_dataset.feature_names)
    iris_dataset_df = pd.concat([X_df, y_df], axis=1, join='inner')
    return iris_dataset_df


def run():
    """Run method"""
    dataset = load_data()


if __name__ == '__main__':
    run()
