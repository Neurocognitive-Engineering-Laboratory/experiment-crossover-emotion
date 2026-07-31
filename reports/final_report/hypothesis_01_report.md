# Hypothesis 1 Report

## Hypothesis

Positive, negative, and neutral emotion inductions differentially affect university students’ working-memory performance.

---

## Method

### Analytical objective

This analysis evaluated whether working-memory performance differed across positive, negative, and neutral emotional conditions.

### Study design

The data were obtained from a crossover experimental design in which each participant completed repeated experimental sessions under different emotional conditions. The analyses accounted for the dependency among repeated observations from the same participant.

### Sample

The analytical sample included `[N]` participants and `[N observations/trials]` valid observations after applying the predefined inclusion and exclusion criteria.

Observations were excluded when:

* participant or session identifiers were missing;
* the experimental condition could not be identified;
* reaction-time values were outside the predefined valid range;
* responses were missing or invalid for the outcome under analysis;
* duplicate or technically invalid trials were identified.

### Variables

The primary predictor was emotional condition, classified as:

* positive;
* negative;
* neutral.

The primary working-memory outcomes were:

* response accuracy;
* calibrated reaction time.

Reaction time was expressed in milliseconds and calculated using correct-response trials unless otherwise specified.

Where available, reaction time was adjusted for individual motor delay and keyboard latency.

### Statistical analysis

Accuracy was analyzed using `[binomial GEE/logistic mixed-effects model/other model]`, with emotional condition included as a fixed effect and participant included as the repeated-measures clustering variable.

Reaction time was analyzed using a linear mixed-effects model with emotional condition as a fixed effect and a participant-specific random intercept.

The initial models were specified as:

```text
Accuracy ~ Emotional condition
Reaction time ~ Emotional condition + (1 | Participant)
```

Adjusted models additionally included the prespecified covariates:

* session;
* experimental sequence;
* intervention order;
* age;
* gender;
* education;
* hand dominance;
* cognitive reappraisal;
* expressive suppression.

The reference emotional condition was `[Neutral/Positive/Negative]`.

Pairwise comparisons were performed between:

* positive versus neutral;
* negative versus neutral;
* positive versus negative.

P-values were adjusted using the `[Holm/Bonferroni/FDR]` procedure. Statistical significance was evaluated using an alpha level of `[0.05]`.

Effect estimates were reported with 95% confidence intervals.

---

## Results

### Analytical sample

A total of `[N]` participants contributed `[N]` valid observations to the accuracy analysis and `[N]` valid observations to the reaction-time analysis.

The number of observations by emotional condition was:

| Emotional condition | Participants | Observations |
| ------------------- | -----------: | -----------: |
| Positive            |        `[N]` |        `[N]` |
| Neutral             |        `[N]` |        `[N]` |
| Negative            |        `[N]` |        `[N]` |

### Descriptive results

Mean working-memory performance by emotional condition was:

| Emotional condition | Accuracy, mean (SD) | Reaction time, mean (SD), ms |
| ------------------- | ------------------: | ---------------------------: |
| Positive            |           `[value]` |                    `[value]` |
| Neutral             |           `[value]` |                    `[value]` |
| Negative            |           `[value]` |                    `[value]` |

### Accuracy model

Emotional condition `[was/was not]` significantly associated with response accuracy, `[global test statistic] = [value]`, `p = [value]`.

Compared with the neutral condition:

* the positive condition was associated with `[higher/lower/no meaningful difference in]` accuracy, estimate = `[value]`, odds ratio = `[value]`, 95% CI `[lower, upper]`, `p = [value]`;
* the negative condition was associated with `[higher/lower/no meaningful difference in]` accuracy, estimate = `[value]`, odds ratio = `[value]`, 95% CI `[lower, upper]`, `p = [value]`.

The positive versus negative contrast indicated `[description]`, adjusted `p = [value]`.

### Reaction-time model

Emotional condition `[was/was not]` significantly associated with calibrated reaction time, `[test statistic] = [value]`, `p = [value]`.

Compared with the neutral condition:

* the positive condition changed reaction time by `[value]` ms, 95% CI `[lower, upper]`, `p = [value]`;
* the negative condition changed reaction time by `[value]` ms, 95% CI `[lower, upper]`, `p = [value]`.

The positive versus negative contrast indicated `[description]`, adjusted `p = [value]`.

### Hypothesis assessment

The results `[supported/partially supported/did not support]` Hypothesis 1.

Emotional condition produced `[significant/non-significant]` differences in `[accuracy/reaction time/both outcomes]`. The strongest contrast was observed between `[conditions]`, characterized by `[brief factual description of the result]`.
