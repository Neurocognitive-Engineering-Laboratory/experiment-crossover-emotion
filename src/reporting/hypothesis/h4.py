"""
Hypothesis 4 scientific report.

Hypothesis:
The effect of emotional condition on working-memory performance varies
according to cognitive load across the 1-back, 2-back, 3-back,
and 4-back levels.
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
)


class Hypothesis4Report(
    BaseHypothesisReport
):
    """
    Generate the final scientific report for Hypothesis 4.
    """

    report_number = 4

    title = (
        "Hypothesis 4 - Emotional Condition × Cognitive Load "
        "on Working-Memory Performance"
    )

    subtitle = (
        "Confirmatory Hypothesis Report"
    )

    output_filename = (
        "hypothesis_04_report"
    )

    input_files = {
        "sample":
            cfg.TABLES_DIR
            / "hypothesis_04"
            / "h4_sample.csv",

        "accuracy_descriptive":
            cfg.TABLES_DIR
            / "hypothesis_04"
            / "h4_accuracy_descriptive.csv",

        "accuracy_model":
            cfg.TABLES_DIR
            / "hypothesis_04"
            / "h4_accuracy_model.csv",

        "accuracy_interactions":
            cfg.TABLES_DIR
            / "hypothesis_04"
            / "h4_accuracy_interactions.csv",

        "accuracy_simple_effects":
            cfg.TABLES_DIR
            / "hypothesis_04"
            / "h4_accuracy_simple_effects.csv",

        "accuracy_global_interaction":
            cfg.TABLES_DIR
            / "hypothesis_04"
            / "h4_accuracy_global_interaction.csv",

        "rt_descriptive":
            cfg.TABLES_DIR
            / "hypothesis_04"
            / "h4_rt_descriptive.csv",

        "rt_model":
            cfg.TABLES_DIR
            / "hypothesis_04"
            / "h4_rt_model.csv",

        "rt_interactions":
            cfg.TABLES_DIR
            / "hypothesis_04"
            / "h4_rt_interactions.csv",

        "rt_simple_effects":
            cfg.TABLES_DIR
            / "hypothesis_04"
            / "h4_rt_simple_effects.csv",

        "rt_global_interaction":
            cfg.TABLES_DIR
            / "hypothesis_04"
            / "h4_rt_global_interaction.csv",

        "summary":
            cfg.TABLES_DIR
            / "hypothesis_04"
            / "h4_summary.csv",
    }

    # ==================================================================
    # RESULT EXTRACTION
    # ==================================================================

    def extract_values(
        self,
    ) -> dict:
        """
        Extract the main H4 results used in the report.
        """

        summary = self.results[
            "summary"
        ]

        accuracy_global = self.results[
            "accuracy_global_interaction"
        ]

        rt_global = self.results[
            "rt_global_interaction"
        ]

        accuracy_interactions = self.results[
            "accuracy_interactions"
        ]

        rt_interactions = self.results[
            "rt_interactions"
        ]

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
            # ACCURACY GLOBAL INTERACTION
            # ----------------------------------------------------------

            "accuracy_global_p":
                float(
                    summary[
                        "accuracy_global_interaction_p"
                    ].iloc[0]
                ),

            "accuracy_global_significant":
                bool(
                    summary[
                        "accuracy_global_interaction_significant"
                    ].iloc[0]
                ),

            "accuracy_significant_terms":
                int(
                    summary[
                        "accuracy_significant_interaction_terms"
                    ].iloc[0]
                ),

            # ----------------------------------------------------------
            # RT GLOBAL INTERACTION
            # ----------------------------------------------------------

            "rt_global_p":
                float(
                    summary[
                        "rt_global_interaction_p"
                    ].iloc[0]
                ),

            "rt_global_significant":
                bool(
                    summary[
                        "rt_global_interaction_significant"
                    ].iloc[0]
                ),

            "rt_significant_terms":
                int(
                    summary[
                        "rt_significant_interaction_terms"
                    ].iloc[0]
                ),

            # ----------------------------------------------------------
            # RAW GLOBAL TEST VALUES
            # ----------------------------------------------------------

            "rt_global_chi2":
                float(
                    rt_global[
                        "chi2"
                    ].iloc[0]
                ),

            "rt_global_df":
                int(
                    rt_global[
                        "df"
                    ].iloc[0]
                ),

            # ----------------------------------------------------------
            # INTERACTION TERM COUNTS
            # ----------------------------------------------------------

            "accuracy_interaction_rows":
                len(
                    accuracy_interactions
                ),

            "rt_interaction_rows":
                len(
                    rt_interactions
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

    def build_sample_table(
        self,
    ) -> pd.DataFrame:
        """
        Build sample distribution table by condition and n-back level.
        """

        table = self.results[
            "sample"
        ].copy()

        table = table.rename(
            columns={
                "emotion_condition":
                    "Condition",

                "nback_level":
                    "N-back",

                "participants":
                    "Participants",

                "trials":
                    "Trials",

                "valid_accuracy":
                    "Valid accuracy",
            }
        )

        return table

    def build_accuracy_descriptive_table(
        self,
    ) -> pd.DataFrame:
        """
        Build descriptive accuracy table by condition × load.
        """

        table = self.results[
            "accuracy_descriptive"
        ].copy()

        table = table.rename(
            columns={
                "emotion_condition":
                    "Condition",

                "nback_level":
                    "N-back",

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

    def build_accuracy_interaction_table(
        self,
    ) -> pd.DataFrame:
        """
        Build accuracy interaction-coefficient table.
        """

        table = self.results[
            "accuracy_interactions"
        ].copy()

        return pd.DataFrame(
            {
                "Term":
                    table[
                        "term"
                    ],

                "Beta":
                    table[
                        "beta"
                    ].map(
                        lambda value:
                        f"{value:.3f}"
                    ),

                "OR":
                    table[
                        "odds_ratio"
                    ].map(
                        lambda value:
                        f"{value:.3f}"
                    ),

                "95% CI":
                    table.apply(
                        lambda row:
                        (
                            "["
                            f"{row['or_ci_low']:.2f}, "
                            f"{row['or_ci_high']:.2f}"
                            "]"
                        ),
                        axis=1,
                    ),

                "p":
                    table[
                        "p"
                    ].map(
                        format_p_value
                    ),
            }
        )

    def build_accuracy_simple_effects_table(
        self,
    ) -> pd.DataFrame:
        """
        Build simple-effect accuracy table across n-back levels.
        """

        table = self.results[
            "accuracy_simple_effects"
        ].copy()

        table = table.sort_values(
            [
                "nback_level",
                "contrast",
            ]
        )

        return pd.DataFrame(
            {
                "N-back":
                    table[
                        "nback_level"
                    ],

                "Contrast":
                    table[
                        "contrast"
                    ],

                "OR":
                    table[
                        "odds_ratio"
                    ].map(
                        lambda value:
                        f"{value:.3f}"
                    ),

                "95% CI":
                    table.apply(
                        lambda row:
                        (
                            "["
                            f"{row['or_ci_low']:.2f}, "
                            f"{row['or_ci_high']:.2f}"
                            "]"
                        ),
                        axis=1,
                    ),

                "p":
                    table[
                        "p"
                    ].map(
                        format_p_value
                    ),
            }
        )

    def build_rt_descriptive_table(
        self,
    ) -> pd.DataFrame:
        """
        Build descriptive RT table by condition × load.
        """

        table = self.results[
            "rt_descriptive"
        ].copy()

        table = table.rename(
            columns={
                "emotion_condition":
                    "Condition",

                "nback_level":
                    "N-back",

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

            table[
                column
            ] = table[
                column
            ].map(
                lambda value:
                f"{value:.2f}"
            )

        return table

    def build_rt_interaction_table(
        self,
    ) -> pd.DataFrame:
        """
        Build RT interaction-coefficient table.
        """

        table = self.results[
            "rt_interactions"
        ].copy()

        return pd.DataFrame(
            {
                "Term":
                    table[
                        "term"
                    ],

                "Beta":
                    table[
                        "beta"
                    ].map(
                        lambda value:
                        f"{value:.3f}"
                    ),

                "RT change":
                    table[
                        "percent_change"
                    ].map(
                        lambda value:
                        f"{value:.1f}%"
                    ),

                "95% CI":
                    table.apply(
                        lambda row:
                        (
                            "["
                            f"{row['percent_ci_low']:.1f}%, "
                            f"{row['percent_ci_high']:.1f}%"
                            "]"
                        ),
                        axis=1,
                    ),

                "p":
                    table[
                        "p"
                    ].map(
                        format_p_value
                    ),
            }
        )

    def build_rt_simple_effects_table(
        self,
    ) -> pd.DataFrame:
        """
        Build simple-effect RT table across n-back levels.
        """

        table = self.results[
            "rt_simple_effects"
        ].copy()

        table = table.sort_values(
            [
                "nback_level",
                "contrast",
            ]
        )

        return pd.DataFrame(
            {
                "N-back":
                    table[
                        "nback_level"
                    ],

                "Contrast":
                    table[
                        "contrast"
                    ],

                "RT change":
                    table[
                        "percent_change"
                    ].map(
                        lambda value:
                        f"{value:.1f}%"
                    ),

                "95% CI":
                    table.apply(
                        lambda row:
                        (
                            "["
                            f"{row['percent_ci_low']:.1f}%, "
                            f"{row['percent_ci_high']:.1f}%"
                            "]"
                        ),
                        axis=1,
                    ),

                "p":
                    table[
                        "p"
                    ].map(
                        format_p_value
                    ),
            }
        )

    def build_global_interaction_table(
        self,
        values: dict,
    ) -> pd.DataFrame:
        """
        Summarize the two global Emotion × N-back interaction tests.
        """

        return pd.DataFrame(
            {
                "Outcome": [
                    "Accuracy",
                    "Reaction Time",
                ],

                "Global interaction p": [
                    format_p_value(
                        values[
                            "accuracy_global_p"
                        ]
                    ),
                    format_p_value(
                        values[
                            "rt_global_p"
                        ]
                    ),
                ],

                "Significant": [
                    (
                        "Yes"
                        if values[
                            "accuracy_global_significant"
                        ]
                        else "No"
                    ),
                    (
                        "Yes"
                        if values[
                            "rt_global_significant"
                        ]
                        else "No"
                    ),
                ],

                "Significant interaction terms": [
                    values[
                        "accuracy_significant_terms"
                    ],
                    values[
                        "rt_significant_terms"
                    ],
                ],
            }
        )

    # ==================================================================
    # TEXT — METHOD
    # ==================================================================

    def build_method(
        self,
        values: dict,
    ) -> list[str]:

        return [
            (
                "A confirmatory interaction analysis was conducted to "
                "evaluate whether the effect of emotional condition on "
                "working-memory performance varied as a function of "
                "cognitive load. The analytical sample included "
                f"{values['participants']} participants."
            ),

            (
                "Emotional condition comprised Neutral, Positive, and "
                "Negative levels, while cognitive load was represented by "
                "the 1-back, 2-back, 3-back, and 4-back task levels. "
                "The primary inferential term was the interaction between "
                "emotional condition and n-back level."
            ),

            (
                "Response accuracy was analyzed using a generalized "
                "estimating equation (GEE) model with a binomial "
                "distribution, logit link, exchangeable within-participant "
                "correlation structure, and robust standard errors. "
                "The accuracy analysis included "
                f"{values['accuracy_observations']:,} trial-level "
                "observations."
            ),

            (
                "Reaction time was analyzed among valid correct-response "
                "trials. Because reaction-time values were positively "
                "skewed, reaction time was log-transformed. A linear "
                "mixed-effects model was fitted with emotional condition, "
                "n-back level, and their interaction as fixed effects, "
                "together with participant-specific random intercepts. "
                "The reaction-time analysis included "
                f"{values['rt_observations']:,} observations."
            ),

            (
                "The global Emotion × N-back interaction for accuracy was "
                "evaluated using a Wald test. For reaction time, the full "
                "interaction mixed-effects model was compared with an "
                "additive model using a likelihood-ratio test under maximum "
                "likelihood estimation. Significant interactions were "
                "followed by planned simple-effect analyses comparing "
                "Positive versus Neutral, Negative versus Neutral, and "
                "Positive versus Negative at each n-back level."
            ),

            (
                "GEE coefficients were exponentiated and interpreted as "
                "odds ratios. Log reaction-time coefficients were converted "
                "to percentage changes in reaction time. Statistical "
                "significance was evaluated using a two-sided alpha level "
                "of .05, with 95% confidence intervals reported."
            ),
        ]

    # ==================================================================
    # TEXT — ACCURACY
    # ==================================================================

    def build_accuracy_results(
        self,
        values: dict,
    ) -> list[str]:

        if values[
            "accuracy_global_significant"
        ]:

            global_text = (
                "The global Emotion × N-back interaction for response "
                "accuracy was statistically significant "
                f"(p {format_p_value(values['accuracy_global_p'])}). "
                "This indicates that the association between emotional "
                "condition and accuracy varied across levels of cognitive "
                "load."
            )

        else:

            global_text = (
                "The global Emotion × N-back interaction for response "
                "accuracy was not statistically significant "
                f"(p {format_p_value(values['accuracy_global_p'])})."
            )

        return [
            global_text,

            (
                f"Among the interaction coefficients, "
                f"{values['accuracy_significant_terms']} terms reached "
                "the predefined alpha level of .05."
            ),

            (
                "The descriptive and simple-effect analyses were therefore "
                "used to characterize how the emotional-condition contrasts "
                "changed from 1-back through 4-back. Because interaction "
                "coefficients are conditional on the model reference levels, "
                "interpretation focuses primarily on the planned simple "
                "effects within each cognitive-load level."
            ),
        ]

    # ==================================================================
    # TEXT — RT
    # ==================================================================

    def build_rt_results(
        self,
        values: dict,
    ) -> list[str]:

        if values[
            "rt_global_significant"
        ]:

            global_text = (
                "The global Emotion × N-back interaction for reaction time "
                "was statistically significant "
                f"(likelihood-ratio chi-square({values['rt_global_df']}) = "
                f"{values['rt_global_chi2']:.2f}, "
                f"p {format_p_value(values['rt_global_p'])}). "
                "Thus, the magnitude of the emotional effect on response "
                "speed varied across cognitive-load levels."
            )

        else:

            global_text = (
                "The global Emotion × N-back interaction for reaction time "
                "was not statistically significant "
                f"(likelihood-ratio chi-square({values['rt_global_df']}) = "
                f"{values['rt_global_chi2']:.2f}, "
                f"p {format_p_value(values['rt_global_p'])})."
            )

        return [
            global_text,

            (
                f"A total of {values['rt_significant_terms']} individual "
                "reaction-time interaction terms reached the predefined "
                "alpha level."
            ),

            (
                "Simple-effect analyses examined the percentage change in "
                "reaction time for each emotional-condition contrast at "
                "each n-back level. Negative percentage values indicate "
                "faster responding for the first condition in the contrast, "
                "whereas positive values indicate slower responding."
            ),
        ]

    # ==================================================================
    # SIMPLE EFFECT SUMMARY
    # ==================================================================

    def build_simple_effect_summary(
        self,
        outcome: str,
    ) -> list[str]:
        """
        Generate a compact level-by-level summary of significant simple effects.
        """

        if outcome == "accuracy":

            table = self.results[
                "accuracy_simple_effects"
            ]

            effect_column = (
                "odds_ratio"
            )

        elif outcome == "rt":

            table = self.results[
                "rt_simple_effects"
            ]

            effect_column = (
                "percent_change"
            )

        else:

            raise ValueError(
                "Outcome must be "
                "'accuracy' or 'rt'."
            )

        significant = table.loc[
            table[
                "p"
            ] < cfg.ALPHA
        ].copy()

        if significant.empty:

            return [
                (
                    "No planned simple-effect contrast reached statistical "
                    "significance at any n-back level."
                )
            ]

        paragraphs = []

        for level in sorted(
            significant[
                "nback_level"
            ].unique()
        ):

            level_data = (
                significant.loc[
                    significant[
                        "nback_level"
                    ] == level
                ]
            )

            effects = []

            for _, row in (
                level_data.iterrows()
            ):

                if outcome == "accuracy":

                    effect_text = (
                        f"{row['contrast']} "
                        f"(OR = {row[effect_column]:.2f}, "
                        f"p {format_p_value(row['p'])})"
                    )

                else:

                    effect_text = (
                        f"{row['contrast']} "
                        f"(RT change = "
                        f"{row[effect_column]:.1f}%, "
                        f"p {format_p_value(row['p'])})"
                    )

                effects.append(
                    effect_text
                )

            paragraphs.append(
                (
                    f"At the {level}-back level, the following planned "
                    f"contrast(s) were statistically significant: "
                    + "; ".join(
                        effects
                    )
                    + "."
                )
            )

        return paragraphs

    # ==================================================================
    # INTERPRETATION
    # ==================================================================

    def build_interpretation(
        self,
        values: dict,
    ) -> list[str]:

        if (
            values[
                "accuracy_global_significant"
            ]
            and values[
                "rt_global_significant"
            ]
        ):

            support_text = (
                "Hypothesis 4 was supported."
            )

        elif (
            values[
                "accuracy_global_significant"
            ]
            or values[
                "rt_global_significant"
            ]
        ):

            support_text = (
                "Hypothesis 4 was partially supported."
            )

        else:

            support_text = (
                "Hypothesis 4 was not supported."
            )

        return [
            support_text,

            (
                "The central prediction of Hypothesis 4 was that emotional "
                "effects on working-memory performance would depend on "
                "cognitive load rather than remaining constant across the "
                "1-back through 4-back levels."
            ),

            (
                "The interaction analyses indicate whether this "
                "load-dependent modulation occurred independently for "
                "accuracy and reaction time. Significant global interactions "
                "provide evidence that the magnitude or direction of the "
                "emotional-condition effect changed as task demands increased."
            ),

            (
                "The simple-effect analyses clarify this interaction by "
                "identifying the specific n-back levels and emotional "
                "contrasts responsible for the overall pattern. Accordingly, "
                "the H4 results should be interpreted in terms of both the "
                "global interaction tests and the level-specific contrasts, "
                "rather than from isolated interaction coefficients alone."
            ),
        ]

    # ==================================================================
    # COMPLETE REPORT
    # ==================================================================

    def build_content(
        self,
    ) -> ReportContent:

        values = (
            self.extract_values()
        )

        accuracy_simple_text = (
            self.build_simple_effect_summary(
                "accuracy"
            )
        )

        rt_simple_text = (
            self.build_simple_effect_summary(
                "rt"
            )
        )

        return ReportContent(
            title=self.title,

            subtitle=self.subtitle,

            hypothesis=(
                "The effect of emotional condition on working-memory "
                "performance varies according to cognitive load across "
                "the 1-back, 2-back, 3-back, and 4-back levels."
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
                # SAMPLE
                # --------------------------------------------------

                ReportSection(
                    title="Analytical Sample",

                    paragraphs=[
                        (
                            "The distribution of participants and trials "
                            "across emotional conditions and n-back levels "
                            "is summarized below."
                        )
                    ],

                    tables=[
                        ReportTable(
                            caption=(
                                "Table 1. Analytical sample by emotional "
                                "condition and cognitive-load level."
                            ),

                            data=(
                                self.build_sample_table()
                            ),
                        )
                    ],
                ),

                # --------------------------------------------------
                # RESULTS
                # --------------------------------------------------

                ReportSection(
                    title="Results",

                    subsections=[
                        # ------------------------------------------
                        # ACCURACY
                        # ------------------------------------------

                        ReportSubsection(
                            title="Accuracy",

                            paragraphs=(
                                self.build_accuracy_results(
                                    values
                                )
                                +
                                accuracy_simple_text
                            ),

                            tables=[
                                ReportTable(
                                    caption=(
                                        "Table 2. Descriptive accuracy "
                                        "by emotional condition and "
                                        "n-back level."
                                    ),

                                    data=(
                                        self.build_accuracy_descriptive_table()
                                    ),
                                ),

                                ReportTable(
                                    caption=(
                                        "Table 3. Emotion × cognitive-load "
                                        "interaction coefficients for "
                                        "response accuracy."
                                    ),

                                    data=(
                                        self.build_accuracy_interaction_table()
                                    ),
                                ),

                                ReportTable(
                                    caption=(
                                        "Table 4. Planned simple effects "
                                        "for response accuracy at each "
                                        "n-back level."
                                    ),

                                    data=(
                                        self.build_accuracy_simple_effects_table()
                                    ),
                                ),
                            ],
                        ),

                        # ------------------------------------------
                        # RT
                        # ------------------------------------------

                        ReportSubsection(
                            title="Reaction Time",

                            paragraphs=(
                                self.build_rt_results(
                                    values
                                )
                                +
                                rt_simple_text
                            ),

                            tables=[
                                ReportTable(
                                    caption=(
                                        "Table 5. Descriptive reaction "
                                        "time by emotional condition and "
                                        "n-back level."
                                    ),

                                    data=(
                                        self.build_rt_descriptive_table()
                                    ),
                                ),

                                ReportTable(
                                    caption=(
                                        "Table 6. Emotion × cognitive-load "
                                        "interaction coefficients for "
                                        "log reaction time."
                                    ),

                                    data=(
                                        self.build_rt_interaction_table()
                                    ),
                                ),

                                ReportTable(
                                    caption=(
                                        "Table 7. Planned simple effects "
                                        "for reaction time at each "
                                        "n-back level."
                                    ),

                                    data=(
                                        self.build_rt_simple_effects_table()
                                    ),
                                ),
                            ],
                        ),

                        # ------------------------------------------
                        # GLOBAL TEST SUMMARY
                        # ------------------------------------------

                        ReportSubsection(
                            title=(
                                "Global Interaction Summary"
                            ),

                            paragraphs=[
                                (
                                    "The global interaction tests summarize "
                                    "whether emotional effects varied across "
                                    "cognitive-load levels for each primary "
                                    "outcome."
                                )
                            ],

                            tables=[
                                ReportTable(
                                    caption=(
                                        "Table 8. Summary of global "
                                        "Emotion × N-back interaction tests."
                                    ),

                                    data=(
                                        self.build_global_interaction_table(
                                            values
                                        )
                                    ),
                                )
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
                            "H4 is supported if the Emotion × N-back "
                            "interaction is statistically significant for "
                            "both primary outcomes."
                        ),

                        (
                            "H4 is partially supported if the interaction "
                            "is statistically significant for only one "
                            "primary outcome."
                        ),

                        (
                            "H4 is not supported if neither global interaction "
                            "test is statistically significant."
                        ),

                        (
                            "Simple-effect analyses are used to characterize "
                            "the load-dependent pattern and are not treated "
                            "as substitutes for the global interaction tests."
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
                            "Conclusion: "
                            f"Hypothesis 4 was "
                            f"{values['assessment']}. "
                            "The results indicate whether the influence "
                            "of emotional condition on working-memory "
                            "performance changed as cognitive load increased "
                            "from 1-back to 4-back."
                        )
                    ],
                ),
            ],
        )