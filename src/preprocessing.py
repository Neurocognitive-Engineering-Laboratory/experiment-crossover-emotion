"""
Data preprocessing utilities for the crossover emotion experiment.

This module contains deterministic transformations applied before
statistical scoring and modeling.

Raw data should never be modified in place.
"""

from __future__ import annotations

import re
from collections.abc import Iterable

import numpy as np
import pandas as pd

from .config import (
    RT_MIN_MS,
    RT_MAX_MS,
)


# ---------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------

def validate_columns(
    data: pd.DataFrame,
    columns: Iterable[str],
) -> None:
    """
    Check whether all required columns are available.
    """

    required = list(columns)

    missing = [
        column
        for column in required
        if column not in data.columns
    ]

    if missing:
        raise ValueError(
            f"Missing required columns: {missing}"
        )


# ---------------------------------------------------------------------
# Column names
# ---------------------------------------------------------------------

def clean_column_name(name: str) -> str:
    """
    Convert a column name into snake_case.

    Examples
    --------
    'Participant ID' -> 'participant_id'
    'SAM-Valence Pre' -> 'sam_valence_pre'
    """

    name = str(name).strip()

    name = re.sub(
        r"([a-z0-9])([A-Z])",
        r"\1_\2",
        name,
    )

    name = re.sub(
        r"[^A-Za-z0-9]+",
        "_",
        name,
    )

    name = re.sub(
        r"_+",
        "_",
        name,
    )

    return name.strip("_").lower()


def standardize_column_names(
    data: pd.DataFrame,
) -> pd.DataFrame:
    """
    Return dataframe with standardized snake_case names.
    """

    df = data.copy()

    df.columns = [
        clean_column_name(column)
        for column in df.columns
    ]

    return df


# ---------------------------------------------------------------------
# Missing data
# ---------------------------------------------------------------------

DEFAULT_MISSING_VALUES = {
    "",
    " ",
    "NA",
    "N/A",
    "na",
    "n/a",
    "null",
    "NULL",
    "None",
    "none",
    "-",
    "--",
}


def normalize_missing_values(
    data: pd.DataFrame,
    missing_values: Iterable | None = None,
) -> pd.DataFrame:
    """
    Replace common textual missing-value codes with NaN.
    """

    df = data.copy()

    values = (
        set(missing_values)
        if missing_values is not None
        else DEFAULT_MISSING_VALUES
    )

    return df.replace(
        list(values),
        np.nan,
    )


# ---------------------------------------------------------------------
# Duplicates
# ---------------------------------------------------------------------

def find_duplicates(
    data: pd.DataFrame,
    subset: list[str],
) -> pd.DataFrame:
    """
    Return duplicated observations using selected identifiers.
    """

    validate_columns(
        data,
        subset,
    )

    mask = data.duplicated(
        subset=subset,
        keep=False,
    )

    return (
        data.loc[mask]
        .sort_values(subset)
        .copy()
    )


def remove_exact_duplicates(
    data: pd.DataFrame,
) -> pd.DataFrame:
    """
    Remove fully duplicated rows.
    """

    return (
        data
        .drop_duplicates()
        .reset_index(drop=True)
        .copy()
    )


# ---------------------------------------------------------------------
# Numeric conversion
# ---------------------------------------------------------------------

def convert_to_numeric(
    data: pd.DataFrame,
    columns: Iterable[str],
) -> pd.DataFrame:
    """
    Convert specified columns to numeric values.

    Invalid values are converted to NaN.
    """

    df = data.copy()

    validate_columns(
        df,
        columns,
    )

    for column in columns:
        df[column] = pd.to_numeric(
            df[column],
            errors="coerce",
        )

    return df


# ---------------------------------------------------------------------
# Categorical variables
# ---------------------------------------------------------------------

def standardize_emotion_condition(
    data: pd.DataFrame,
    column: str = "emotion",
) -> pd.DataFrame:
    """
    Standardize emotional-condition labels.
    """

    validate_columns(
        data,
        [column],
    )

    df = data.copy()

    mapping = {
        "positive": "Positive",
        "pos": "Positive",
        "positive emotion": "Positive",

        "negative": "Negative",
        "neg": "Negative",
        "negative emotion": "Negative",

        "neutral": "Neutral",
        "neu": "Neutral",
        "neutral emotion": "Neutral",
    }

    normalized = (
        df[column]
        .astype("string")
        .str.strip()
        .str.lower()
    )

    df[column] = normalized.map(
        mapping
    ).fillna(df[column])

    return df


def derive_group_information(
    data: pd.DataFrame,
    group_column: str = "group",
) -> pd.DataFrame:
    """
    Derive emotion and intervention order from Groups A-D.

    A = Positive, autobiography first
    B = Negative, autobiography first
    C = Positive, emotion induction first
    D = Negative, emotion induction first
    """

    validate_columns(
        data,
        [group_column],
    )

    df = data.copy()

    group = (
        df[group_column]
        .astype("string")
        .str.strip()
        .str.upper()
    )

    emotion_map = {
        "A": "Positive",
        "B": "Negative",
        "C": "Positive",
        "D": "Negative",
    }

    order_map = {
        "A": "Autobiography_First",
        "B": "Autobiography_First",
        "C": "Emotion_Induction_First",
        "D": "Emotion_Induction_First",
    }

    df["emotion"] = group.map(
        emotion_map
    )

    df["intervention_order"] = group.map(
        order_map
    )

    return df


def derive_sequence_information(
    data: pd.DataFrame,
    category_column: str = "category",
) -> pd.DataFrame:
    """
    Convert experimental Categories I-IV into crossover sequences.
    """

    validate_columns(
        data,
        [category_column],
    )

    df = data.copy()

    category = (
        df[category_column]
        .astype("string")
        .str.strip()
        .str.upper()
    )

    sequence_map = {
        "I": "A_B",
        "II": "B_A",
        "III": "C_D",
        "IV": "D_C",
    }

    df["sequence"] = category.map(
        sequence_map
    )

    return df


# ---------------------------------------------------------------------
# Reaction-time preprocessing
# ---------------------------------------------------------------------

def filter_reaction_times(
    data: pd.DataFrame,
    rt_column: str,
    *,
    min_rt: float | None = RT_MIN_MS,
    max_rt: float | None = RT_MAX_MS,
) -> pd.DataFrame:
    """
    Mark implausible reaction times as missing.

    Thresholds are configurable because final limits should be
    justified in the Statistical Analysis Plan.

    Units are assumed to be milliseconds.
    """

    validate_columns(
        data,
        [rt_column],
    )

    df = data.copy()

    df[rt_column] = pd.to_numeric(
        df[rt_column],
        errors="coerce",
    )

    if min_rt is not None:
        df.loc[
            df[rt_column] < min_rt,
            rt_column,
        ] = np.nan

    if max_rt is not None:
        df.loc[
            df[rt_column] > max_rt,
            rt_column,
        ] = np.nan

    return df


def calibrate_reaction_time(
    data: pd.DataFrame,
    rt_column: str,
    motor_delay_column: str,
    *,
    keyboard_delay_column: str | None = None,
    output_column: str = "calibrated_rt",
) -> pd.DataFrame:
    """
    Adjust observed reaction time for individual motor delay and,
    optionally, keyboard latency.

    calibrated_rt =
        observed_rt - motor_delay - keyboard_delay
    """

    columns = [
        rt_column,
        motor_delay_column,
    ]

    if keyboard_delay_column is not None:
        columns.append(
            keyboard_delay_column
        )

    validate_columns(
        data,
        columns,
    )

    df = data.copy()

    observed = pd.to_numeric(
        df[rt_column],
        errors="coerce",
    )

    motor = pd.to_numeric(
        df[motor_delay_column],
        errors="coerce",
    )

    calibrated = observed - motor

    if keyboard_delay_column is not None:

        keyboard = pd.to_numeric(
            df[keyboard_delay_column],
            errors="coerce",
        )

        calibrated = calibrated - keyboard

    df[output_column] = calibrated

    return df


# ---------------------------------------------------------------------
# Long-format conversion
# ---------------------------------------------------------------------

def wide_to_long(
    data: pd.DataFrame,
    id_columns: list[str],
    value_columns: list[str],
    *,
    variable_name: str = "measure",
    value_name: str = "value",
) -> pd.DataFrame:
    """
    Generic wide-to-long conversion.
    """

    validate_columns(
        data,
        id_columns + value_columns,
    )

    return (
        data.melt(
            id_vars=id_columns,
            value_vars=value_columns,
            var_name=variable_name,
            value_name=value_name,
        )
        .reset_index(drop=True)
    )


# ---------------------------------------------------------------------
# N-back
# ---------------------------------------------------------------------

def prepare_nback_trials(
    data: pd.DataFrame,
    *,
    correct_column: str,
    rt_column: str,
    response_column: str | None = None,
) -> pd.DataFrame:
    """
    Standardize trial-level n-back variables.

    Correct values are converted to 0/1 where possible.
    """

    columns = [
        correct_column,
        rt_column,
    ]

    if response_column:
        columns.append(response_column)

    validate_columns(
        data,
        columns,
    )

    df = data.copy()

    mapping = {
        True: 1,
        False: 0,
        "correct": 1,
        "incorrect": 0,
        "right": 1,
        "wrong": 0,
        "1": 1,
        "0": 0,
        1: 1,
        0: 0,
    }

    normalized = (
        df[correct_column]
        .astype("string")
        .str.strip()
        .str.lower()
    )

    df["correct"] = (
        normalized
        .map(mapping)
    )

    numeric = pd.to_numeric(
        df[correct_column],
        errors="coerce",
    )

    df["correct"] = (
        df["correct"]
        .fillna(numeric)
    )

    df[rt_column] = pd.to_numeric(
        df[rt_column],
        errors="coerce",
    )

    return df


# ---------------------------------------------------------------------
# Dataset integrity
# ---------------------------------------------------------------------

def check_session_counts(
    data: pd.DataFrame,
    participant: str,
    session: str,
    *,
    expected_sessions: int = 2,
) -> pd.DataFrame:
    """
    Identify participants without the expected number of sessions.
    """

    validate_columns(
        data,
        [participant, session],
    )

    counts = (
        data.groupby(participant)[session]
        .nunique()
        .rename("n_sessions")
        .reset_index()
    )

    return counts.loc[
        counts["n_sessions"]
        != expected_sessions
    ].copy()