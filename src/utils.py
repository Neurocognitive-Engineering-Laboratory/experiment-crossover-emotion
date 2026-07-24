"""
General-purpose project utilities.

Functions in this module should be reusable across preprocessing,
scoring, modeling and visualization.
"""

from __future__ import annotations

import os
import random
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

from src import config as cfg


def initialize_project() -> None:
    """
    Initialize reproducibility settings and output directories.
    """

    set_random_seed(
        cfg.RANDOM_SEED
    )

    directories = [
        cfg.INTERIM_DATA_DIR,
        cfg.PROCESSED_DATA_DIR,

        cfg.FIGURES_DESIGN_DIR,
        cfg.FIGURES_EXPLORATORY_DIR,
        cfg.FIGURES_MANIPULATION_DIR,
        cfg.FIGURES_NBACK_DIR,
        cfg.FIGURES_MEDIATION_DIR,
        cfg.FIGURES_MODELS_DIR,
        cfg.FIGURES_FINAL_DIR,

        cfg.REPORTS_TECHNICAL_DIR,
        cfg.TABLES_DIR,
        cfg.FINAL_REPORT_DIR,
    ]

    create_project_output_directories(
        directories
    )


def print_project_config() -> None:
    """
    Print the main project configuration.
    """

    print("Project configuration")
    print("=" * 60)

    print(
        f"Project:          {cfg.PROJECT_NAME}"
    )

    print(
        f"Project root:     {cfg.PROJECT_ROOT}"
    )

    print(
        f"Raw data:         {cfg.RAW_DATA_DIR}"
    )

    print(
        f"Processed data:   {cfg.PROCESSED_DATA_DIR}"
    )

    print(
        f"Figures:          {cfg.FIGURES_DIR}"
    )

    print("-" * 60)

    print(
        f"Random seed:      {cfg.RANDOM_SEED}"
    )

    print(
        f"Alpha:            {cfg.ALPHA}"
    )

    print(
        f"Confidence level: {cfg.CONFIDENCE_LEVEL}"
    )

    print(
        f"Bootstrap:        {cfg.N_BOOTSTRAP}"
    )

    print(
        f"RT range:         "
        f"{cfg.RT_MIN_MS}–{cfg.RT_MAX_MS} ms"
    )

    print(
        f"Figure DPI:       {cfg.FIGURE_DPI}"
    )

    print("=" * 60)
    

# =====================================================================
# REPRODUCIBILITY
# =====================================================================

def set_random_seed(
    seed: int = cfg.RANDOM_SEED,
) -> None:
    """
    Set random seeds used by Python and NumPy.

    Parameters
    ----------
    seed:
        Random seed used for reproducibility.

    Examples
    --------
    >>> set_random_seed(42)
    """

    random.seed(seed)

    np.random.seed(seed)

    os.environ["PYTHONHASHSEED"] = str(seed)


# =====================================================================
# DIRECTORIES
# =====================================================================

def ensure_directory(
    path: str | Path,
) -> Path:
    """
    Create a directory if it does not already exist.
    """

    directory = Path(path)

    directory.mkdir(
        parents=True,
        exist_ok=True,
    )

    return directory


def create_project_output_directories(
    directories: list[str | Path],
) -> None:
    """
    Create multiple project output directories.
    """

    for directory in directories:
        ensure_directory(directory)


# =====================================================================
# DATAFRAME VALIDATION
# =====================================================================

def validate_columns(
    data: pd.DataFrame,
    columns: list[str],
) -> None:
    """
    Check whether requested columns exist in a dataframe.
    """

    missing = [
        column
        for column in columns
        if column not in data.columns
    ]

    if missing:
        raise ValueError(
            f"Missing required columns: {missing}"
        )


def validate_not_empty(
    data: pd.DataFrame,
) -> None:
    """
    Check whether a dataframe contains observations.
    """

    if data.empty:
        raise ValueError(
            "The dataframe contains no observations."
        )


# =====================================================================
# VARIABLE INFORMATION
# =====================================================================

def dataframe_summary(
    data: pd.DataFrame,
) -> pd.DataFrame:
    """
    Generate a compact summary of dataframe variables.

    Returns
    -------
    DataFrame with:
        variable
        dtype
        n
        missing
        missing_percent
        unique
    """

    n_rows = len(data)

    summary = pd.DataFrame(
        {
            "variable": data.columns,
            "dtype": [
                str(dtype)
                for dtype in data.dtypes
            ],
            "n": [
                data[column].notna().sum()
                for column in data.columns
            ],
            "missing": [
                data[column].isna().sum()
                for column in data.columns
            ],
            "unique": [
                data[column].nunique(
                    dropna=True
                )
                for column in data.columns
            ],
        }
    )

    if n_rows > 0:

        summary["missing_percent"] = (
            summary["missing"]
            / n_rows
            * 100
        )

    else:

        summary["missing_percent"] = np.nan

    return summary[
        [
            "variable",
            "dtype",
            "n",
            "missing",
            "missing_percent",
            "unique",
        ]
    ]


# =====================================================================
# NUMERIC UTILITIES
# =====================================================================

def safe_numeric(
    series: pd.Series,
) -> pd.Series:
    """
    Convert values to numeric without raising conversion errors.
    """

    return pd.to_numeric(
        series,
        errors="coerce",
    )


def safe_divide(
    numerator: Any,
    denominator: Any,
) -> Any:
    """
    Divide values while avoiding division-by-zero errors.
    """

    with np.errstate(
        divide="ignore",
        invalid="ignore",
    ):

        result = np.divide(
            numerator,
            denominator,
        )

    if np.isscalar(result):

        if not np.isfinite(result):
            return np.nan

        return result

    result = np.asarray(
        result,
        dtype=float,
    )

    result[
        ~np.isfinite(result)
    ] = np.nan

    return result


# =====================================================================
# FILE NAMING
# =====================================================================

def sanitize_filename(
    name: str,
) -> str:
    """
    Convert text into a safe filename.
    """

    name = name.strip().lower()

    replacements = {
        " ": "_",
        "-": "_",
        "/": "_",
        "\\": "_",
        ":": "_",
    }

    for old, new in replacements.items():
        name = name.replace(
            old,
            new,
        )

    while "__" in name:
        name = name.replace(
            "__",
            "_",
        )

    return name.strip("_")


def build_figure_path(
    directory: str | Path,
    name: str,
    *,
    extension: str = cfg.FIGURE_FORMAT,
) -> Path:
    """
    Build a standardized figure output path.
    """

    directory = ensure_directory(
        directory
    )

    filename = (
        f"{sanitize_filename(name)}."
        f"{extension.lstrip('.')}"
    )

    return directory / filename


# =====================================================================
# RESULTS EXPORT
# =====================================================================

def save_table(
    data: pd.DataFrame,
    path: str | Path,
    *,
    index: bool = False,
) -> Path:
    """
    Save a dataframe according to the output file extension.

    Supported:
        CSV
        XLSX
    """

    path = Path(path)

    ensure_directory(
        path.parent
    )

    extension = (
        path.suffix
        .lower()
    )

    if extension == ".csv":

        data.to_csv(
            path,
            index=index,
        )

    elif extension == ".xlsx":

        data.to_excel(
            path,
            index=index,
        )

    else:

        raise ValueError(
            "Supported formats are .csv and .xlsx"
        )

    return path


# =====================================================================
# MODEL RESULTS
# =====================================================================

def model_to_dataframe(
    result,
) -> pd.DataFrame:
    """
    Convert common statsmodels result objects into a tidy table.
    """

    params = result.params

    confidence = result.conf_int()

    table = pd.DataFrame(
        {
            "term": params.index,
            "estimate": params.values,
            "std_error": np.asarray(
                result.bse
            ),
            "p_value": np.asarray(
                result.pvalues
            ),
            "ci_low": confidence.iloc[:, 0].values,
            "ci_high": confidence.iloc[:, 1].values,
        }
    )

    return table