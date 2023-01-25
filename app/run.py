"""Complete me
"""
from typing import List

import pandas as pd
from flask import Flask, render_template, request

from src.utils import load_parquet, load_pickle, load_yaml, parse_arguments

app = Flask(__name__)


def main(arguments_list: List = None) -> None:
    """Complete me
    """
    arguments = parse_arguments(arguments_list=arguments_list)
    main_config = load_yaml(arguments.main_config_path)
    model_config = load_yaml(path=main_config.path.config_model_path)
    ranked_features_df = load_parquet(
        path=main_config.path.feature_score_path
    )
    model = load_pickle(path=main_config.path.trained_model_path)
    return model, list(ranked_features_df[:model_config.num_features]['feature'])

# web page that handles user query and displays model results


@app.route('/go')
def go():
    """Complete me
    """
    # save user input in query
    classes_dict = {
        0: 'Iris Setosa',
        1: 'Iris Versicolour',
        2: 'Iris Virginica'
    }
    sepal_len = request.args.get('sepal_len', '')
    sepal_wid = request.args.get('sepal_wid', '')
    petal_len = request.args.get('petal_len', '')
    petal_wid = request.args.get('petal_wid', '')
    query = pd.DataFrame({
        'sepal length (cm)': [sepal_len],
        'sepal width (cm)': [sepal_wid],
        'petal length (cm)': [petal_len],
        'petal width (cm)': [petal_wid],
    })
    model, k_features = main()
    predict_class = model.predict(query[k_features])[0]
    return render_template(
        'go.html',
        classification_result=classes_dict[predict_class],
    )


@app.route('/')
@app.route('/index')
def index():
    """Complete me
    """
    return render_template('master.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3001, debug=True)
