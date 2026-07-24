"""
Models for binary repeated-measures outcomes.

Designed primarily for trial-level accuracy data.
"""

from __future__ import annotations

import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.genmod.cov_struct import (
    Exchangeable,
    Independence,
)

from .utils import extract_coefficients


def fit_binary_gee(
    data: pd.DataFrame,
    formula: str,
    subject: str,
    *,
    correlation: str = "exchangeable",
):
    """
    Fit a binomial Generalized Estimating Equation.

    Outcome must generally be coded:
        0 = incorrect
        1 = correct

    Parameters
    ----------
    correlation:
        "exchangeable" or "independence"
    """

    structures = {
        "exchangeable": Exchangeable(),
        "independence": Independence(),
    }

    if correlation not in structures:
        raise ValueError(
            "correlation must be "
            "'exchangeable' or 'independence'"
        )

    model = smf.gee(
        formula=formula,
        groups=subject,
        data=data,
        family=sm.families.Binomial(),
        cov_struct=structures[correlation],
    )

    return model.fit()


def binary_model_table(
    result,
) -> pd.DataFrame:
    """
    Extract logistic GEE coefficients and odds ratios.
    """

    table = extract_coefficients(result)

    table["odds_ratio"] = (
        table["estimate"]
        .apply(lambda value: float(
            __import__("numpy").exp(value)
        ))
    )

    table["or_ci_low"] = (
        table["ci_low"]
        .apply(lambda value: float(
            __import__("numpy").exp(value)
        ))
    )

    table["or_ci_high"] = (
        table["ci_high"]
        .apply(lambda value: float(
            __import__("numpy").exp(value)
        ))
    )

    return table