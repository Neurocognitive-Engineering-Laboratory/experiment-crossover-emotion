"""
Base class for hypothesis-specific report generators.
"""

from __future__ import annotations

from abc import (
    ABC,
    abstractmethod,
)
from pathlib import Path

import pandas as pd

from .report_builder import (
    ReportContent,
    ScientificReportBuilder,
)

from .report_utils import (
    load_csv_tables,
)


class BaseHypothesisReport(
    ABC
):
    """
    Base class for all hypothesis reports.

    Subclasses define:
        - input result files;
        - title and hypothesis;
        - report-specific interpretation;
        - report tables.
    """

    report_number: int

    title: str

    subtitle: str = (
        "Confirmatory Hypothesis Report"
    )

    output_filename: str

    input_files: dict[
        str,
        Path,
    ]

    def __init__(
        self,
        *,
        output_directory: (
            str | Path
        ),
    ) -> None:

        self.output_directory = Path(
            output_directory
        )

        self.output_directory.mkdir(
            parents=True,
            exist_ok=True,
        )

        self.results: dict[
            str,
            pd.DataFrame
        ] = {}

    # ------------------------------------------------------------------
    # DATA
    # ------------------------------------------------------------------

    def load_results(
        self,
    ) -> dict[str, pd.DataFrame]:
        """
        Load CSV result tables.
        """

        self.results = (
            load_csv_tables(
                self.input_files
            )
        )

        return self.results

    # ------------------------------------------------------------------
    # REPORT DEFINITION
    # ------------------------------------------------------------------

    @abstractmethod
    def build_content(
        self,
    ) -> ReportContent:
        """
        Build hypothesis-specific report content.
        """

        raise NotImplementedError

    # ------------------------------------------------------------------
    # GENERATION
    # ------------------------------------------------------------------

    def generate(
        self,
    ) -> tuple[Path, Path]:
        """
        Generate both DOCX and PDF reports.
        """

        if not self.results:

            self.load_results()

        content = (
            self.build_content()
        )

        builder = (
            ScientificReportBuilder(
                content
            )
        )

        docx_path = (
            self.output_directory
            / f"{self.output_filename}.docx"
        )

        pdf_path = (
            self.output_directory
            / f"{self.output_filename}.pdf"
        )

        builder.build_docx(
            docx_path
        )

        builder.build_pdf(
            pdf_path
        )

        return (
            docx_path,
            pdf_path,
        )