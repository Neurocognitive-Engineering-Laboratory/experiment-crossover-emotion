"""
Scoring utilities for questionnaires and experimental tasks.

Scoring rules should be documented in docs/04_variables_and_outcomes.md
and modified here only when justified by the study protocol.
"""

from __future__ import annotations

from collections.abc import Iterable

import numpy as np
import pandas as pd

from .preprocessing import validate_columns

from .config import (
    SAM_MIN,
    SAM_MAX,
    ERQ_MIN,
    ERQ_MAX,
)

# ---------------------------------------------------------------------
# Generic Likert scoring
# ---------------------------------------------------------------------

def reverse_score(
    series: pd.Series,
    *,
    minimum: float,
    maximum: float,
) -> pd.Series:
    """
    Reverse-score a Likert item.

    Formula
    -------
    reversed = minimum + maximum - observed

    Example
    -------
    For a 1-4 scale:
        1 -> 4
        2 -> 3
        3 -> 2
        4 -> 1
    """

    values = pd.to_numeric(
        series,
        errors="coerce",
    )

    return (
        minimum
        + maximum
        - values
    )


def score_items(
    data: pd.DataFrame,
    items: list[str],
    *,
    reverse_items: Iterable[str] | None = None,
    minimum: float = 1,
    maximum: float = 4,
    method: str = "mean",
    min_valid_items: int | None = None,
) -> pd.Series:
    """
    Calculate a questionnaire score from multiple items.
    """

    validate_columns(
        data,
        items,
    )

    df = data[
        items
    ].apply(
        pd.to_numeric,
        errors="coerce",
    )

    reverse_items = set(
        reverse_items or []
    )

    invalid_reverse = (
        reverse_items
        - set(items)
    )

    if invalid_reverse:
        raise ValueError(
            "Reverse-scored items not present "
            f"in items: {invalid_reverse}"
        )

    for item in reverse_items:

        df[item] = reverse_score(
            df[item],
            minimum=minimum,
            maximum=maximum,
        )

    if min_valid_items is None:
        min_valid_items = len(items)

    valid_count = df.notna().sum(axis=1)

    if method == "mean":

        result = df.mean(
            axis=1,
            skipna=True,
        )

    elif method == "sum":

        result = df.sum(
            axis=1,
            skipna=True,
        )

    else:
        raise ValueError(
            "method must be 'mean' or 'sum'."
        )

    result[
        valid_count < min_valid_items
    ] = np.nan

    return result


# ---------------------------------------------------------------------
# State / Trait score
# ---------------------------------------------------------------------

def score_six_item_state_trait(
    data: pd.DataFrame,
    direct_items: list[str],
    reverse_items: list[str],
    *,
    output_column: str,
    minimum: float = 1,
    maximum: float = 4,
    min_valid_items: int = 6,
) -> pd.DataFrame:
    """
    Score the six-item mood/anxiety measure described in the protocol.

    Three items are direct and three are reverse scored.
    Final score is the average across items.
    """

    items = (
        direct_items
        + reverse_items
    )

    if len(items) != 6:
        raise ValueError(
            "Exactly six items are expected."
        )

    df = data.copy()

    df[output_column] = score_items(
        data=df,
        items=items,
        reverse_items=reverse_items,
        minimum=minimum,
        maximum=maximum,
        method="mean",
        min_valid_items=min_valid_items,
    )

    return df


# ---------------------------------------------------------------------
# ERQ
# ---------------------------------------------------------------------

def score_erq(
    data: pd.DataFrame,
    *,
    reappraisal_items: list[str],
    suppression_items: list[str],
    output_reappraisal: str = "cognitive_reappraisal",
    output_suppression: str = "expressive_suppression",
) -> pd.DataFrame:
    """
    Calculate ERQ subscale scores.

    The expected original ERQ structure is:
    - Cognitive Reappraisal: 6 items
    - Expressive Suppression: 4 items

    Scores are summed by default to preserve the ranges described
    in the protocol:
    - Reappraisal: 6-42
    - Suppression: 4-28

    This assumes items are scored from 1 to 7.
    """

    if len(reappraisal_items) != 6:
        raise ValueError(
            "Cognitive Reappraisal should contain 6 items."
        )

    if len(suppression_items) != 4:
        raise ValueError(
            "Expressive Suppression should contain 4 items."
        )

    df = data.copy()

    df[output_reappraisal] = score_items(
        data,
        reappraisal_items,
        minimum=ERQ_MIN,
        maximum=ERQ_MAX,
        method="sum",
        min_valid_items=6,
    )

    df[output_suppression] = score_items(
        data,
        suppression_items,
        minimum=ERQ_MIN,
        maximum=ERQ_MAX,
        method="sum",
        min_valid_items=4,
    )

    return df


# ---------------------------------------------------------------------
# SAM
# ---------------------------------------------------------------------

def score_sam(
    data: pd.DataFrame,
    *,
    valence: str,
    arousal: str,
    dominance: str,
    prefix: str = "sam",
) -> pd.DataFrame:
    """
    Standardize SAM dimensions as numeric scores.

    SAM scores are expected on a 1-9 scale.
    """

    validate_columns(
        data,
        [
            valence,
            arousal,
            dominance,
        ],
    )

    df = data.copy()

    variables = {
        valence: f"{prefix}_valence",
        arousal: f"{prefix}_arousal",
        dominance: f"{prefix}_dominance",
    }

    for source, target in variables.items():

        score = pd.to_numeric(
            df[source],
            errors="coerce",
        )

        score = score.where(
            score.between(
                SAM_MIN,
                SAM_MAX,
            )
        )

        df[target] = score

    return df


def calculate_change_score(
    data: pd.DataFrame,
    pre: str,
    post: str,
    *,
    output_column: str,
) -> pd.DataFrame:
    """
    Calculate post - pre change score.

    Positive values indicate increase from baseline.
    """

    validate_columns(
        data,
        [pre, post],
    )

    df = data.copy()

    df[output_column] = (
        pd.to_numeric(
            df[post],
            errors="coerce",
        )
        -
        pd.to_numeric(
            df[pre],
            errors="coerce",
        )
    )

    return df


# ---------------------------------------------------------------------
# N-back scoring
# ---------------------------------------------------------------------

def score_nback_block(
    data: pd.DataFrame,
    *,
    correct_column: str = "correct",
    rt_column: str = "reaction_time",
    response_column: str | None = None,
) -> dict[str, float]:
    """
    Calculate performance metrics for one n-back block.

    Reaction-time statistics are calculated only for correct
    responses.
    """

    validate_columns(
        data,
        [
            correct_column,
            rt_column,
        ],
    )

    df = data.copy()

    correct = pd.to_numeric(
        df[correct_column],
        errors="coerce",
    )

    rt = pd.to_numeric(
        df[rt_column],
        errors="coerce",
    )

    n_trials = len(df)

    correct_count = int(
        (correct == 1).sum()
    )

    incorrect_count = int(
        (correct == 0).sum()
    )

    if response_column is not None:

        validate_columns(
            df,
            [response_column],
        )

        no_response_count = int(
            df[response_column]
            .isna()
            .sum()
        )

    else:

        no_response_count = int(
            correct.isna().sum()
        )

    accuracy = (
        correct_count / n_trials
        if n_trials > 0
        else np.nan
    )

    correct_rt = rt[
        correct == 1
    ].dropna()

    return {
        "n_trials": n_trials,
        "correct_count": correct_count,
        "incorrect_count": incorrect_count,
        "no_response_count": no_response_count,
        "accuracy": accuracy,
        "rt_mean_correct": correct_rt.mean(),
        "rt_sd_correct": correct_rt.std(ddof=1),
        "rt_median_correct": correct_rt.median(),
    }


def aggregate_nback(
    data: pd.DataFrame,
    group_columns: list[str],
    *,
    correct_column: str = "correct",
    rt_column: str = "reaction_time",
) -> pd.DataFrame:
    """
    Aggregate trial-level n-back data.

    Typical grouping:
        participant_id
        session
        emotion
        nback_moment
        nback_level
    """

    validate_columns(
        data,
        group_columns
        + [
            correct_column,
            rt_column,
        ],
    )

    records = []

    for keys, group in data.groupby(
        group_columns,
        dropna=False,
        observed=True,
    ):

        if not isinstance(keys, tuple):
            keys = (keys,)

        record = dict(
            zip(
                group_columns,
                keys,
            )
        )

        record.update(
            score_nback_block(
                group,
                correct_column=correct_column,
                rt_column=rt_column,
            )
        )

        records.append(record)

    return pd.DataFrame(records)


# ---------------------------------------------------------------------
# Reaction-time training scores
# ---------------------------------------------------------------------

def score_motor_delay(
    data: pd.DataFrame,
    *,
    rt_column: str,
    hand_column: str,
    participant_column: str,
    session_column: str | None = None,
) -> pd.DataFrame:
    """
    Calculate mean and SD of motor reaction time by hand.

    Expected hand values might include:
        Right
        Left
    """

    columns = [
        participant_column,
        hand_column,
        rt_column,
    ]

    if session_column:
        columns.append(
            session_column
        )

    validate_columns(
        data,
        columns,
    )

    group_columns = [
        participant_column,
    ]

    if session_column:
        group_columns.append(
            session_column
        )

    group_columns.append(
        hand_column
    )

    result = (
        data.groupby(
            group_columns,
            observed=True,
        )[rt_column]
        .agg(
            motor_rt_mean="mean",
            motor_rt_sd="std",
            motor_rt_n="count",
        )
        .reset_index()
    )

    return result


# ---------------------------------------------------------------------
# Speed-accuracy summary
# ---------------------------------------------------------------------

def inverse_efficiency_score(
    accuracy: pd.Series,
    reaction_time: pd.Series,
) -> pd.Series:
    """
    Calculate Inverse Efficiency Score (IES).

    IES = mean reaction time / proportion correct

    Higher values indicate worse combined speed-accuracy performance.

    This should be treated as a secondary descriptive metric rather
    than a replacement for separate RT and accuracy models.
    """

    accuracy = pd.to_numeric(
        accuracy,
        errors="coerce",
    )

    reaction_time = pd.to_numeric(
        reaction_time,
        errors="coerce",
    )

    valid_accuracy = accuracy.where(
        accuracy > 0
    )

    return (
        reaction_time
        / valid_accuracy
    )