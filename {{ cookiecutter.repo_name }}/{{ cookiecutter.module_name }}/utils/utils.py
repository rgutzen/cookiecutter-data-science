from pathlib import Path

import numpy as np
import pandas as pd

types_int = ['id', 'index']
types_float = []
types_bool = []

dtypes = dict.fromkeys(types_int, int) \
    | dict.fromkeys(types_float, float) \
    | dict.fromkeys(types_bool, bool)


def load_df(path, dtypes=dtypes):
    df = pd.read_csv(path, dtype=dtypes)
    df.drop(df.columns[df.columns.str.contains('unnamed', case=False)],
            axis=1, inplace=True)
    return df