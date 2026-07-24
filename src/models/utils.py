"""
Shared utilities for statistical models.
"""

from __future__ import annotations

from typing import Iterable

import numpy as np
import pandas as pd


def validate_columns(
    data: pd.DataFrame,
    columns: Iterable[str],
) -> None:
    """
    Check whether required columns are available.
    """

    columns = list(columns)

    missing = [
        column
        for column in columns
        if column not in data.columns
    ]

    if missing:
        raise ValueError(
            f"Missing required columns: {missing}"
        )


def remove_missing(
    data: pd.DataFrame,
    columns: Iterable[str],
) -> pd.DataFrame:
    """
    Return a dataframe containing complete cases
    for the requested variables.
    """

    columns = list(columns)

    validate_columns(
        data,
        columns,
    )

    return (
        data[columns]
        .replace([np.inf, -np.inf], np.nan)
        .dropna()
        .copy()
    )


def extract_coefficients(
    result,
) -> pd.DataFrame:
    """
    Convert a statsmodels result object into a tidy
    coefficient dataframe.
    """

    params = result.params
    conf = result.conf_int()

    output = pd.DataFrame(
        {
            "term": params.index,
            "estimate": params.values,
            "std_error": result.bse,
            "p_value": result.pvalues,
            "ci_low": conf.iloc[:, 0],
            "ci_high": conf.iloc[:, 1],
        }
    )

    return output.reset_index(drop=True)