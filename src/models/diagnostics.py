"""
Statistical model diagnostics.
"""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats


def residual_diagnostics(
    result,
    *,
    show: bool = True,
):
    """
    Basic residual diagnostics for linear-type models.
    """

    residuals = np.asarray(result.resid)

    fitted = np.asarray(
        result.fittedvalues
    )

    # Residuals vs fitted
    fig1, ax1 = plt.subplots()

    ax1.scatter(
        fitted,
        residuals,
        alpha=0.6,
    )

    ax1.axhline(
        0,
        linestyle="--",
    )

    ax1.set_xlabel("Fitted values")
    ax1.set_ylabel("Residuals")
    ax1.set_title(
        "Residuals vs Fitted"
    )

    fig1.tight_layout()

    # Q-Q plot
    fig2, ax2 = plt.subplots()

    stats.probplot(
        residuals,
        dist="norm",
        plot=ax2,
    )

    ax2.set_title(
        "Normal Q-Q Plot"
    )

    fig2.tight_layout()

    if show:
        plt.show()

    return (fig1, ax1), (fig2, ax2)


def model_information(result) -> dict:
    """
    Extract common model-fit statistics when available.
    """

    attributes = [
        "aic",
        "bic",
        "llf",
        "nobs",
    ]

    output = {}

    for attribute in attributes:

        if hasattr(result, attribute):

            try:
                output[attribute] = float(
                    getattr(result, attribute)
                )

            except (TypeError, ValueError):
                pass

    return output