import pandas as pd

from src.reporting import (
    ReportContent,
    ReportSection,
    ReportSubsection,
    ReportTable,
    ScientificReportBuilder,
)


accuracy = pd.DataFrame(
    {
        "Condition": [
            "Neutral",
            "Positive",
        ],
        "Accuracy": [
            "85.0%",
            "85.1%",
        ],
    }
)


content = ReportContent(
    title="Reporting Infrastructure Test",
    subtitle="Scientific Report Test",
    hypothesis=(
        "This is a test hypothesis."
    ),
    sections=[
        ReportSection(
            title="Method",
            paragraphs=[
                (
                    "This section verifies that the "
                    "generic scientific-report "
                    "infrastructure is working."
                )
            ],
        ),

        ReportSection(
            title="Results",
            subsections=[
                ReportSubsection(
                    title="Accuracy",
                    paragraphs=[
                        (
                            "Accuracy was similar "
                            "between conditions."
                        )
                    ],
                    tables=[
                        ReportTable(
                            caption=(
                                "Table 1. "
                                "Accuracy by condition."
                            ),
                            data=accuracy,
                        )
                    ],
                )
            ],
        ),

        ReportSection(
            title="Hypothesis Assessment",
            paragraphs=[
                (
                    "The reporting infrastructure "
                    "generated both document formats "
                    "successfully."
                )
            ],
        ),
    ],
)


builder = ScientificReportBuilder(
    content
)

builder.build_docx(
    "reports/final_report/"
    "reporting_test.docx"
)

builder.build_pdf(
    "reports/final_report/"
    "reporting_test.pdf"
)

print(
    "Reporting infrastructure: OK"
)