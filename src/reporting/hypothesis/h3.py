"""
Hypothesis 3 scientific report.

Hypothesis:
Positive emotional induction improves working-memory performance
relative to neutral and negative emotional conditions.
"""

from __future__ import annotations

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
    format_p_value,
    format_percent,
    get_condition_row,
)


class Hypothesis3Report(
    BaseHypothesisReport
):
    """
    Generate the final scientific report for Hypothesis 3.
    """

    report_number = 3

    title = (
        "Hypothesis 3 - Effect of Positive Emotion "
        "on Working-Memory Performance"
    )

    subtitle = (
        "Confirmatory Hypothesis Report"
    )

    output_filename = (
        "hypothesis_03_report"
    )

    input_files = {
        "sample":
            cfg.TABLES_DIR
            / "hypothesis_03"
            / "h3_sample.csv",

        "accuracy_descriptive":
            cfg.TABLES_DIR
            / "hypothesis_03"
            / "h3_accuracy_descriptive.csv",

        "accuracy_models":
            cfg.TABLES_DIR
            / "hypothesis_03"
            / "h3_accuracy_models.csv",

        "rt_descriptive":
            cfg.TABLES_DIR
            / "hypothesis_03"
            / "h3_rt_descriptive.csv",

        "rt_models":
            cfg.TABLES_DIR
            / "hypothesis_03"
            / "h3_rt_models.csv",

        "efficiency_descriptive":
            cfg.TABLES_DIR
            / "hypothesis_03"
            / "h3_efficiency_descriptive.csv",

        "efficiency_tests":
            cfg.TABLES_DIR
            / "hypothesis_03"
            / "h3_efficiency_tests.csv",

        "summary":
            cfg.TABLES_DIR
            / "hypothesis_03"
            / "h3_summary.csv",
    }

    # ==================================================================
    # RESULT EXTRACTION
    # ==================================================================

    def extract_values(
        self,
    ) -> dict:
        """
        Extract all numerical values required by the H3 report.
        """

        accuracy_desc = self.results[
            "accuracy_descriptive"
        ]

        accuracy_models = self.results[
            "accuracy_models"
        ]

        rt_desc = self.results[
            "rt_descriptive"
        ]

        rt_models = self.results[
            "rt_models"
        ]

        efficiency_tests = self.results[
            "efficiency_tests"
        ]

        summary = self.results[
            "summary"
        ]

        positive_accuracy = get_condition_row(
            accuracy_desc,
            "Positive",
        )

        neutral_accuracy = get_condition_row(
            accuracy_desc,
            "Neutral",
        )

        negative_accuracy = get_condition_row(
            accuracy_desc,
            "Negative",
        )

        positive_rt = get_condition_row(
            rt_desc,
            "Positive",
        )

        neutral_rt = get_condition_row(
            rt_desc,
            "Neutral",
        )

        negative_rt = get_condition_row(
            rt_desc,
            "Negative",
        )

        accuracy_positive_neutral = (
            accuracy_models.loc[
                accuracy_models["contrast"]
                == "Positive vs Neutral"
            ]
            .iloc[0]
        )

        accuracy_positive_negative = (
            accuracy_models.loc[
                accuracy_models["contrast"]
                == "Positive vs Negative"
            ]
            .iloc[0]
        )

        rt_positive_neutral = (
            rt_models.loc[
                rt_models["contrast"]
                == "Positive vs Neutral"
            ]
            .iloc[0]
        )

        rt_positive_negative = (
            rt_models.loc[
                rt_models["contrast"]
                == "Positive vs Negative"
            ]
            .iloc[0]
        )

        ies_positive_neutral = (
            efficiency_tests.loc[
                efficiency_tests["contrast"]
                == "Positive vs Neutral"
            ]
            .iloc[0]
        )

        ies_positive_negative = (
            efficiency_tests.loc[
                efficiency_tests["contrast"]
                == "Positive vs Negative"
            ]
            .iloc[0]
        )

        return {
            # ----------------------------------------------------------
            # SAMPLE
            # ----------------------------------------------------------

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

            # ----------------------------------------------------------
            # ACCURACY DESCRIPTIVE
            # ----------------------------------------------------------

            "positive_accuracy":
                float(
                    positive_accuracy[
                        "accuracy_mean"
                    ]
                ),

            "neutral_accuracy":
                float(
                    neutral_accuracy[
                        "accuracy_mean"
                    ]
                ),

            "negative_accuracy":
                float(
                    negative_accuracy[
                        "accuracy_mean"
                    ]
                ),

            # ----------------------------------------------------------
            # ACCURACY MODELS
            # ----------------------------------------------------------

            "pn_accuracy_beta":
                float(
                    accuracy_positive_neutral[
                        "beta"
                    ]
                ),

            "pn_accuracy_se":
                float(
                    accuracy_positive_neutral[
                        "se"
                    ]
                ),

            "pn_accuracy_z":
                float(
                    accuracy_positive_neutral[
                        "z"
                    ]
                ),

            "pn_accuracy_p":
                float(
                    accuracy_positive_neutral[
                        "p"
                    ]
                ),

            "pn_accuracy_or":
                float(
                    accuracy_positive_neutral[
                        "odds_ratio"
                    ]
                ),

            "pn_accuracy_ci_low":
                float(
                    accuracy_positive_neutral[
                        "or_ci_low"
                    ]
                ),

            "pn_accuracy_ci_high":
                float(
                    accuracy_positive_neutral[
                        "or_ci_high"
                    ]
                ),

            "pg_accuracy_beta":
                float(
                    accuracy_positive_negative[
                        "beta"
                    ]
                ),

            "pg_accuracy_se":
                float(
                    accuracy_positive_negative[
                        "se"
                    ]
                ),

            "pg_accuracy_z":
                float(
                    accuracy_positive_negative[
                        "z"
                    ]
                ),

            "pg_accuracy_p":
                float(
                    accuracy_positive_negative[
                        "p"
                    ]
                ),

            "pg_accuracy_or":
                float(
                    accuracy_positive_negative[
                        "odds_ratio"
                    ]
                ),

            "pg_accuracy_ci_low":
                float(
                    accuracy_positive_negative[
                        "or_ci_low"
                    ]
                ),

            "pg_accuracy_ci_high":
                float(
                    accuracy_positive_negative[
                        "or_ci_high"
                    ]
                ),

            # ----------------------------------------------------------
            # RT DESCRIPTIVE
            # ----------------------------------------------------------

            "positive_mean_rt":
                float(
                    positive_rt[
                        "mean_rt"
                    ]
                ),

            "neutral_mean_rt":
                float(
                    neutral_rt[
                        "mean_rt"
                    ]
                ),

            "negative_mean_rt":
                float(
                    negative_rt[
                        "mean_rt"
                    ]
                ),

            # ----------------------------------------------------------
            # RT MODELS
            # ----------------------------------------------------------

            "pn_rt_beta":
                float(
                    rt_positive_neutral[
                        "beta"
                    ]
                ),

            "pn_rt_se":
                float(
                    rt_positive_neutral[
                        "se"
                    ]
                ),

            "pn_rt_z":
                float(
                    rt_positive_neutral[
                        "z"
                    ]
                ),

            "pn_rt_p":
                float(
                    rt_positive_neutral[
                        "p"
                    ]
                ),

            "pn_rt_change":
                float(
                    rt_positive_neutral[
                        "percent_change"
                    ]
                ),

            "pn_rt_ci_low":
                float(
                    rt_positive_neutral[
                        "percent_ci_low"
                    ]
                ),

            "pn_rt_ci_high":
                float(
                    rt_positive_neutral[
                        "percent_ci_high"
                    ]
                ),

            "pg_rt_beta":
                float(
                    rt_positive_negative[
                        "beta"
                    ]
                ),

            "pg_rt_se":
                float(
                    rt_positive_negative[
                        "se"
                    ]
                ),

            "pg_rt_z":
                float(
                    rt_positive_negative[
                        "z"
                    ]
                ),

            "pg_rt_p":
                float(
                    rt_positive_negative[
                        "p"
                    ]
                ),

            "pg_rt_change":
                float(
                    rt_positive_negative[
                        "percent_change"
                    ]
                ),

            "pg_rt_ci_low":
                float(
                    rt_positive_negative[
                        "percent_ci_low"
                    ]
                ),

            "pg_rt_ci_high":
                float(
                    rt_positive_negative[
                        "percent_ci_high"
                    ]
                ),

            # ----------------------------------------------------------
            # EFFICIENCY
            # ----------------------------------------------------------

            "pn_ies_n":
                int(
                    ies_positive_neutral[
                        "n"
                    ]
                ),

            "pn_ies_positive_mean":
                float(
                    ies_positive_neutral[
                        "positive_mean"
                    ]
                ),

            "pn_ies_comparator_mean":
                float(
                    ies_positive_neutral[
                        "comparator_mean"
                    ]
                ),

            "pn_ies_difference":
                float(
                    ies_positive_neutral[
                        "mean_difference"
                    ]
                ),

            "pn_ies_t":
                float(
                    ies_positive_neutral[
                        "t"
                    ]
                ),

            "pn_ies_p":
                float(
                    ies_positive_neutral[
                        "p"
                    ]
                ),

            "pg_ies_n":
                int(
                    ies_positive_negative[
                        "n"
                    ]
                ),

            "pg_ies_positive_mean":
                float(
                    ies_positive_negative[
                        "positive_mean"
                    ]
                ),

            "pg_ies_comparator_mean":
                float(
                    ies_positive_negative[
                        "comparator_mean"
                    ]
                ),

            "pg_ies_difference":
                float(
                    ies_positive_negative[
                        "mean_difference"
                    ]
                ),

            "pg_ies_t":
                float(
                    ies_positive_negative[
                        "t"
                    ]
                ),

            "pg_ies_p":
                float(
                    ies_positive_negative[
                        "p"
                    ]
                ),

            # ----------------------------------------------------------
            # ASSESSMENT
            # ----------------------------------------------------------

            "assessment":
                str(
                    summary[
                        "assessment"
                    ].iloc[0]
                ),
        }

    # ==================================================================
    # TABLES
    # ==================================================================

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

                "correct":
                    "Correct",

                "accuracy_mean":
                    "Accuracy",

                "accuracy_sd":
                    "SD",

                "accuracy_median":
                    "Median",
            }
        )

        table["Accuracy"] = (
            table["Accuracy"]
            .map(format_percent)
        )

        table["SD"] = (
            table["SD"]
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
                    "Positive vs Neutral",
                    "Positive vs Negative",
                ],

                "Beta": [
                    f"{values['pn_accuracy_beta']:.3f}",
                    f"{values['pg_accuracy_beta']:.3f}",
                ],

                "OR": [
                    f"{values['pn_accuracy_or']:.3f}",
                    f"{values['pg_accuracy_or']:.3f}",
                ],

                "95% CI": [
                    (
                        "["
                        f"{values['pn_accuracy_ci_low']:.2f}, "
                        f"{values['pn_accuracy_ci_high']:.2f}"
                        "]"
                    ),
                    (
                        "["
                        f"{values['pg_accuracy_ci_low']:.2f}, "
                        f"{values['pg_accuracy_ci_high']:.2f}"
                        "]"
                    ),
                ],

                "p": [
                    format_p_value(
                        values[
                            "pn_accuracy_p"
                        ]
                    ),
                    format_p_value(
                        values[
                            "pg_accuracy_p"
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

        for column in [
            "Mean RT",
            "SD",
            "Median RT",
            "Mean log RT",
        ]:

            if column in table.columns:

                table[column] = (
                    table[column]
                    .map(
                        lambda value:
                        f"{value:.2f}"
                    )
                )

        return table

    def build_rt_model_table(
        self,
        values: dict,
    ) -> pd.DataFrame:

        return pd.DataFrame(
            {
                "Contrast": [
                    "Positive vs Neutral",
                    "Positive vs Negative",
                ],

                "Beta": [
                    f"{values['pn_rt_beta']:.3f}",
                    f"{values['pg_rt_beta']:.3f}",
                ],

                "RT change": [
                    f"{values['pn_rt_change']:.1f}%",
                    f"{values['pg_rt_change']:.1f}%",
                ],

                "95% CI": [
                    (
                        "["
                        f"{values['pn_rt_ci_low']:.1f}%, "
                        f"{values['pn_rt_ci_high']:.1f}%"
                        "]"
                    ),
                    (
                        "["
                        f"{values['pg_rt_ci_low']:.1f}%, "
                        f"{values['pg_rt_ci_high']:.1f}%"
                        "]"
                    ),
                ],

                "p": [
                    format_p_value(
                        values[
                            "pn_rt_p"
                        ]
                    ),
                    format_p_value(
                        values[
                            "pg_rt_p"
                        ]
                    ),
                ],
            }
        )

    def build_efficiency_table(
        self,
        values: dict,
    ) -> pd.DataFrame:

        return pd.DataFrame(
            {
                "Contrast": [
                    "Positive vs Neutral",
                    "Positive vs Negative",
                ],

                "N": [
                    values[
                        "pn_ies_n"
                    ],
                    values[
                        "pg_ies_n"
                    ],
                ],

                "Positive IES": [
                    f"{values['pn_ies_positive_mean']:.2f}",
                    f"{values['pg_ies_positive_mean']:.2f}",
                ],

                "Comparator IES": [
                    f"{values['pn_ies_comparator_mean']:.2f}",
                    f"{values['pg_ies_comparator_mean']:.2f}",
                ],

                "Difference": [
                    f"{values['pn_ies_difference']:.2f}",
                    f"{values['pg_ies_difference']:.2f}",
                ],

                "t": [
                    f"{values['pn_ies_t']:.2f}",
                    f"{values['pg_ies_t']:.2f}",
                ],

                "p": [
                    format_p_value(
                        values[
                            "pn_ies_p"
                        ]
                    ),
                    format_p_value(
                        values[
                            "pg_ies_p"
                        ]
                    ),
                ],
            }
        )

    # ==================================================================
    # TEXT
    # ==================================================================

    def build_method(
        self,
        values: dict,
    ) -> list[str]:

        return [
            (
                "A confirmatory trial-level analysis was conducted to "
                "determine whether positive emotional induction improved "
                "working-memory performance relative to neutral and negative "
                "emotional conditions. The analytical sample included "
                f"{values['participants']} participants."
            ),

            (
                "The primary outcomes were response accuracy and reaction "
                "time. Accuracy was analyzed using generalized estimating "
                "equation (GEE) models with a binomial distribution, logit "
                "link, exchangeable within-participant correlation structure, "
                "and robust standard errors. Two planned contrasts were "
                "evaluated: Positive versus Neutral and Positive versus "
                f"Negative. The accuracy analysis included "
                f"{values['accuracy_observations']:,} trial-level observations."
            ),

            (
                "Reaction time was analyzed among valid correct-response "
                "trials only. Because reaction-time data were positively "
                "skewed, reaction time was log-transformed prior to modeling. "
                "Linear mixed-effects models were fitted with emotional "
                "condition as a fixed effect and a participant-specific "
                "random intercept. The reaction-time analysis included "
                f"{values['rt_observations']:,} observations."
            ),

            (
                "GEE coefficients were exponentiated and interpreted as odds "
                "ratios. Log reaction-time coefficients were exponentiated "
                "and converted to percentage changes. Inverse efficiency "
                "scores were examined as a secondary indicator of combined "
                "speed and accuracy. Statistical significance was evaluated "
                "using a two-sided alpha level of .05, with 95% confidence "
                "intervals reported."
            ),
        ]

    def build_accuracy_results(
        self,
        values: dict,
    ) -> list[str]:

        return [
            (
                "Mean trial-level accuracy was "
                f"{format_percent(values['positive_accuracy'])} "
                "in the positive condition, "
                f"{format_percent(values['neutral_accuracy'])} "
                "in the neutral condition, and "
                f"{format_percent(values['negative_accuracy'])} "
                "in the negative condition."
            ),

            (
                "Positive emotion did not significantly improve accuracy "
                "relative to the neutral condition "
                f"(OR = {values['pn_accuracy_or']:.3f}, "
                f"95% CI [{values['pn_accuracy_ci_low']:.2f}, "
                f"{values['pn_accuracy_ci_high']:.2f}], "
                f"p {format_p_value(values['pn_accuracy_p'])})."
            ),

            (
                "Accuracy was descriptively higher under positive than "
                "negative emotion, but this difference was not statistically "
                "significant "
                f"(OR = {values['pg_accuracy_or']:.3f}, "
                f"95% CI [{values['pg_accuracy_ci_low']:.2f}, "
                f"{values['pg_accuracy_ci_high']:.2f}], "
                f"p {format_p_value(values['pg_accuracy_p'])})."
            ),

            (
                "Thus, the accuracy analyses did not provide evidence that "
                "positive emotional induction improved the probability of "
                "producing a correct response relative to either comparator."
            ),
        ]

    def build_rt_results(
        self,
        values: dict,
    ) -> list[str]:

        return [
            (
                "Positive emotion was associated with a substantial reduction "
                "in reaction time relative to the neutral condition."
            ),

            (
                "Compared with neutral emotion, positive emotion was associated "
                "with a significantly lower log reaction time "
                f"(beta = {values['pn_rt_beta']:.3f}, "
                f"SE = {values['pn_rt_se']:.3f}, "
                f"z = {values['pn_rt_z']:.2f}, "
                f"p {format_p_value(values['pn_rt_p'])}). "
                "After back-transformation, this corresponded to an estimated "
                f"{abs(values['pn_rt_change']):.1f}% reduction in reaction "
                "time."
            ),

            (
                "By contrast, reaction time under positive emotion did not "
                "significantly differ from reaction time under negative "
                "emotion "
                f"(beta = {values['pg_rt_beta']:.3f}, "
                f"SE = {values['pg_rt_se']:.3f}, "
                f"z = {values['pg_rt_z']:.2f}, "
                f"p {format_p_value(values['pg_rt_p'])}). "
                "The estimated difference was only "
                f"{abs(values['pg_rt_change']):.1f}%."
            ),

            (
                "Therefore, positive emotional induction was associated with "
                "faster responding relative to the neutral condition, but it "
                "did not confer a significant reaction-time advantage over "
                "negative emotion."
            ),
        ]

    def build_efficiency_results(
        self,
        values: dict,
    ) -> list[str]:

        return [
            (
                "Inverse efficiency was examined as a secondary measure of "
                "combined processing speed and accuracy."
            ),

            (
                "For the Positive versus Neutral comparison, mean IES was "
                f"{values['pn_ies_positive_mean']:.2f} under positive emotion "
                "and "
                f"{values['pn_ies_comparator_mean']:.2f} under the neutral "
                "condition "
                f"(t = {values['pn_ies_t']:.2f}, "
                f"p {format_p_value(values['pn_ies_p'])})."
            ),

            (
                "For the Positive versus Negative comparison, mean IES was "
                f"{values['pg_ies_positive_mean']:.2f} under positive emotion "
                "and "
                f"{values['pg_ies_comparator_mean']:.2f} under negative "
                "emotion "
                f"(t = {values['pg_ies_t']:.2f}, "
                f"p {format_p_value(values['pg_ies_p'])})."
            ),

            (
                "These secondary analyses should be interpreted alongside "
                "the separate accuracy and reaction-time models rather than "
                "as replacements for the primary outcomes."
            ),
        ]

    def build_interpretation(
        self,
        values: dict,
    ) -> list[str]:

        return [
            (
                "Hypothesis 3 was partially supported."
            ),

            (
                "Positive emotional induction did not improve response "
                "accuracy relative to either the neutral or negative condition."
            ),

            (
                "However, participants responded substantially faster under "
                "positive emotion than under the neutral condition, with an "
                f"estimated reaction-time reduction of "
                f"{abs(values['pn_rt_change']):.1f}%. "
                "This improvement in response speed occurred without a "
                "statistically detectable loss of accuracy."
            ),

            (
                "The positive condition did not significantly outperform the "
                "negative condition in either accuracy or reaction time. "
                "Therefore, the observed facilitation cannot be interpreted "
                "as a valence-specific advantage of positive emotion."
            ),

            (
                "Overall, positive emotional induction enhanced processing "
                "speed relative to the neutral baseline but did not produce a "
                "generalized improvement in working-memory performance across "
                "both comparator conditions."
            ),
        ]

    # ==================================================================
    # COMPLETE REPORT
    # ==================================================================

    def build_content(
        self,
    ) -> ReportContent:

        values = self.extract_values()

        return ReportContent(
            title=self.title,

            subtitle=self.subtitle,

            hypothesis=(
                "Positive emotional induction improves working-memory "
                "performance relative to neutral and negative emotional "
                "conditions."
            ),

            sections=[
                ReportSection(
                    title="Method",

                    paragraphs=(
                        self.build_method(
                            values
                        )
                    ),
                ),

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
                                        "across emotional conditions."
                                    ),
                                    data=(
                                        self.build_accuracy_descriptive_table()
                                    ),
                                ),

                                ReportTable(
                                    caption=(
                                        "Table 2. Planned GEE contrasts "
                                        "for response accuracy."
                                    ),
                                    data=(
                                        self.build_accuracy_model_table(
                                            values
                                        )
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
                                        "time across emotional conditions."
                                    ),
                                    data=(
                                        self.build_rt_descriptive_table()
                                    ),
                                ),

                                ReportTable(
                                    caption=(
                                        "Table 4. Planned mixed-effects "
                                        "contrasts for log reaction time."
                                    ),
                                    data=(
                                        self.build_rt_model_table(
                                            values
                                        )
                                    ),
                                ),
                            ],
                        ),

                        ReportSubsection(
                            title="Processing Efficiency",

                            paragraphs=(
                                self.build_efficiency_results(
                                    values
                                )
                            ),

                            tables=[
                                ReportTable(
                                    caption=(
                                        "Table 5. Paired inverse-efficiency "
                                        "comparisons."
                                    ),
                                    data=(
                                        self.build_efficiency_table(
                                            values
                                        )
                                    ),
                                ),
                            ],
                        ),
                    ],
                ),

                ReportSection(
                    title="Decision Rules",

                    bullets=[
                        (
                            "H3 is supported if positive emotion improves "
                            "performance relative to both neutral and negative "
                            "conditions."
                        ),

                        (
                            "H3 is partially supported if positive emotion "
                            "improves only one primary outcome or improves "
                            "performance relative to only one comparator."
                        ),

                        (
                            "H3 is not supported if positive emotion produces "
                            "no reliable performance advantage relative to "
                            "either comparator."
                        ),
                    ],
                ),

                ReportSection(
                    title="Interpretation",

                    paragraphs=(
                        self.build_interpretation(
                            values
                        )
                    ),
                ),

                ReportSection(
                    title="Hypothesis Assessment",

                    paragraphs=[
                        (
                            "Conclusion: Hypothesis 3 was partially supported. "
                            "Positive emotional induction significantly "
                            "improved response speed relative to the neutral "
                            "condition, but it did not improve accuracy and did "
                            "not significantly outperform the negative "
                            "condition."
                        )
                    ],
                ),
            ],
        )