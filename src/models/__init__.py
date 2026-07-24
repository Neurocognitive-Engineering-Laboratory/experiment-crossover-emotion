"""
Statistical modeling API for the project.
"""

from .linear import (
    fit_linear_model,
    linear_model_table,
)

from .mixed import (
    fit_mixed_model,
    mixed_model_table,
)

from .binary import (
    fit_binary_gee,
    binary_model_table,
)

from .moderation import (
    fit_moderation,
    moderation_table,
)

from .mediation import (
    fit_mediation,
)

from .diagnostics import (
    residual_diagnostics,
    model_information,
)

__all__ = [
    "fit_linear_model",
    "linear_model_table",
    "fit_mixed_model",
    "mixed_model_table",
    "fit_binary_gee",
    "binary_model_table",
    "fit_moderation",
    "moderation_table",
    "fit_mediation",
    "residual_diagnostics",
    "model_information",
]