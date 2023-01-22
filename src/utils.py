"""
Complete me
"""
import os
from argparse import ArgumentParser, Namespace
from pathlib import Path
from typing import List, Text

import pandas as pd
import yaml
from yaml.loader import SafeLoader


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
