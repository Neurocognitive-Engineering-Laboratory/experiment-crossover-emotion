"""
Hypothesis 2 scientific report.

Hypothesis:
Negative emotional induction leads to poorer working-memory performance
relative to the neutral emotional condition.
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
    find_model_contrast,
    format_p_value,
    format_percent,
    get_condition_row,
)


class Hypothesis2Report(
    BaseHypothesisReport
):
    """
    Generate the final scientific report for Hypothesis 2.
    """

    report_number = 2

    title = (
        "Hypothesis 2 - Effect of Negative Emotion "
        "on Working-Memory Performance"
    )

    subtitle = (
        "Confirmatory Hypothesis Report"
    )

    output_filename = (
        "hypothesis_02_report"
    )

    input_files = {
        "accuracy_descriptive":
            cfg.TABLES_DIR
            / "hypothesis_02"
            / "h2_accuracy_descriptive.csv",

        "accuracy_model":
            cfg.TABLES_DIR
            / "hypothesis_02"
            / "h2_accuracy_model.csv",

        "rt_descriptive":
            cfg.TABLES_DIR
            / "hypothesis_02"
            / "h2_rt_descriptive.csv",

        "rt_model":
            cfg.TABLES_DIR
            / "hypothesis_02"
            / "h2_rt_model.csv",

        "efficiency_descriptive":
            cfg.TABLES_DIR
            / "hypothesis_02"
            / "h2_efficiency_descriptive.csv",

        "efficiency_test":
            cfg.TABLES_DIR
            / "hypothesis_02"
            / "h2_efficiency_test.csv",

        "summary":
            cfg.TABLES_DIR
            / "hypothesis_02"
            / "h2_summary.csv",
    }

    # ==================================================================
    # RESULT EXTRACTION
    # ==================================================================

    def extract_values(
        self,
    ) -> dict:
        """
        Extract all numerical values required by the report.
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

        efficiency_test = self.results[
            "efficiency_test"
        ]

        summary = self.results[
            "summary"
        ]

        negative_accuracy = (
            get_condition_row(
                accuracy_desc,
                "Negative",
            )
        )

        neutral_accuracy = (
            get_condition_row(
                accuracy_desc,
                "Neutral",
            )
        )

        negative_rt = (
            get_condition_row(
                rt_desc,
                "Negative",
            )
        )

        neutral_rt = (
            get_condition_row(
                rt_desc,
                "Neutral",
            )
        )

        accuracy_contrast = (
            find_model_contrast(
                accuracy_model,
                "Negative",
            )
        )

        rt_contrast = (
            find_model_contrast(
                rt_model,
                "Negative",
            )
        )

        efficiency = (
            efficiency_test.iloc[0]
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

            "negative_accuracy":
                float(
                    negative_accuracy[
                        "accuracy_mean"
                    ]
                ),

            "neutral_accuracy":
                float(
                    neutral_accuracy[
                        "accuracy_mean"
                    ]
                ),

            "negative_accuracy_sd":
                float(
                    negative_accuracy[
                        "accuracy_sd"
                    ]
                ),

            "neutral_accuracy_sd":
                float(
                    neutral_accuracy[
                        "accuracy_sd"
                    ]
                ),

            # ----------------------------------------------------------
            # ACCURACY MODEL
            # ----------------------------------------------------------

            "accuracy_beta":
                float(
                    accuracy_contrast[
                        "beta"
                    ]
                ),

            "accuracy_se":
                float(
                    accuracy_contrast[
                        "se"
                    ]
                ),

            "accuracy_z":
                float(
                    accuracy_contrast[
                        "z"
                    ]
                ),

            "accuracy_p":
                float(
                    accuracy_contrast[
                        "p"
                    ]
                ),

            "accuracy_or":
                float(
                    accuracy_contrast[
                        "odds_ratio"
                    ]
                ),

            "accuracy_ci_low":
                float(
                    accuracy_contrast[
                        "or_ci_low"
                    ]
                ),

            "accuracy_ci_high":
                float(
                    accuracy_contrast[
                        "or_ci_high"
                    ]
                ),

            # ----------------------------------------------------------
            # RT DESCRIPTIVE
            # ----------------------------------------------------------

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

            "negative_median_rt":
                float(
                    negative_rt[
                        "median_rt"
                    ]
                ),

            "neutral_median_rt":
                float(
                    neutral_rt[
                        "median_rt"
                    ]
                ),

            # ----------------------------------------------------------
            # RT MODEL
            # ----------------------------------------------------------

            "rt_beta":
                float(
                    rt_contrast[
                        "beta"
                    ]
                ),

            "rt_se":
                float(
                    rt_contrast[
                        "se"
                    ]
                ),

            "rt_z":
                float(
                    rt_contrast[
                        "z"
                    ]
                ),

            "rt_p":
                float(
                    rt_contrast[
                        "p"
                    ]
                ),

            "rt_percent_change":
                float(
                    rt_contrast[
                        "percent_change"
                    ]
                ),

            "rt_ci_low":
                float(
                    rt_contrast[
                        "percent_ci_low"
                    ]
                ),

            "rt_ci_high":
                float(
                    rt_contrast[
                        "percent_ci_high"
                    ]
                ),

            # ----------------------------------------------------------
            # PROCESSING EFFICIENCY
            # ----------------------------------------------------------

            "efficiency_n":
                int(
                    efficiency[
                        "n"
                    ]
                ),

            "neutral_ies":
                float(
                    efficiency[
                        "neutral_mean"
                    ]
                ),

            "negative_ies":
                float(
                    efficiency[
                        "negative_mean"
                    ]
                ),

            "ies_difference":
                float(
                    efficiency[
                        "mean_difference"
                    ]
                ),

            "ies_t":
                float(
                    efficiency[
                        "t"
                    ]
                ),

            "ies_p":
                float(
                    efficiency[
                        "p"
                    ]
                ),

            # ----------------------------------------------------------
            # FINAL ASSESSMENT
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
        """
        Build report-ready descriptive accuracy table.
        """

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

        table[
            "Accuracy"
        ] = table[
            "Accuracy"
        ].map(
            format_percent
        )

        table[
            "SD"
        ] = table[
            "SD"
        ].map(
            lambda value:
            f"{value:.3f}"
        )

        return table

    def build_accuracy_model_table(
        self,
        values: dict,
    ) -> pd.DataFrame:
        """
        Build the Negative vs Neutral accuracy model table.
        """

        return pd.DataFrame(
            {
                "Contrast": [
                    "Negative vs Neutral"
                ],

                "Beta": [
                    f"{values['accuracy_beta']:.3f}"
                ],

                "OR": [
                    f"{values['accuracy_or']:.3f}"
                ],

                "95% CI": [
                    (
                        "["
                        f"{values['accuracy_ci_low']:.2f}, "
                        f"{values['accuracy_ci_high']:.2f}"
                        "]"
                    )
                ],

                "p": [
                    format_p_value(
                        values[
                            "accuracy_p"
                        ]
                    )
                ],
            }
        )

    def build_rt_descriptive_table(
        self,
    ) -> pd.DataFrame:
        """
        Build report-ready reaction-time descriptive table.
        """

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
        """
        Build report-ready reaction-time model table.
        """

        return pd.DataFrame(
            {
                "Contrast": [
                    "Negative vs Neutral"
                ],

                "Beta": [
                    f"{values['rt_beta']:.3f}"
                ],

                "RT change": [
                    (
                        f"{values['rt_percent_change']:.1f}%"
                    )
                ],

                "95% CI": [
                    (
                        "["
                        f"{values['rt_ci_low']:.1f}%, "
                        f"{values['rt_ci_high']:.1f}%"
                        "]"
                    )
                ],

                "p": [
                    format_p_value(
                        values[
                            "rt_p"
                        ]
                    )
                ],
            }
        )

    def build_efficiency_table(
        self,
        values: dict,
    ) -> pd.DataFrame:
        """
        Build report-ready processing-efficiency test table.
        """

        return pd.DataFrame(
            {
                "Comparison": [
                    "Negative vs Neutral"
                ],

                "N": [
                    values[
                        "efficiency_n"
                    ]
                ],

                "Neutral IES": [
                    f"{values['neutral_ies']:.2f}"
                ],

                "Negative IES": [
                    f"{values['negative_ies']:.2f}"
                ],

                "Difference": [
                    f"{values['ies_difference']:.2f}"
                ],

                "t": [
                    f"{values['ies_t']:.2f}"
                ],

                "p": [
                    format_p_value(
                        values[
                            "ies_p"
                        ]
                    )
                ],
            }
        )

    # ==================================================================
    # METHOD
    # ==================================================================

    def build_method(
        self,
        values: dict,
    ) -> list[str]:

        return [
            (
                "A confirmatory trial-level analysis was conducted to "
                "determine whether negative emotional induction impaired "
                "working-memory performance relative to the neutral "
                "condition. The analytical sample included "
                f"{values['participants']} participants."
            ),

            (
                "The primary outcomes were response accuracy and reaction "
                "time. Accuracy was analyzed using a generalized estimating "
                "equation (GEE) model with a binomial distribution, logit "
                "link, exchangeable within-participant correlation structure, "
                "and robust standard errors. Emotional condition was entered "
                "as the predictor, with the neutral condition specified as "
                "the reference category. The accuracy analysis included "
                f"{values['accuracy_observations']:,} trial-level observations."
            ),

            (
                "Reaction time was analyzed among valid correct-response "
                "trials only. Because reaction-time values were positively "
                "skewed, reaction time was log-transformed before modeling. "
                "A linear mixed-effects model was fitted with emotional "
                "condition as a fixed effect and a participant-specific "
                "random intercept. Maximum-likelihood estimation was used. "
                "The reaction-time analysis included "
                f"{values['rt_observations']:,} observations."
            ),

            (
                "Model coefficients from the binomial GEE were exponentiated "
                "and interpreted as odds ratios. Coefficients from the "
                "log reaction-time model were exponentiated and converted "
                "to percentage changes relative to the neutral condition. "
                "Inverse efficiency was additionally examined as a secondary "
                "indicator of the combined speed-accuracy pattern. "
                "Statistical significance was evaluated using a two-sided "
                "alpha level of .05, and 95% confidence intervals are reported."
            ),
        ]

    # ==================================================================
    # ACCURACY RESULTS
    # ==================================================================

    def build_accuracy_results(
        self,
        values: dict,
    ) -> list[str]:

        percentage_difference = (
            (
                values[
                    "negative_accuracy"
                ]
                -
                values[
                    "neutral_accuracy"
                ]
            )
            * 100
        )

        return [
            (
                "Mean trial-level accuracy was "
                f"{format_percent(values['negative_accuracy'])} "
                "in the negative condition and "
                f"{format_percent(values['neutral_accuracy'])} "
                "in the neutral condition. The descriptive difference "
                f"was {percentage_difference:.1f} percentage points."
            ),

            (
                "Relative to the neutral condition, negative emotion was "
                "associated with a small reduction in the estimated odds "
                "of a correct response "
                f"(beta = {values['accuracy_beta']:.3f}, "
                f"SE = {values['accuracy_se']:.3f}, "
                f"z = {values['accuracy_z']:.2f}, "
                f"p {format_p_value(values['accuracy_p'])}). "
                "The corresponding odds ratio was "
                f"{values['accuracy_or']:.3f} "
                "(95% CI "
                f"[{values['accuracy_ci_low']:.2f}, "
                f"{values['accuracy_ci_high']:.2f}])."
            ),

            (
                "The confidence interval included the null value of 1.00, "
                "and the comparison was not statistically significant. "
                "Therefore, the analysis did not provide sufficient evidence "
                "that negative emotional induction reduced response accuracy "
                "relative to the neutral condition."
            ),
        ]

    # ==================================================================
    # RT RESULTS
    # ==================================================================

    def build_rt_results(
        self,
        values: dict,
    ) -> list[str]:

        change = values[
            "rt_percent_change"
        ]

        if change < 0:

            direction = "lower"
            behavioral_direction = "faster"

        else:

            direction = "higher"
            behavioral_direction = "slower"

        return [
            (
                "Mean reaction time was "
                f"{values['negative_mean_rt']:.1f} ms "
                "in the negative condition and "
                f"{values['neutral_mean_rt']:.1f} ms "
                "in the neutral condition."
            ),

            (
                "The negative emotional condition was significantly "
                f"associated with {direction} log reaction time relative "
                "to the neutral condition "
                f"(beta = {values['rt_beta']:.3f}, "
                f"SE = {values['rt_se']:.3f}, "
                f"z = {values['rt_z']:.2f}, "
                f"p {format_p_value(values['rt_p'])})."
            ),

            (
                "After back-transformation, reaction time under negative "
                "emotion was estimated to be "
                f"{abs(change):.1f}% {direction} "
                "than under the neutral condition "
                "(95% CI "
                f"[{values['rt_ci_low']:.1f}%, "
                f"{values['rt_ci_high']:.1f}%]). "
                "Thus, participants responded significantly "
                f"{behavioral_direction}, rather than more slowly, "
                "during the negative emotional condition."
            ),
        ]

    # ==================================================================
    # PROCESSING EFFICIENCY
    # ==================================================================

    def build_efficiency_results(
        self,
        values: dict,
    ) -> list[str]:

        significant = (
            values[
                "ies_p"
            ]
            < cfg.ALPHA
        )

        lower_ies = (
            values[
                "negative_ies"
            ]
            <
            values[
                "neutral_ies"
            ]
        )

        if significant and lower_ies:

            interpretation = (
                "Negative emotion was associated with significantly "
                "better combined processing efficiency."
            )

        elif significant:

            interpretation = (
                "Negative emotion was associated with significantly "
                "poorer combined processing efficiency."
            )

        else:

            interpretation = (
                "The inverse-efficiency comparison was not statistically "
                "significant."
            )

        return [
            (
                "Inverse efficiency was examined as a secondary measure "
                "combining reaction speed and response accuracy. Mean IES "
                "was "
                f"{values['negative_ies']:.2f} under negative emotion and "
                f"{values['neutral_ies']:.2f} under the neutral condition."
            ),

            (
                "The paired comparison yielded a mean difference of "
                f"{values['ies_difference']:.2f}, "
                f"t = {values['ies_t']:.2f}, "
                f"p {format_p_value(values['ies_p'])}. "
                f"{interpretation}"
            ),
        ]

    # ==================================================================
    # INTERPRETATION
    # ==================================================================

    def build_interpretation(
        self,
        values: dict,
    ) -> list[str]:

        return [
            (
                "Hypothesis 2 was not supported."
            ),

            (
                "The hypothesis predicted that negative emotional induction "
                "would impair working-memory performance relative to the "
                "neutral condition."
            ),

            (
                "Although response accuracy was descriptively lower under "
                "negative emotion, the difference was small and statistically "
                "non-significant. Therefore, there was no reliable evidence "
                "that negative emotion decreased the probability of producing "
                "a correct response."
            ),

            (
                "Reaction-time results were opposite to the predicted "
                "impairment pattern. Rather than responding more slowly, "
                "participants responded approximately "
                f"{abs(values['rt_percent_change']):.1f}% faster under "
                "negative emotion than under the neutral condition."
            ),

            (
                "The combination of significantly faster responses and a "
                "small, non-significant reduction in accuracy may be "
                "descriptively compatible with a shift toward faster "
                "responding. However, it does not provide strong evidence "
                "of a speed-accuracy trade-off because the reduction in "
                "accuracy was not statistically supported."
            ),

            (
                "Overall, negative emotional induction altered response "
                "speed but did not produce the expected deterioration in "
                "working-memory performance."
            ),
        ]

    # ==================================================================
    # COMPLETE CONTENT
    # ==================================================================

    def build_content(
        self,
    ) -> ReportContent:

        values = (
            self.extract_values()
        )

        return ReportContent(
            title=self.title,

            subtitle=self.subtitle,

            hypothesis=(
                "Negative emotional induction leads to poorer "
                "working-memory performance relative to the "
                "neutral emotional condition."
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
                                        "under neutral and negative emotion."
                                    ),

                                    data=(
                                        self.build_accuracy_descriptive_table()
                                    ),
                                ),

                                ReportTable(
                                    caption=(
                                        "Table 2. Binomial GEE estimate "
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
                                        "time under neutral and negative "
                                        "emotion."
                                    ),

                                    data=(
                                        self.build_rt_descriptive_table()
                                    ),
                                ),

                                ReportTable(
                                    caption=(
                                        "Table 4. Mixed-effects model "
                                        "estimate for log reaction time."
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
                                        "comparison."
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

                # --------------------------------------------------
                # DECISION RULES
                # --------------------------------------------------

                ReportSection(
                    title="Decision Rules",

                    bullets=[
                        (
                            "H2 is supported if negative emotion is "
                            "associated with significantly lower accuracy, "
                            "significantly slower reaction time, or both."
                        ),

                        (
                            "H2 is partially supported if only one impairment "
                            "outcome is statistically supported or if there "
                            "is clear evidence of a speed-accuracy trade-off."
                        ),

                        (
                            "H2 is not supported if negative emotion does "
                            "not significantly reduce accuracy and responses "
                            "are not significantly slower than under neutral "
                            "emotion."
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
                # FINAL ASSESSMENT
                # --------------------------------------------------

                ReportSection(
                    title="Hypothesis Assessment",

                    paragraphs=[
                        (
                            "Conclusion: Hypothesis 2 was not supported. "
                            "Negative emotion did not significantly reduce "
                            "response accuracy and was associated with faster, "
                            "rather than slower, reaction times relative to "
                            "the neutral condition."
                        )
                    ],
                ),
            ],
        )