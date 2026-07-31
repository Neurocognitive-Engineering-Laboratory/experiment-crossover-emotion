# Hypothesis 3 Report

## Hypothesis

Compared with negative and neutral emotional conditions, positive emotion induction improves working-memory performance.

---

## Method

### Analytical objective

This analysis assessed whether positive emotion induction improved working-memory accuracy or optimized reaction time relative to negative and neutral conditions.

### Study design

Repeated observations from the crossover experiment were analyzed while accounting for within-participant correlation.

### Sample

The analysis included `[N]` participants with valid observations under the positive condition and at least one comparator condition.

The number of valid observations was:

| Condition | Participants | Accuracy observations | RT observations |
| --------- | -----------: | --------------------: | --------------: |
| Positive  |        `[N]` |                 `[N]` |           `[N]` |
| Neutral   |        `[N]` |                 `[N]` |           `[N]` |
| Negative  |        `[N]` |                 `[N]` |           `[N]` |

### Variables

The primary predictor was emotional condition.

The positive condition was contrasted separately against:

* neutral emotion;
* negative emotion.

Primary outcomes were:

* response accuracy;
* calibrated reaction time.

Secondary outcomes included:

* inverse-efficiency score;
* omission rate;
* incorrect-response rate.

### Statistical analysis

Accuracy was analyzed using `[binomial GEE/logistic mixed model]`.

Reaction time was analyzed using a linear mixed-effects model with a random intercept for participant.

The models were specified as:

```text
Accuracy ~ Emotional condition
Reaction time ~ Emotional condition + (1 | Participant)
```

The adjusted models additionally included:

```text
n-back level
session
sequence
intervention order
motor delay
age
gender
education
hand dominance
cognitive reappraisal
expressive suppression
```

The primary contrasts were:

```text
Positive − Neutral
Positive − Negative
```

P-values were adjusted for multiple comparisons using `[method]`.

### Decision rule

Evidence of improved working-memory performance required at least one of the following:

* significantly higher accuracy without a meaningful reaction-time penalty;
* significantly faster reaction time without reduced accuracy;
* improvement in both accuracy and reaction time;
* significantly lower inverse-efficiency score.

---

## Results

### Descriptive results

| Condition | Accuracy, mean (SD) | Reaction time, mean (SD), ms | Inverse efficiency |
| --------- | ------------------: | ---------------------------: | -----------------: |
| Positive  |           `[value]` |                    `[value]` |          `[value]` |
| Neutral   |           `[value]` |                    `[value]` |          `[value]` |
| Negative  |           `[value]` |                    `[value]` |          `[value]` |

### Positive versus neutral

For accuracy, the positive condition was associated with `[higher/lower/similar]` performance compared with neutral emotion:

```text
Estimate = [value]
Odds ratio = [value]
95% CI = [lower, upper]
Adjusted p = [value]
```

For reaction time, the positive condition differed from neutral by `[value]` ms, 95% CI `[lower, upper]`, adjusted `p = [value]`.

The inverse-efficiency difference was `[value]`, 95% CI `[lower, upper]`, `p = [value]`.

### Positive versus negative

For accuracy, the positive condition was associated with `[higher/lower/similar]` performance compared with negative emotion:

```text
Estimate = [value]
Odds ratio = [value]
95% CI = [lower, upper]
Adjusted p = [value]
```

For reaction time, the positive condition differed from negative by `[value]` ms, 95% CI `[lower, upper]`, adjusted `p = [value]`.

The inverse-efficiency difference was `[value]`, 95% CI `[lower, upper]`, `p = [value]`.

### Adjusted analysis

After adjustment for experimental order, session, participant characteristics, and emotion-regulation scores, the positive-emotion effect `[remained statistically significant/was attenuated/was no longer statistically significant]`.

The adjusted results indicated `[brief description of the final pattern]`.

### Hypothesis assessment

The results `[supported/partially supported/did not support]` Hypothesis 3.

Positive emotion produced `[higher accuracy/faster reaction times/better combined efficiency/no clear performance improvement]` relative to `[neutral/negative/both comparator conditions]`.
