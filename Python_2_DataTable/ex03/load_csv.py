#!/usr/bin/env python3

import pandas as pd
import sys
import os


def _check_path(path: str) -> None:
    """
    check path
    """
    if not isinstance(path, str):
        raise ValueError("path must be a string")
    if not path:
        raise ValueError("path is empty")
    if not os.path.isfile(path):
        raise FileNotFoundError(f"no such file: {path}")
    if not path.endswith(".csv"):
        raise ValueError(f"{path} is not CSV file")


def load(path: str) -> pd.DataFrame | None:
    """
    return PD_Dataflame
    if error Return Null
    """
    try:
        _check_path(path)
        df = pd.read_csv(path)
    except (OSError, ValueError, pd.errors.ParserError) as e:
        print(f"Error: {e}", file=sys.stderr)
        return None
    print(f"Loading dataset of dimensions {df.shape}")
    return df
