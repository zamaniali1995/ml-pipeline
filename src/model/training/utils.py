"""Complete me
"""
from typing import Dict, List, Text

import pandas as pd
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.ensemble import AdaBoostClassifier, RandomForestClassifier
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.inspection import DecisionBoundaryDisplay
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

from src.model.utils import split_train_target
from src.utils import Log


class Model():
    """Model evaluation
    """

    def __init__(
        self,
        models: List,
        candidate_params: Dict,
    ) -> None:
        """Complete me
        """
        self.models_name = models
        self.candidate_params = candidate_params

    def select(
        self,
        train_data_df: pd.DataFrame
    ) -> None:
        """Complete me
        """
        for model_name in self.models_name:
            Log.info('Training '+model_name+' model ...')
            model = get_model(model_name=model_name)
            X_train_df, y_train_df = split_train_target(
                data_df=train_data_df,
                target_column='target',
            )
            model.fit(X_train_df, y_train_df)
            for num_feature in self.candidate_params.get('num_features'):
                Log.info(
                    'Number of features: '+str(num_feature)
                )

    def save(self) -> None:
        """Complete me
        """
        print('save')


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
        print(error)
        # logger.error(error)
    return model
