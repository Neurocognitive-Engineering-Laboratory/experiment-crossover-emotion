"""
Linear regression models.
"""

from __future__ import annotations

import pandas as pd
import statsmodels.formula.api as smf

from .utils import extract_coefficients


def fit_linear_model(
    data: pd.DataFrame,
    formula: str,
    *,
    robust_se: bool = False,
):
    """
    Fit an ordinary least-squares regression model.

    Example
    -------
    fit_linear_model(
        data=df,
        formula="Reaction_Time ~ C(Emotion) + C(NBack_Level)"
    )
    """

    model = smf.ols(
        formula=formula,
        data=data,
    )

    result = model.fit()

    if robust_se:
        result = result.get_robustcov_results(
            cov_type="HC3"
        )

    return result


def linear_model_table(
    result,
) -> pd.DataFrame:
    """
    Return coefficients from an OLS model.
    """

    return extract_coefficients(result)