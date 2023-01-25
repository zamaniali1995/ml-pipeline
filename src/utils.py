"""
Complete me
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
    """Complete me
    """
    dir = Path(os.path.split(path)[0])
    dir.mkdir(parents=True, exist_ok=True)
    df.to_parquet(path=path, engine=engine)


def parse_arguments(arguments_list: List) -> Namespace:
    """Complete me
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


def load_yaml(path: Path) -> Dict:
    """Complete me
    """
    with open(path, 'r') as stream:
        try:
            yaml_obj = DefaultMunch.fromDict(yaml.safe_load(stream))
        except yaml.YAMLError as exc:
            Log.error(exc)
    return yaml_obj


def write_yaml(file: Dict, path: Path):
    """Complete me
    """
    with Path(path).open(mode='w') as stream:
        dump(file, stream)


def load_parquet(path: Path, engine='pyarrow') -> pd.DataFrame:
    """Complete me
    """
    return pd.read_parquet(path, engine=engine)


def write_pickle(file, path: Path):
    """
    COMPLETE THIS

    """
    dir = Path(os.path.split(path)[0])
    dir.mkdir(parents=True, exist_ok=True)
    with open(path, 'wb') as handle:
        pickle.dump(file, handle)


class Log():
    """Complete me
    """

    def error(self, msg: Text) -> None:
        """Logs an input error message with the logger module

        :param Text msg: input message with the recorded error
        """
        struct_logger.error(msg)
        logging.error(msg=msg)

    def info(msg: Text) -> None:
        """Logs an input info message with the logger module

        :param Text msg: input message with the recorded info
        """
        struct_logger.info(msg)
        logging.info(msg=msg)
