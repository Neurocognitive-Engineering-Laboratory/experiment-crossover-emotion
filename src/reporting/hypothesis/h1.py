"""
Hypothesis 1 scientific report.

Hypothesis:
Positive, negative, and neutral emotional conditions differentially
affect working-memory performance.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

from src import config as cfg

from ..report_builder import (
    ReportContent,
    ReportSection,
    ReportSubsection,
    ReportTable,
)

from ..report_generator import (
    BaseHypothesisReport,
)

from ..report_utils import (
    find_column,
    find_model_contrast,
    format_p_value,
    format_percent,
    get_condition_row,
    get_value,
)

class Hypothesis1Report(
    BaseHypothesisReport
):
    """
    Generate the final scientific report for Hypothesis 1.
    """

    report_number = 1

    title = (
        "Hypothesis 1 - Effect of Emotional Condition "
        "on Working-Memory Performance"
    )

    subtitle = (
        "Confirmatory Hypothesis Report"
    )

    output_filename = (
        "hypothesis_01_report"
    )

    input_files = {
        "accuracy_descriptive":
            cfg.TABLES_DIR
            / "hypothesis_01"
            / "h1_accuracy_descriptive.csv",

        "accuracy_model":
            cfg.TABLES_DIR
            / "hypothesis_01"
            / "h1_accuracy_model.csv",

        "rt_descriptive":
            cfg.TABLES_DIR
            / "hypothesis_01"
            / "h1_rt_descriptive.csv",

        "rt_model":
            cfg.TABLES_DIR
            / "hypothesis_01"
            / "h1_rt_model.csv",

        "summary":
            cfg.TABLES_DIR
            / "hypothesis_01"
            / "h1_summary.csv",
    }

    # ------------------------------------------------------------------
    # RESULT EXTRACTION
    # ------------------------------------------------------------------

    def extract_values(
        self,
    ) -> dict:
        """
        Extract all values used by the report.
        """

        accuracy_desc = self.results[
            "accuracy_descriptive"
        ]

        accuracy_model = self.results[
            "accuracy_model"
        ]

        rt_desc = self.results[
            "rt_descriptive"
        ]

        rt_model = self.results[
            "rt_model"
        ]

        summary = self.results[
            "summary"
        ]

        negative_acc = get_condition_row(
            accuracy_desc,
            "Negative",
        )

        neutral_acc = get_condition_row(
            accuracy_desc,
            "Neutral",
        )

        positive_acc = get_condition_row(
            accuracy_desc,
            "Positive",
        )

        negative_rt = get_condition_row(
            rt_desc,
            "Negative",
        )

        neutral_rt = get_condition_row(
            rt_desc,
            "Neutral",
        )

        positive_rt = get_condition_row(
            rt_desc,
            "Positive",
        )

        negative_acc_model = (
            find_model_contrast(
                accuracy_model,
                "Negative",
            )
        )

        positive_acc_model = (
            find_model_contrast(
                accuracy_model,
                "Positive",
            )
        )

        negative_rt_model = (
            find_model_contrast(
                rt_model,
                "Negative",
            )
        )

        positive_rt_model = (
            find_model_contrast(
                rt_model,
                "Positive",
            )
        )

        return {
            "participants":
                int(
                    summary[
                        "participants"
                    ].iloc[0]
                ),

            "accuracy_observations":
                int(
                    summary[
                        "accuracy_observations"
                    ].iloc[0]
                ),

            "rt_observations":
                int(
                    summary[
                        "rt_observations"
                    ].iloc[0]
                ),

            # Accuracy descriptive
            "negative_accuracy":
                float(
                    negative_acc[
                        "accuracy_mean"
                    ]
                ),

            "neutral_accuracy":
                float(
                    neutral_acc[
                        "accuracy_mean"
                    ]
                ),

            "positive_accuracy":
                float(
                    positive_acc[
                        "accuracy_mean"
                    ]
                ),

            # Accuracy models
            "negative_accuracy_beta":
                float(
                    negative_acc_model[
                        "beta"
                    ]
                ),

            "negative_accuracy_se":
                float(
                    negative_acc_model[
                        "se"
                    ]
                ),

            "negative_accuracy_z":
                float(
                    negative_acc_model[
                        "z"
                    ]
                ),

            "negative_accuracy_p":
                float(
                    negative_acc_model[
                        "p"
                    ]
                ),

            "negative_accuracy_or":
                float(
                    negative_acc_model[
                        "odds_ratio"
                    ]
                ),

            "negative_accuracy_ci_low":
                float(
                    negative_acc_model[
                        "or_ci_low"
                    ]
                ),

            "negative_accuracy_ci_high":
                float(
                    negative_acc_model[
                        "or_ci_high"
                    ]
                ),

            "positive_accuracy_beta":
                float(
                    positive_acc_model[
                        "beta"
                    ]
                ),

            "positive_accuracy_se":
                float(
                    positive_acc_model[
                        "se"
                    ]
                ),

            "positive_accuracy_z":
                float(
                    positive_acc_model[
                        "z"
                    ]
                ),

            "positive_accuracy_p":
                float(
                    positive_acc_model[
                        "p"
                    ]
                ),

            "positive_accuracy_or":
                float(
                    positive_acc_model[
                        "odds_ratio"
                    ]
                ),

            "positive_accuracy_ci_low":
                float(
                    positive_acc_model[
                        "or_ci_low"
                    ]
                ),

            "positive_accuracy_ci_high":
                float(
                    positive_acc_model[
                        "or_ci_high"
                    ]
                ),

            # RT descriptive
            "negative_mean_rt":
                float(
                    negative_rt[
                        "mean_rt"
                    ]
                ),

            "neutral_mean_rt":
                float(
                    neutral_rt[
                        "mean_rt"
                    ]
                ),

            "positive_mean_rt":
                float(
                    positive_rt[
                        "mean_rt"
                    ]
                ),

            # RT models
            "negative_rt_beta":
                float(
                    negative_rt_model[
                        "beta"
                    ]
                ),

            "negative_rt_se":
                float(
                    negative_rt_model[
                        "se"
                    ]
                ),

            "negative_rt_z":
                float(
                    negative_rt_model[
                        "z"
                    ]
                ),

            "negative_rt_p":
                float(
                    negative_rt_model[
                        "p"
                    ]
                ),

            "negative_rt_change":
                float(
                    negative_rt_model[
                        "percent_change"
                    ]
                ),

            "negative_rt_ci_low":
                float(
                    negative_rt_model[
                        "percent_ci_low"
                    ]
                ),

            "negative_rt_ci_high":
                float(
                    negative_rt_model[
                        "percent_ci_high"
                    ]
                ),

            "positive_rt_beta":
                float(
                    positive_rt_model[
                        "beta"
                    ]
                ),

            "positive_rt_se":
                float(
                    positive_rt_model[
                        "se"
                    ]
                ),

            "positive_rt_z":
                float(
                    positive_rt_model[
                        "z"
                    ]
                ),

            "positive_rt_p":
                float(
                    positive_rt_model[
                        "p"
                    ]
                ),

            "positive_rt_change":
                float(
                    positive_rt_model[
                        "percent_change"
                    ]
                ),

            "positive_rt_ci_low":
                float(
                    positive_rt_model[
                        "percent_ci_low"
                    ]
                ),

            "positive_rt_ci_high":
                float(
                    positive_rt_model[
                        "percent_ci_high"
                    ]
                ),

            "assessment":
                str(
                    summary[
                        "assessment"
                    ].iloc[0]
                ),
        }

    # ------------------------------------------------------------------
    # TABLES
    # ------------------------------------------------------------------

    def build_accuracy_descriptive_table(
        self,
    ) -> pd.DataFrame:

        table = self.results[
            "accuracy_descriptive"
        ].copy()

        table = table.rename(
            columns={
                "emotion_condition":
                    "Condition",

                "participants":
                    "Participants",

                "trials":
                    "Trials",

                "accuracy_mean":
                    "Accuracy",

                "accuracy_sd":
                    "SD",

                "accuracy_median":
                    "Median",
            }
        )

        if "Accuracy" in table.columns:

            table[
                "Accuracy"
            ] = (
                table[
                    "Accuracy"
                ]
                .map(
                    lambda value:
                    format_percent(
                        value
                    )
                )
            )

        if "SD" in table.columns:

            table[
                "SD"
            ] = (
                table[
                    "SD"
                ]
                .map(
                    lambda value:
                    f"{value:.3f}"
                )
            )

        return table

    def build_accuracy_model_table(
        self,
        values: dict,
    ) -> pd.DataFrame:

        return pd.DataFrame(
            {
                "Contrast": [
                    "Negative vs Neutral",
                    "Positive vs Neutral",
                ],

                "OR": [
                    (
                        f"{values['negative_accuracy_or']:.2f}"
                    ),
                    (
                        f"{values['positive_accuracy_or']:.2f}"
                    ),
                ],

                "95% CI": [
                    (
                        "["
                        f"{values['negative_accuracy_ci_low']:.2f}, "
                        f"{values['negative_accuracy_ci_high']:.2f}"
                        "]"
                    ),
                    (
                        "["
                        f"{values['positive_accuracy_ci_low']:.2f}, "
                        f"{values['positive_accuracy_ci_high']:.2f}"
                        "]"
                    ),
                ],

                "p": [
                    format_p_value(
                        values[
                            "negative_accuracy_p"
                        ]
                    ),
                    format_p_value(
                        values[
                            "positive_accuracy_p"
                        ]
                    ),
                ],
            }
        )

    def build_rt_descriptive_table(
        self,
    ) -> pd.DataFrame:

        table = self.results[
            "rt_descriptive"
        ].copy()

        table = table.rename(
            columns={
                "emotion_condition":
                    "Condition",

                "participants":
                    "Participants",

                "trials":
                    "Trials",

                "mean_rt":
                    "Mean RT",

                "sd_rt":
                    "SD",

                "median_rt":
                    "Median RT",

                "mean_log_rt":
                    "Mean log RT",
            }
        )

        numeric_columns = [
            "Mean RT",
            "SD",
            "Median RT",
            "Mean log RT",
        ]

        for column in numeric_columns:

            if column in table.columns:

                table[
                    column
                ] = table[
                    column
                ].map(
                    lambda value:
                    f"{value:.2f}"
                )

        return table

    def build_rt_model_table(
        self,
        values: dict,
    ) -> pd.DataFrame:

        return pd.DataFrame(
            {
                "Contrast": [
                    "Negative vs Neutral",
                    "Positive vs Neutral",
                ],

                "Beta": [
                    (
                        f"{values['negative_rt_beta']:.3f}"
                    ),
                    (
                        f"{values['positive_rt_beta']:.3f}"
                    ),
                ],

                "RT change": [
                    (
                        f"{values['negative_rt_change']:.1f}%"
                    ),
                    (
                        f"{values['positive_rt_change']:.1f}%"
                    ),
                ],

                "95% CI": [
                    (
                        "["
                        f"{values['negative_rt_ci_low']:.1f}%, "
                        f"{values['negative_rt_ci_high']:.1f}%"
                        "]"
                    ),
                    (
                        "["
                        f"{values['positive_rt_ci_low']:.1f}%, "
                        f"{values['positive_rt_ci_high']:.1f}%"
                        "]"
                    ),
                ],

                "p": [
                    format_p_value(
                        values[
                            "negative_rt_p"
                        ]
                    ),
                    format_p_value(
                        values[
                            "positive_rt_p"
                        ]
                    ),
                ],
            }
        )

    # ------------------------------------------------------------------
    # TEXT
    # ------------------------------------------------------------------

    def build_method(
        self,
        values: dict,
    ) -> list[str]:

        return [
            (
                "A trial-level confirmatory analysis was conducted to evaluate "
                "whether working-memory performance differed across neutral, "
                "positive, and negative emotional conditions. The analytical "
                f"sample included {values['participants']} participants."
            ),

            (
                "Response accuracy was analyzed using a generalized estimating "
                "equation (GEE) model with a binomial distribution, logit link, "
                "exchangeable within-participant correlation structure, and "
                "robust standard errors. Emotional condition was entered as "
                "the primary predictor, with the neutral condition specified "
                "as the reference category. The accuracy model included "
                f"{values['accuracy_observations']:,} trial-level observations."
            ),

            (
                "Reaction time was analyzed among valid correct-response trials "
                "only. Because reaction-time data were positively skewed, "
                "reaction time was log-transformed prior to modeling. A linear "
                "mixed-effects model was fitted with emotional condition as a "
                "fixed effect and a participant-specific random intercept. "
                f"The reaction-time analysis included "
                f"{values['rt_observations']:,} observations. "
                "Maximum-likelihood estimation was used."
            ),

            (
                "Model coefficients from the binomial GEE were exponentiated "
                "and interpreted as odds ratios. Coefficients from the log "
                "reaction-time model were exponentiated and converted to "
                "percentage changes relative to the neutral condition. "
                "Statistical significance was evaluated using a two-sided "
                "alpha level of .05, and 95% confidence intervals are reported."
            ),
        ]

    def build_accuracy_results(
        self,
        values: dict,
    ) -> list[str]:

        return [
            (
                "Descriptively, accuracy was highly similar across emotional "
                "conditions. Mean trial-level accuracy was "
                f"{format_percent(values['negative_accuracy'])} in the "
                "negative condition, "
                f"{format_percent(values['neutral_accuracy'])} in the "
                "neutral condition, and "
                f"{format_percent(values['positive_accuracy'])} in the "
                "positive condition."
            ),

            (
                "Relative to the neutral condition, the negative condition "
                "was associated with a small, non-significant reduction in "
                "the odds of a correct response "
                f"(beta = {values['negative_accuracy_beta']:.3f}, "
                f"SE = {values['negative_accuracy_se']:.3f}, "
                f"z = {values['negative_accuracy_z']:.2f}, "
                f"p {format_p_value(values['negative_accuracy_p'])}), "
                "corresponding to an odds ratio of "
                f"{values['negative_accuracy_or']:.2f} "
                "(95% CI "
                f"[{values['negative_accuracy_ci_low']:.2f}, "
                f"{values['negative_accuracy_ci_high']:.2f}])."
            ),

            (
                "The positive condition did not differ significantly from "
                "the neutral condition "
                f"(beta = {values['positive_accuracy_beta']:.3f}, "
                f"SE = {values['positive_accuracy_se']:.3f}, "
                f"z = {values['positive_accuracy_z']:.2f}, "
                f"p {format_p_value(values['positive_accuracy_p'])}), "
                "with an odds ratio of "
                f"{values['positive_accuracy_or']:.2f} "
                "(95% CI "
                f"[{values['positive_accuracy_ci_low']:.2f}, "
                f"{values['positive_accuracy_ci_high']:.2f}])."
            ),

            (
                "Taken together, these findings provide no evidence that "
                "emotional condition substantially altered the probability "
                "of producing a correct response."
            ),
        ]

    def build_rt_results(
        self,
        values: dict,
    ) -> list[str]:

        return [
            (
                "In contrast to accuracy, emotional condition was strongly "
                "associated with reaction time."
            ),

            (
                "Relative to the neutral condition, the negative emotional "
                "condition was associated with a significantly lower log "
                "reaction time "
                f"(beta = {values['negative_rt_beta']:.3f}, "
                f"SE = {values['negative_rt_se']:.3f}, "
                f"z = {values['negative_rt_z']:.2f}, "
                f"p {format_p_value(values['negative_rt_p'])}). "
                "After back-transformation, this coefficient corresponded "
                "to an estimated "
                f"{abs(values['negative_rt_change']):.1f}% reduction in "
                "reaction time relative to the neutral condition."
            ),

            (
                "The positive emotional condition was also associated with "
                "a significantly lower log reaction time compared with the "
                "neutral condition "
                f"(beta = {values['positive_rt_beta']:.3f}, "
                f"SE = {values['positive_rt_se']:.3f}, "
                f"z = {values['positive_rt_z']:.2f}, "
                f"p {format_p_value(values['positive_rt_p'])}). "
                "This corresponds to an estimated "
                f"{abs(values['positive_rt_change']):.1f}% reduction in "
                "reaction time relative to neutral."
            ),

            (
                "The magnitude of the positive and negative coefficients was "
                "similar, suggesting that both emotionally induced conditions "
                "were associated with faster responses compared with the "
                "neutral baseline."
            ),
        ]

    def build_interpretation(
        self,
        values: dict,
    ) -> list[str]:

        return [
            (
                "Hypothesis 1 was partially supported."
            ),

            (
                "The emotional manipulation did not produce statistically "
                "detectable differences in response accuracy. Accuracy "
                "remained approximately 84-85% across the three emotional "
                "conditions."
            ),

            (
                "However, emotional condition showed a pronounced association "
                "with reaction speed. Both positive and negative emotional "
                "conditions were associated with substantially faster "
                "responses than the neutral condition."
            ),

            (
                "Importantly, the faster responses under emotional induction "
                "were not accompanied by a statistically significant loss of "
                "accuracy. Thus, the results suggest that emotional induction "
                "influenced the speed component of working-memory performance "
                "more strongly than the probability of a correct response."
            ),

            (
                "Because both positive and negative conditions showed effects "
                "in the same direction relative to neutral, these results do "
                "not demonstrate a valence-specific advantage of positive "
                "emotion or a valence-specific impairment under negative "
                "emotion. Those directional predictions are evaluated in "
                "Hypotheses 2 and 3."
            ),
        ]

    # ------------------------------------------------------------------
    # COMPLETE REPORT
    # ------------------------------------------------------------------

    def build_content(
        self,
    ) -> ReportContent:

        values = self.extract_values()

        accuracy_table = (
            self.build_accuracy_descriptive_table()
        )

        accuracy_model_table = (
            self.build_accuracy_model_table(
                values
            )
        )

        rt_table = (
            self.build_rt_descriptive_table()
        )

        rt_model_table = (
            self.build_rt_model_table(
                values
            )
        )

        return ReportContent(
            title=self.title,

            subtitle=self.subtitle,

            hypothesis=(
                "Positive, negative, and neutral emotional "
                "conditions differentially affect "
                "working-memory performance."
            ),

            sections=[
                # --------------------------------------------------
                # METHOD
                # --------------------------------------------------

                ReportSection(
                    title="Method",

                    paragraphs=(
                        self.build_method(
                            values
                        )
                    ),
                ),

                # --------------------------------------------------
                # RESULTS
                # --------------------------------------------------

                ReportSection(
                    title="Results",

                    subsections=[
                        ReportSubsection(
                            title="Accuracy",

                            paragraphs=(
                                self.build_accuracy_results(
                                    values
                                )
                            ),

                            tables=[
                                ReportTable(
                                    caption=(
                                        "Table 1. Descriptive accuracy "
                                        "by emotional condition."
                                    ),

                                    data=accuracy_table,
                                ),

                                ReportTable(
                                    caption=(
                                        "Table 2. GEE estimates for "
                                        "response accuracy."
                                    ),

                                    data=(
                                        accuracy_model_table
                                    ),
                                ),
                            ],
                        ),

                        ReportSubsection(
                            title="Reaction Time",

                            paragraphs=(
                                self.build_rt_results(
                                    values
                                )
                            ),

                            tables=[
                                ReportTable(
                                    caption=(
                                        "Table 3. Descriptive reaction "
                                        "time by emotional condition."
                                    ),

                                    data=rt_table,
                                ),

                                ReportTable(
                                    caption=(
                                        "Table 4. Mixed-effects model "
                                        "estimates for log reaction time."
                                    ),

                                    data=rt_model_table,
                                ),
                            ],
                        ),
                    ],
                ),

                # --------------------------------------------------
                # DECISION RULES
                # --------------------------------------------------

                ReportSection(
                    title="Decision Rules",

                    bullets=[
                        (
                            "H1 is supported if there is clear evidence of "
                            "differences between emotional conditions in "
                            "accuracy, reaction time, or both."
                        ),

                        (
                            "H1 is partially supported if differences arise "
                            "in only one outcome or in only one specific "
                            "contrast."
                        ),

                        (
                            "H1 is not supported if there is no evidence of "
                            "relevant differences between conditions."
                        ),
                    ],
                ),

                # --------------------------------------------------
                # INTERPRETATION
                # --------------------------------------------------

                ReportSection(
                    title="Interpretation",

                    paragraphs=(
                        self.build_interpretation(
                            values
                        )
                    ),
                ),

                # --------------------------------------------------
                # ASSESSMENT
                # --------------------------------------------------

                ReportSection(
                    title="Hypothesis Assessment",

                    paragraphs=[
                        (
                            "Conclusion: Hypothesis 1 was partially supported. "
                            "Emotional condition did not significantly affect "
                            "accuracy, but both positive and negative emotional "
                            "conditions were associated with substantially "
                            "faster reaction times relative to the neutral "
                            "condition."
                        )
                    ],
                ),
            ],
        )