"""
Scientific reporting API.
"""

from .report_builder import (
    ReportContent,
    ReportSection,
    ReportSubsection,
    ReportTable,
    ScientificReportBuilder,
)

from .report_generator import (
    BaseHypothesisReport,
)

from .report_utils import (
    format_number,
    format_p_value,
    format_percent,
    format_ci,
    odds_ratio,
    log_effect_to_percent,
)

__all__ = [
    "ReportContent",
    "ReportSection",
    "ReportSubsection",
    "ReportTable",
    "ScientificReportBuilder",
    "BaseHypothesisReport",
    "format_number",
    "format_p_value",
    "format_percent",
    "format_ci",
    "odds_ratio",
    "log_effect_to_percent",
]