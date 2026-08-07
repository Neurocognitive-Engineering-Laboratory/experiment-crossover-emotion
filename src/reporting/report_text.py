"""
Reusable scientific-report text helpers.
"""

from __future__ import annotations

from .report_utils import (
    format_p_value,
)


def significance_statement(
    p_value: float,
) -> str:
    """
    Return a textual significance statement.
    """

    if p_value < 0.05:

        return (
            "The effect was statistically significant "
            f"(p {format_p_value(p_value)})."
        )

    return (
        "The effect was not statistically significant "
        f"(p {format_p_value(p_value)})."
    )


def accuracy_direction(
    odds_ratio: float,
) -> str:
    """
    Describe the direction of an odds-ratio effect.
    """

    if odds_ratio > 1:

        return (
            "higher odds of a correct response"
        )

    if odds_ratio < 1:

        return (
            "lower odds of a correct response"
        )

    return (
        "no change in the odds of "
        "a correct response"
    )


def rt_direction(
    percent_change: float,
) -> str:
    """
    Describe reaction-time direction.
    """

    if percent_change < 0:

        return "faster responses"

    if percent_change > 0:

        return "slower responses"

    return "no reaction-time difference"


def performance_direction(
    accuracy_change: float,
    rt_change: float,
) -> str:
    """
    Provide a high-level speed-accuracy description.
    """

    accuracy_better = (
        accuracy_change > 0
    )

    accuracy_worse = (
        accuracy_change < 0
    )

    rt_faster = (
        rt_change < 0
    )

    rt_slower = (
        rt_change > 0
    )

    if accuracy_better and rt_faster:

        return (
            "faster and more accurate performance"
        )

    if accuracy_worse and rt_slower:

        return (
            "slower and less accurate performance"
        )

    if accuracy_worse and rt_faster:

        return (
            "faster but less accurate performance"
        )

    if accuracy_better and rt_slower:

        return (
            "slower but more accurate performance"
        )

    return (
        "no clear combined performance pattern"
    )