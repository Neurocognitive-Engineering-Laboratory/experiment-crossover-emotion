"""
Generate the final Hypothesis 1 scientific report.
"""

from src import config as cfg

from src.reporting.hypothesis import (
    Hypothesis1Report,
)


def main() -> None:

    print("=" * 70)
    print("GENERATING HYPOTHESIS 1 REPORT")
    print("=" * 70)

    report = Hypothesis1Report(
        output_directory=(
            cfg.FINAL_REPORT_DIR
        )
    )

    docx_path, pdf_path = (
        report.generate()
    )

    print(
        "\nHypothesis 1 report generated successfully."
    )

    print(
        f"\nDOCX:\n{docx_path}"
    )

    print(
        f"\nPDF:\n{pdf_path}"
    )


if __name__ == "__main__":
    main()