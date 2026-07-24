"""
Moderation model utilities.
"""

from __future__ import annotations

import pandas as pd
import statsmodels.formula.api as smf

from .utils import extract_coefficients


def fit_moderation(
    data: pd.DataFrame,
    outcome: str,
    predictor: str,
    moderator: str,
    *,
    covariates: list[str] | None = None,
    center: bool = True,
):
    """
    Fit a linear moderation model.

    Y ~ X * Moderator + Covariates
    """

    df = data.copy()

    predictor_model = predictor
    moderator_model = moderator

    if center:

        predictor_model = f"{predictor}_c"
        moderator_model = f"{moderator}_c"

        df[predictor_model] = (
            df[predictor]
            - df[predictor].mean()
        )

        df[moderator_model] = (
            df[moderator]
            - df[moderator].mean()
        )

    formula = (
        f"{outcome} ~ "
        f"{predictor_model} * "
        f"{moderator_model}"
    )

    if covariates:

        formula += " + " + " + ".join(
            covariates
        )

    model = smf.ols(
        formula=formula,
        data=df,
    )

    result = model.fit()

    return result, df


def moderation_table(
    result,
) -> pd.DataFrame:
    """
    Return moderation coefficients.
    """

    return extract_coefficients(result)