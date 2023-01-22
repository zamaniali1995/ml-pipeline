"""
Complete me
"""
import os
from pathlib import Path
from typing import Text

import pandas as pd


def write_parquet(df: pd.DataFrame, path: Path, engine: Text = 'pyarrow'):
    """Complete me
    """
    dir = Path(os.path.split(path)[0])
    dir.mkdir(parents=True, exist_ok=True)
    df.to_parquet(path=path, engine=engine)
