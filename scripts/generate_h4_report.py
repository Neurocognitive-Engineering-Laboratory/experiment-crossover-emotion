"""
Generate the final Hypothesis 4 scientific report.
"""

from src import config as cfg

from src.reporting.hypothesis import (
    Hypothesis4Report,
)


def main() -> None:

    print("=" * 70)
    print("GENERATING HYPOTHESIS 4 REPORT")
    print("=" * 70)

    report = Hypothesis4Report(
        output_directory=(
            cfg.FINAL_REPORT_DIR
        )
    )

    docx_path, pdf_path = (
        report.generate()
    )

    print(
        "\nHypothesis 4 report generated successfully."
    )

    print(
        f"\nDOCX:\n{docx_path}"
    )

    print(
        f"\nPDF:\n{pdf_path}"
    )


if __name__ == "__main__":
    main()