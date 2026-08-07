"""
Visual styles for DOCX and PDF scientific reports.
"""

from __future__ import annotations

from docx import Document
from docx.shared import Pt

from reportlab.lib.enums import (
    TA_CENTER,
    TA_JUSTIFY,
)
from reportlab.lib.styles import (
    ParagraphStyle,
    getSampleStyleSheet,
)


# ======================================================================
# DOCX
# ======================================================================

def configure_docx_styles(
    document: Document,
) -> None:
    """
    Apply the standard report style to a DOCX document.
    """

    styles = document.styles

    normal = styles["Normal"]

    normal.font.name = "Arial"
    normal.font.size = Pt(10.5)

    title = styles["Title"]

    title.font.name = "Arial"
    title.font.size = Pt(18)
    title.font.bold = True

    heading1 = styles["Heading 1"]

    heading1.font.name = "Arial"
    heading1.font.size = Pt(14)
    heading1.font.bold = True

    heading2 = styles["Heading 2"]

    heading2.font.name = "Arial"
    heading2.font.size = Pt(12)
    heading2.font.bold = True

    heading3 = styles["Heading 3"]

    heading3.font.name = "Arial"
    heading3.font.size = Pt(11)
    heading3.font.bold = True


# ======================================================================
# PDF
# ======================================================================

def create_pdf_styles() -> dict[str, ParagraphStyle]:
    """
    Create reusable ReportLab paragraph styles.
    """

    styles = getSampleStyleSheet()

    return {
        "title": ParagraphStyle(
            "ReportTitle",
            parent=styles["Title"],
            fontName="Helvetica-Bold",
            fontSize=17,
            leading=21,
            alignment=TA_CENTER,
            spaceAfter=12,
        ),

        "subtitle": ParagraphStyle(
            "ReportSubtitle",
            parent=styles["Normal"],
            fontName="Helvetica",
            fontSize=10,
            leading=13,
            alignment=TA_CENTER,
            spaceAfter=16,
        ),

        "heading1": ParagraphStyle(
            "ReportHeading1",
            parent=styles["Heading1"],
            fontName="Helvetica-Bold",
            fontSize=13,
            leading=16,
            spaceBefore=10,
            spaceAfter=6,
        ),

        "heading2": ParagraphStyle(
            "ReportHeading2",
            parent=styles["Heading2"],
            fontName="Helvetica-Bold",
            fontSize=11,
            leading=14,
            spaceBefore=8,
            spaceAfter=5,
        ),

        "heading3": ParagraphStyle(
            "ReportHeading3",
            parent=styles["Heading3"],
            fontName="Helvetica-Bold",
            fontSize=10,
            leading=13,
            spaceBefore=6,
            spaceAfter=4,
        ),

        "body": ParagraphStyle(
            "ReportBody",
            parent=styles["BodyText"],
            fontName="Helvetica",
            fontSize=9.5,
            leading=14,
            alignment=TA_JUSTIFY,
            spaceAfter=8,
        ),

        "bullet": ParagraphStyle(
            "ReportBullet",
            parent=styles["BodyText"],
            fontName="Helvetica",
            fontSize=9.5,
            leading=14,
            leftIndent=12,
            firstLineIndent=-7,
            spaceAfter=5,
        ),

        "caption": ParagraphStyle(
            "TableCaption",
            parent=styles["BodyText"],
            fontName="Helvetica",
            fontSize=8.5,
            leading=11,
            spaceBefore=6,
            spaceAfter=5,
        ),
    }