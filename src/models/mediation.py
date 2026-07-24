"""
Bootstrap mediation analyses.

Initial implementation for continuous outcomes.
"""

from __future__ import annotations

import pandas as pd
import pingouin as pg

from ..config import (
    N_BOOTSTRAP,
    BOOTSTRAP_SEED,
)


def fit_mediation(
    data: pd.DataFrame,
    predictor: str,
    mediator: str | list[str],
    outcome: str,
    *,
    covariates: str | list[str] | None = None,
    n_boot: int = N_BOOTSTRAP,
    alpha: float = 0.05,
    seed: int = BOOTSTRAP_SEED,
) -> pd.DataFrame:
    """
    Perform bootstrap mediation analysis.

    Parameters
    ----------
    predictor:
        Exposure/predictor variable.

    mediator:
        Mediator or parallel mediators.

    outcome:
        Continuous outcome.

    covariates:
        Optional adjustment variables.

    n_boot:
        Number of bootstrap samples.
    """

    result = pg.mediation_analysis(
        data=data,
        x=predictor,
        m=mediator,
        y=outcome,
        covar=covariates,
        alpha=alpha,
        n_boot=n_boot,
        seed=seed,
    )

    return result