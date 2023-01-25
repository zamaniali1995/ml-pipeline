"""
This file contains all utility functions used in the src directory
"""
import logging
import os
import pickle
from argparse import ArgumentParser, Namespace
from pathlib import Path
from typing import Dict, List, Text

import pandas as pd
import structlog
import yaml
from munch import DefaultMunch
from yaml import dump

struct_logger = structlog.getLogger(__name__)
logging.basicConfig(
    filename='log.log',
    encoding='utf-8',
    level=logging.DEBUG,
    format='%(asctime)s %(message)s',
    datefmt='%m/%d/%Y %I:%M:%S %p'
)


def write_parquet(df: pd.DataFrame, path: Path, engine: Text = 'pyarrow'):
    """
    Converts a pd.DataFrame object into a parquet file that is saved

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame to be saved as a parquet file
    path : Path
        Path to save the parquet file
    engine : Text, optional
        Engine method used to convert the DataFrame to the parquet file, by default 'pyarrow'
    """
    dir = Path(os.path.split(path)[0])
    dir.mkdir(parents=True, exist_ok=True)
    df.to_parquet(path=path, engine=engine)


def parse_arguments(arguments_list: List) -> Namespace:
    """
    Parse arguments using the ArgumentParser library 

    Parameters
    ----------
    arguments_list : List
        List of arguments to be parsed

    Returns
    -------
    Namespace
        Parsed arguments from the input argument list
    """
    parser = ArgumentParser('Parse config path.')
    parser.add_argument(
        '--config_path',
        type=Path,
        help='Path to the config path.'
    )
    parser.add_argument(
        '--main_config_path',
        type=Path,
        help='Path to the main config path.'
    )
    return parser.parse_args(arguments_list)


def load_yaml(path: Path) -> any:
    """
    Reads a .yaml file and converts it from a dictionary structure to an easy
        to use Object structure. (Instead of dict... Object.item.subitem)

    Parameters
    ----------
    path : Path
        Path to the .yaml file

    Returns
    -------
    any
        Returns a 'Munch' Object to interpret the dictionary structure of the .yaml file 
    """
    with open(path, 'r') as stream:
        try:
            yaml_obj = DefaultMunch.fromDict(yaml.safe_load(stream))
        except yaml.YAMLError as exc:
            Log.error(msg=exc)
    return yaml_obj


def write_yaml(file: Dict, path: Path):
    """
    Saves a dictionary object as a .yaml file

    Parameters
    ----------
    file : Dict
        Dictionary to be saved as a .yaml file
    path : Path
        Path to save the .yaml file
    """
    with Path(path).open(mode='w') as stream:
        dump(file, stream)


def load_parquet(path: Path, engine='pyarrow') -> pd.DataFrame:
    """
    Loads a parquet file into a usable pd.DataFrame object

    Parameters
    ----------
    path : Path
        Path to the stored parquet file to be read
    engine : str, optional
        method of reading the parquet file and converting it to a pd.DataFrame, by default 'pyarrow'

    Returns
    -------
    pd.DataFrame
        DataFrame that was generated from the parquet file
    """
    return pd.read_parquet(path, engine=engine)


def write_pickle(file, path: Path):
    """
    Saves an object to a pickle binary file

    Parameters
    ----------
    file : any
        The object to be saved as a pickle binary file
    path : Path
        Path to save and write the pickle file to
    """
    dir = Path(os.path.split(Path(path))[0])
    dir.mkdir(parents=True, exist_ok=True)
    with open(Path(path), 'wb') as handle:
        pickle.dump(file, handle)


def load_pickle(path: Path):
    """
    Loads a pickle file as an object

    Parameters
    ----------
    path : Path
        Path to read and open the pickle file from

    Returns
    -------
    any
        Returns the object that was loaded from the pickle file
    """
    with open(Path(path), 'rb') as f:
        pickle_file = pickle.load(f)
    return pickle_file


class Log():
    """
    A Log class to control the recording of different terminal outputs during runtime
    """

    def error(msg: Text) -> None:
        """Logs an input error message with the logger module

        Parameters
        ----------
        msg : Text
            Input message with the recorded error
        """
        struct_logger.error(msg)
        logging.error(msg=msg)

    def info(msg: Text) -> None:
        """Logs an input info message with the logger module

        Parameters
        ----------
        msg : Text
            Input message with the recorded info
        """
        struct_logger.info(msg)
        logging.info(msg=msg)
