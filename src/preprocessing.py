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
# Reshaping SAM valence
# ---------------------------------------------------------------------

def reshape_sam_valence(
    data: pd.DataFrame,
    participant_column: str,
) -> pd.DataFrame:
    """
    Convert SAM valence measurements from wide to long format.
    """

    sam_columns = [
        column
        for column in data.columns
        if column.startswith("sam_neg_")
        or column.startswith("sam_pos_")
    ]

    long = data.melt(
        id_vars=[participant_column],
        value_vars=sam_columns,
        var_name="sam_measure",
        value_name="sam_valence",
    )

    long["emotion"] = np.where(
        long["sam_measure"].str.contains(
            "_neg_"
        ),
        "Negative",
        "Positive",
    )

    long["timepoint"] = (
        long["sam_measure"]
        .str.extract(
            r"_v(.+?)_mean"
        )[0]
    )

    long["sam_valence"] = pd.to_numeric(
        long["sam_valence"],
        errors="coerce",
    )

    return long


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

# ======================================================================
# COLUMN STANDARDIZATION
# ======================================================================

def standardize_column_names(
    data: pd.DataFrame,
) -> pd.DataFrame:
    """
    Standardize dataframe column names to snake_case.
    """

    df = data.copy()

    def clean_column_name(column: str) -> str:
        column = str(column).strip()
        column = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", column)
        column = column.replace(".", "_")
        column = column.replace("-", "_")
        column = column.replace(" ", "_")
        column = re.sub(r"_+", "_", column)

        return column.lower().strip("_")

    df.columns = [
        clean_column_name(column)
        for column in df.columns
    ]

    return df


# ======================================================================
# MISSING VALUES
# ======================================================================

def normalize_missing_values(
    data: pd.DataFrame,
) -> pd.DataFrame:
    """
    Convert common textual missing-value representations to NaN.
    """

    df = data.copy()

    missing_values = [
        "",
        " ",
        "  ",
        "NA",
        "N/A",
        "na",
        "n/a",
        "NaN",
        "nan",
        "None",
        "null",
        "NULL",
    ]

    df = df.replace(
        missing_values,
        np.nan,
    )

    return df


# ======================================================================
# PARTICIPANT IDENTIFIER
# ======================================================================

def standardize_participant_id(
    data: pd.DataFrame,
    source_column: str = "participant_name",
) -> pd.DataFrame:
    """
    Rename the participant identifier and standardize its type.
    """

    df = data.copy()

    if source_column not in df.columns:
        raise ValueError(
            f"Column '{source_column}' not found."
        )

    if source_column != "participant_id":
        df = df.rename(
            columns={
                source_column: "participant_id"
            }
        )

    df["participant_id"] = pd.to_numeric(
        df["participant_id"],
        errors="coerce",
    ).astype("Int64")

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
    
    
    
def reshape_sam_valence(
    data: pd.DataFrame,
    participant_column: str,
) -> pd.DataFrame:
    """
    Convert SAM valence measurements from wide to long format.
    """

    sam_columns = [
        column
        for column in data.columns
        if column.startswith("sam_neg_")
        or column.startswith("sam_pos_")
    ]

    long = data.melt(
        id_vars=[participant_column],
        value_vars=sam_columns,
        var_name="sam_measure",
        value_name="sam_valence",
    )

    long["emotion"] = np.where(
        long["sam_measure"].str.contains(
            "_neg_"
        ),
        "Negative",
        "Positive",
    )

    long["timepoint"] = (
        long["sam_measure"]
        .str.extract(
            r"_v(.+?)_mean"
        )[0]
    )

    long["sam_valence"] = pd.to_numeric(
        long["sam_valence"],
        errors="coerce",
    )

    return long


# ---------------------------------------------------------------------
# Preprocessing SAM/questionnaire data
# ---------------------------------------------------------------------

def preprocess_sam(
    data: pd.DataFrame,
) -> pd.DataFrame:
    """
    Clean and standardize the participant-level SAM/questionnaire dataset.
    """

    df = data.copy()

    # --------------------------------------------------------------
    # Standardize structure
    # --------------------------------------------------------------

    df = standardize_column_names(df)
    df = normalize_missing_values(df)

    df = standardize_participant_id(
        df,
        source_column="participant_name",
    )

    # --------------------------------------------------------------
    # Numeric columns
    # --------------------------------------------------------------

    numeric_columns = [
        column
        for column in df.columns
        if (
            column.startswith("sam_")
            or column.startswith("result_state")
            or column.startswith("traite_result")
            or column in {
                "age",
                "cog_reap",
                "ex_sup",
                "order",
                "group_id",
                "sex",
            }
        )
    ]

    for column in numeric_columns:

        df[column] = pd.to_numeric(
            df[column],
            errors="coerce",
        )

    # --------------------------------------------------------------
    # Explicit categorical columns
    # --------------------------------------------------------------

    df["group_id"] = (
        df["group_id"]
        .astype("Int64")
    )

    df["order"] = (
        df["order"]
        .astype("Int64")
    )

    df["sex"] = (
        df["sex"]
        .astype("Int64")
    )

    # --------------------------------------------------------------
    # Duplicate participant check
    # --------------------------------------------------------------

    if df["participant_id"].duplicated().any():

        duplicated_ids = (
            df.loc[
                df["participant_id"].duplicated(
                    keep=False
                ),
                "participant_id",
            ]
            .unique()
            .tolist()
        )

        raise ValueError(
            "Duplicated participant IDs found "
            f"in SAM dataset: {duplicated_ids}"
        )

    return df


# ---------------------------------------------------------------------
# Preprocessing nback trial-level data
# ---------------------------------------------------------------------

def repair_nback_response_columns(
    data: pd.DataFrame,
) -> pd.DataFrame:
    """
    Repair datasets in which Correct_Response and
    R_Reaction_Time were inconsistently exported.

    The numeric value is interpreted as reaction time.
    The non-numeric value is interpreted as the correct-response code.
    """

    df = data.copy()

    required_columns = {
        "correct_response",
        "r_reaction_time",
    }

    missing = (
        required_columns
        - set(df.columns)
    )

    if missing:
        raise ValueError(
            "Missing required columns: "
            f"{sorted(missing)}"
        )

    correct_numeric = pd.to_numeric(
        df["correct_response"],
        errors="coerce",
    )

    rt_numeric = pd.to_numeric(
        df["r_reaction_time"],
        errors="coerce",
    )

    # --------------------------------------------------------------
    # Reconstruct reaction time
    # --------------------------------------------------------------

    df["reaction_time_ms"] = (
        rt_numeric.combine_first(
            correct_numeric
        )
    )

    # --------------------------------------------------------------
    # Reconstruct expected response/key
    # --------------------------------------------------------------

    correct_is_numeric = (
        correct_numeric.notna()
    )

    df["correct_response_clean"] = np.where(
        correct_is_numeric,
        df["r_reaction_time"],
        df["correct_response"],
    )

    df["correct_response_clean"] = (
        df["correct_response_clean"]
        .astype("string")
        .str.strip()
    )

    return df


# ---------------------------------------------------------------------
# Preprocessing nback
# ---------------------------------------------------------------------

def preprocess_nback(
    data: pd.DataFrame,
) -> pd.DataFrame:
    """
    Clean and standardize trial-level n-back data.
    """

    df = data.copy()

    # --------------------------------------------------------------
    # Basic normalization
    # --------------------------------------------------------------

    df = standardize_column_names(df)
    df = normalize_missing_values(df)

    df = standardize_participant_id(
        df,
        source_column="participant_name",
    )

    # --------------------------------------------------------------
    # Repair exported RT / correct-response columns
    # --------------------------------------------------------------

    df = repair_nback_response_columns(
        df
    )

    # --------------------------------------------------------------
    # Normalize strings
    # --------------------------------------------------------------

    string_columns = [
        "participant_group",
        "session_id",
        "block_name",
        "trial_name",
        "event_name",
        "participant_response",
        "key",
        "pressed_or_released",
        "error_code",
        "cr",
    ]

    for column in string_columns:

        if column in df.columns:

            df[column] = (
                df[column]
                .astype("string")
                .str.strip()
            )

    # --------------------------------------------------------------
    # Numeric variables
    # --------------------------------------------------------------

    numeric_columns = [
        "order",
        "cumulative_time",
        "reaction_time_ms",
    ]

    for column in numeric_columns:

        if column in df.columns:

            df[column] = pd.to_numeric(
                df[column],
                errors="coerce",
            )

    # --------------------------------------------------------------
    # Binary accuracy
    # --------------------------------------------------------------

    if "cr" in df.columns:

        df["accuracy"] = (
            df["cr"]
            .str.lower()
            .map(
                {
                    "correct": 1,
                    "incorrect": 0,
                    "not respond": 0,
                }
            )
            .astype("Int64")
        )

    return df


# ---------------------------------------------------------------------
# Preprocessing derivative nback variables
# ---------------------------------------------------------------------

def derive_nback_level(
    data: pd.DataFrame,
) -> pd.DataFrame:
    """
    Extract n-back level from trial_name.
    """

    df = data.copy()

    if "trial_name" not in df.columns:
        raise ValueError(
            "'trial_name' column not found."
        )

    df["nback_level"] = (
        df["trial_name"]
        .astype("string")
        .str.extract(
            r"n\s*=\s*(\d+)",
            expand=False,
        )
    )

    df["nback_level"] = pd.to_numeric(
        df["nback_level"],
        errors="coerce",
    ).astype("Int64")

    return df



def derive_session_number(
    data: pd.DataFrame,
) -> pd.DataFrame:
    """
    Convert session labels into ordered session numbers.
    """

    df = data.copy()

    mapping = {
        "1st": 1,
        "2nd": 2,
    }

    df["session_number"] = (
        df["session_id"]
        .map(mapping)
        .astype("Int64")
    )

    return df


# ---------------------------------------------------------------------
# Flag reaction times outside plausible range
# ---------------------------------------------------------------------

def flag_reaction_times(
    data: pd.DataFrame,
    minimum_ms: float = 100,
    maximum_ms: float = 5000,
) -> pd.DataFrame:
    """
    Flag reaction times outside plausible limits.
    Does not remove observations.
    """

    df = data.copy()

    rt = df["reaction_time_ms"]

    df["rt_too_fast"] = (
        rt < minimum_ms
    )

    df["rt_too_slow"] = (
        rt > maximum_ms
    )

    df["rt_valid"] = (
        rt.notna()
        & ~df["rt_too_fast"]
        & ~df["rt_too_slow"]
    )

    return df

# ---------------------------------------------------------------------
# Derive experimental sequence from group_id
# ---------------------------------------------------------------------

def derive_experimental_sequence(
    data: pd.DataFrame,
) -> pd.DataFrame:
    """
    Derive experimental category and sequence from group_id.
    """

    df = data.copy()

    category_map = {
        1: "I",
        2: "II",
        3: "III",
        4: "IV",
    }

    sequence_map = {
        1: "A_B",
        2: "B_A",
        3: "C_D",
        4: "D_C",
    }

    group_sequence_map = {
        1: "A to B",
        2: "B to A",
        3: "C to D",
        4: "D to C",
    }

    df["category"] = (
        df["group_id"]
        .map(category_map)
        .astype("string")
    )

    df["sequence"] = (
        df["group_id"]
        .map(sequence_map)
        .astype("string")
    )

    df["group_sequence"] = (
        df["group_id"]
        .map(group_sequence_map)
        .astype("string")
    )

    return df