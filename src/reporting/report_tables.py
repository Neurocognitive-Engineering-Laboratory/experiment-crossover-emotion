"""
Table rendering utilities for DOCX and PDF reports.
"""

from __future__ import annotations

from typing import Sequence

import pandas as pd

from docx import Document
from docx.enum.table import (
    WD_CELL_VERTICAL_ALIGNMENT,
    WD_TABLE_ALIGNMENT,
)

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    Paragraph,
    Table,
    TableStyle,
)


# ======================================================================
# DOCX
# ======================================================================

def add_docx_table(
    document: Document,
    dataframe: pd.DataFrame,
    *,
    style: str = "Table Grid",
) -> None:
    """
    Add a pandas dataframe as a DOCX table.
    """

    table = document.add_table(
        rows=1,
        cols=len(dataframe.columns),
    )

    table.style = style

    table.alignment = (
        WD_TABLE_ALIGNMENT.CENTER
    )

    # Header
    for index, column in enumerate(
        dataframe.columns
    ):

        cell = table.rows[0].cells[
            index
        ]

        cell.text = str(column)

        cell.vertical_alignment = (
            WD_CELL_VERTICAL_ALIGNMENT.CENTER
        )

        for run in (
            cell.paragraphs[0].runs
        ):
            run.bold = True

    # Body
    for _, row in dataframe.iterrows():

        cells = table.add_row().cells

        for index, value in enumerate(
            row
        ):

            cells[index].text = (
                "" if pd.isna(value)
                else str(value)
            )

            cells[
                index
            ].vertical_alignment = (
                WD_CELL_VERTICAL_ALIGNMENT.CENTER
            )


# ======================================================================
# PDF
# ======================================================================

def dataframe_to_pdf_table(
    dataframe: pd.DataFrame,
    *,
    column_widths: Sequence | None = None,
    font_size: float = 8,
) -> Table:
    """
    Convert a pandas dataframe into a ReportLab table.
    """

    styles = getSampleStyleSheet()

    body_style = styles[
        "BodyText"
    ]

    data = []

    # Header
    data.append(
        [
            Paragraph(
                f"<b>{column}</b>",
                body_style,
            )
            for column in dataframe.columns
        ]
    )

    # Rows
    for _, row in dataframe.iterrows():

        data.append(
            [
                Paragraph(
                    (
                        ""
                        if pd.isna(value)
                        else str(value)
                    ),
                    body_style,
                )
                for value in row
            ]
        )

    table = Table(
        data,
        colWidths=column_widths,
        repeatRows=1,
        hAlign="CENTER",
    )

    table.setStyle(
        TableStyle(
            [
                (
                    "BACKGROUND",
                    (0, 0),
                    (-1, 0),
                    colors.HexColor(
                        "#E6E6E6"
                    ),
                ),
                (
                    "TEXTCOLOR",
                    (0, 0),
                    (-1, 0),
                    colors.black,
                ),
                (
                    "GRID",
                    (0, 0),
                    (-1, -1),
                    0.5,
                    colors.grey,
                ),
                (
                    "VALIGN",
                    (0, 0),
                    (-1, -1),
                    "MIDDLE",
                ),
                (
                    "FONTSIZE",
                    (0, 0),
                    (-1, -1),
                    font_size,
                ),
                (
                    "LEFTPADDING",
                    (0, 0),
                    (-1, -1),
                    5,
                ),
                (
                    "RIGHTPADDING",
                    (0, 0),
                    (-1, -1),
                    5,
                ),
                (
                    "TOPPADDING",
                    (0, 0),
                    (-1, -1),
                    5,
                ),
                (
                    "BOTTOMPADDING",
                    (0, 0),
                    (-1, -1),
                    5,
                ),
            ]
        )
    )

    return table