"""
General utilities for scientific report generation.

This module contains formatting, validation, path, and result-extraction
helpers shared by all hypothesis reports.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any, Mapping

import numpy as np
import pandas as pd


# ======================================================================
# PATH UTILITIES
# ======================================================================

def ensure_directory(
    path: str | Path,
) -> Path:
    """
    Create a directory if it does not exist.
    """

    directory = Path(path)

    directory.mkdir(
        parents=True,
        exist_ok=True,
    )

    return directory


def validate_files(
    files: Mapping[str, Path],
) -> None:
    """
    Validate that all expected report input files exist.
    """

    missing = [
        path
        for path in files.values()
        if not path.exists()
    ]

    if missing:

        message = "\n".join(
            f"- {path}"
            for path in missing
        )

        raise FileNotFoundError(
            "Required report files were not found:\n"
            f"{message}"
        )


def load_csv_tables(
    files: Mapping[str, Path],
) -> dict[str, pd.DataFrame]:
    """
    Load multiple CSV result files into a dictionary.
    """

    validate_files(files)

    return {
        name: pd.read_csv(path)
        for name, path in files.items()
    }


# ======================================================================
# SAFE VALUE EXTRACTION
# ======================================================================

def first_value(
    data: pd.DataFrame,
    column: str,
    default: Any = np.nan,
) -> Any:
    """
    Safely retrieve the first value from a dataframe column.
    """

    if data.empty:
        return default

    if column not in data.columns:
        return default

    return data[column].iloc[0]


def get_condition_row(
    data: pd.DataFrame,
    condition: str,
) -> pd.Series:
    """
    Retrieve a descriptive-statistics row for a condition.

    Supported condition-column names include:
        emotion_condition
        condition
        Condition
    """

    candidate_columns = [
        "emotion_condition",
        "condition",
        "Condition",
    ]

    condition_column = next(
        (
            column
            for column in candidate_columns
            if column in data.columns
        ),
        None,
    )

    if condition_column is None:

        raise KeyError(
            "No condition column was found."
        )

    mask = (
        data[condition_column]
        .astype(str)
        .str.strip()
        .str.lower()
        == condition.strip().lower()
    )

    subset = data.loc[mask]

    if subset.empty:

        raise ValueError(
            f"Condition '{condition}' "
            "was not found in the table."
        )

    return subset.iloc[0]


def find_model_contrast(
    data: pd.DataFrame,
    keyword: str,
) -> pd.Series:
    """
    Find a model-result row using a term or contrast keyword.
    """

    candidate_columns = [
        "term",
        "contrast",
        "Contrast",
    ]

    for column in candidate_columns:

        if column not in data.columns:
            continue

        mask = (
            data[column]
            .astype(str)
            .str.contains(
                keyword,
                case=False,
                regex=False,
            )
        )

        if mask.any():
            return data.loc[mask].iloc[0]

    if len(data) == 1:
        return data.iloc[0]

    raise ValueError(
        f"Could not identify contrast containing "
        f"'{keyword}'."
    )


# ======================================================================
# NUMERIC FORMATTING
# ======================================================================

def format_number(
    value: Any,
    digits: int = 3,
    missing: str = "NA",
) -> str:
    """
    Format numeric results for reports.
    """

    try:
        number = float(value)

    except (TypeError, ValueError):
        return str(value)

    if np.isnan(number):
        return missing

    return f"{number:.{digits}f}"


def format_p_value(
    value: Any,
    threshold: float = 0.001,
) -> str:
    """
    Format p-values using scientific-report conventions.

    Examples
    --------
    0.0002 -> "< .001"
    0.0213 -> "= .021"
    """

    try:
        p = float(value)

    except (TypeError, ValueError):
        return str(value)

    if np.isnan(p):
        return "NA"

    if p < threshold:
        return "< .001"

    return f"= {p:.3f}".replace(
        "0.",
        ".",
    )


def format_percent(
    value: Any,
    digits: int = 1,
    *,
    proportion: bool = True,
) -> str:
    """
    Format proportions or percentages.

    Parameters
    ----------
    proportion:
        If True, 0.85 becomes 85.0%.
        If False, -23.4 becomes -23.4%.
    """

    try:
        number = float(value)

    except (TypeError, ValueError):
        return str(value)

    if np.isnan(number):
        return "NA"

    if proportion:
        number *= 100

    return f"{number:.{digits}f}%"


def format_ci(
    lower: Any,
    upper: Any,
    digits: int = 2,
) -> str:
    """
    Format a confidence interval.
    """

    return (
        "["
        f"{format_number(lower, digits)}, "
        f"{format_number(upper, digits)}"
        "]"
    )


# ======================================================================
# MODEL TRANSFORMATIONS
# ======================================================================

def odds_ratio(
    beta: float,
) -> float:
    """
    Convert a log-odds coefficient into an odds ratio.
    """

    return float(
        np.exp(beta)
    )


def log_effect_to_percent(
    beta: float,
) -> float:
    """
    Convert a log-scale coefficient to percentage change.

    Formula:
        100 * (exp(beta) - 1)
    """

    return float(
        (
            np.exp(beta)
            - 1
        )
        * 100
    )


def log_ci_to_percent(
    lower: float,
    upper: float,
) -> tuple[float, float]:
    """
    Convert log-scale confidence interval limits to percentages.
    """

    return (
        log_effect_to_percent(lower),
        log_effect_to_percent(upper),
    )