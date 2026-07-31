# Hypothesis 2 Report

## Hypothesis

Negative emotion induction leads to decreased working-memory performance compared with the neutral emotional condition.

---

## Method

### Analytical objective

This analysis examined whether negative emotion induction impaired working-memory performance relative to the neutral condition.

A secondary objective was to determine whether the negative condition produced a speed–accuracy trade-off.

### Study design

The analysis used repeated observations from the crossover experiment. Participant-level dependency was accounted for through `[mixed-effects modeling/GEE]`.

### Sample

The analysis included participants with valid observations in the negative and neutral conditions.

The final analytical sample consisted of `[N]` participants, `[N]` negative-condition observations, and `[N]` neutral-condition observations.

### Variables

The exposure variable was emotional condition, restricted to:

* negative;
* neutral.

The outcomes were:

* accuracy;
* calibrated reaction time.

Accuracy was represented as `[trial-level binary response/proportion of correct responses]`.

Reaction time was calculated using `[correct trials/all valid response trials]`.

The speed–accuracy relationship was evaluated by jointly interpreting changes in accuracy and reaction time. A secondary inverse-efficiency score was calculated as:

```text
Inverse efficiency score =
Mean reaction time / Proportion of correct responses
```

Higher inverse-efficiency values indicated poorer combined performance.

### Statistical analysis

Accuracy was modeled using:

```text
Accuracy ~ Negative versus neutral condition
```

Reaction time was modeled using:

```text
Reaction time ~ Negative versus neutral condition
                    + (1 | Participant)
```

Adjusted models included:

* n-back level;
* session;
* sequence;
* intervention order;
* motor delay;
* keyboard latency;
* demographic variables;
* emotion-regulation scores.

The negative-condition coefficient represented the estimated difference relative to the neutral reference condition.

For the accuracy model, results were expressed as odds ratios with 95% confidence intervals.

For the reaction-time model, results were expressed as mean differences in milliseconds with 95% confidence intervals.

---

## Results

### Descriptive results

Performance in the negative and neutral conditions was:

| Condition | Accuracy, mean (SD) | Reaction time, mean (SD), ms | Inverse efficiency |
| --------- | ------------------: | ---------------------------: | -----------------: |
| Negative  |           `[value]` |                    `[value]` |          `[value]` |
| Neutral   |           `[value]` |                    `[value]` |          `[value]` |

### Accuracy

Participants in the negative condition showed `[lower/higher/similar]` accuracy compared with the neutral condition.

The estimated effect was:

```text
Estimate = [value]
Odds ratio = [value]
95% CI = [lower, upper]
p = [value]
```

After adjustment for the predefined covariates, the effect `[remained significant/was attenuated/was no longer significant]`.

### Reaction time

Compared with the neutral condition, negative emotion was associated with a reaction-time difference of `[value]` ms, 95% CI `[lower, upper]`, `p = [value]`.

The direction of the effect indicated `[slower/faster/no meaningfully different]` responses under negative emotion.

### Speed–accuracy trade-off

The combined pattern of accuracy and reaction time was consistent with:

`[select one]`

* faster but less accurate responding;
* slower but more accurate responding;
* slower and less accurate responding;
* faster and more accurate responding;
* no clear speed–accuracy trade-off.

The inverse-efficiency score was `[higher/lower/not significantly different]` under negative emotion, with an estimated difference of `[value]`, 95% CI `[lower, upper]`, `p = [value]`.

### Hypothesis assessment

The findings `[supported/partially supported/did not support]` Hypothesis 2.

Negative emotion was associated with `[lower accuracy/slower reaction time/both/neither]` compared with the neutral condition. The observed pattern was most consistent with `[brief factual description]`.
