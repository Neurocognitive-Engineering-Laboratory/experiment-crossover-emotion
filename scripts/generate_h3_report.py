"""
Generate the final Hypothesis 3 scientific report.
"""

from src import config as cfg

from src.reporting.hypothesis import (
    Hypothesis3Report,
)


def main() -> None:

    print("=" * 70)
    print("GENERATING HYPOTHESIS 3 REPORT")
    print("=" * 70)

    report = Hypothesis3Report(
        output_directory=(
            cfg.FINAL_REPORT_DIR
        )
    )

    docx_path, pdf_path = (
        report.generate()
    )

    print(
        "\nHypothesis 3 report generated successfully."
    )

    print(
        f"\nDOCX:\n{docx_path}"
    )

    print(
        f"\nPDF:\n{pdf_path}"
    )


if __name__ == "__main__":
    main()