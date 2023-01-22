from sklearn import datasets
from pathlib import Path
import os
import pandas as pd
from typing import Dict, List, Text


iris_dataset = datasets.load_iris()
X = iris_dataset.data
y = iris_dataset.target
y_df = pd.DataFrame(y, columns=['target'])
X_df = pd.DataFrame(X, columns=iris_dataset.feature_names)
iris_dataset_df = pd.concat([X_df, y_df], axis=1, join='inner')
