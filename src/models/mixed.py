"""
Linear mixed-effects models for repeated-measures
and crossover data.
"""

from __future__ import annotations

import pandas as pd
import statsmodels.formula.api as smf

from .utils import extract_coefficients

from ..config import (
    MIXED_MODEL_METHOD,
    DEFAULT_RANDOM_EFFECT,
)


def fit_mixed_model(
    data: pd.DataFrame,
    formula: str,
    subject: str,
    *,
    re_formula: str = DEFAULT_RANDOM_EFFECT,
    method: str = MIXED_MODEL_METHOD,
):
    """
    Fit a linear mixed-effects model.

    Parameters
    ----------
    data:
        Long-format dataframe.

    formula:
        Fixed-effects model formula.

    subject:
        Participant identifier.

    re_formula:
        Random-effects specification.
        Default "1" = random intercept.

    method:
        Optimization method.

    Example
    -------
    model = fit_mixed_model(
        data=df,
        formula=(
            "Reaction_Time ~ "
            "C(Emotion) * C(NBack_Level)"
        ),
        subject="Participant_ID",
    )
    """

    model = smf.mixedlm(
        formula=formula,
        data=data,
        groups=data[subject],
        re_formula=re_formula,
    )

    result = model.fit(
        method=method,
        reml=False,
    )

    return result


def mixed_model_table(
    result,
) -> pd.DataFrame:
    """
    Return fixed and random-effect estimates.
    """

    return extract_coefficients(result)