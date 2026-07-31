# Hypothesis 4 Report

## Hypothesis

The effect of emotional condition on working-memory performance varies according to cognitive load across the 1-back, 2-back, 3-back, and 4-back levels.

---

## Method

### Analytical objective

This analysis evaluated whether cognitive load moderated the relationship between emotional condition and working-memory performance.

### Study design

The analysis used trial-level or block-level repeated observations from the n-back task.

Each participant contributed observations across multiple n-back levels and emotional conditions. The nested structure of observations within participants was accounted for in the statistical models.

### Sample

The analysis included `[N]` participants and `[N]` valid observations distributed across the four n-back levels.

| N-back level | Participants | Valid observations |
| ------------ | -----------: | -----------------: |
| 1-back       |        `[N]` |              `[N]` |
| 2-back       |        `[N]` |              `[N]` |
| 3-back       |        `[N]` |              `[N]` |
| 4-back       |        `[N]` |              `[N]` |

### Variables

The predictors were:

* emotional condition;
* n-back level;
* emotional condition × n-back level interaction.

Emotional condition included:

* positive;
* neutral;
* negative.

Cognitive load was represented by:

* 1-back;
* 2-back;
* 3-back;
* 4-back.

The outcomes were:

* accuracy;
* calibrated reaction time.

The reference categories were:

```text
Emotional condition: [Neutral]
N-back level: [1-back]
```

### Statistical analysis

Accuracy was analyzed using a repeated-measures binomial model:

```text
Accuracy ~ Emotional condition
           * N-back level
```

Reaction time was analyzed using a linear mixed-effects model:

```text
Reaction time ~ Emotional condition
                * N-back level
                + (1 | Participant)
```

The adjusted models included:

* session;
* sequence;
* intervention order;
* motor delay;
* demographic variables;
* cognitive reappraisal;
* expressive suppression.

The primary test was the global emotional condition × n-back level interaction.

Where the interaction was statistically significant, simple effects were estimated:

* emotional-condition comparisons within each n-back level;
* n-back-level comparisons within each emotional condition.

Multiplicity adjustment was performed using `[method]`.

### Interpretation

A statistically significant interaction indicated that the emotional-condition effect differed according to cognitive-load level.

The absence of a significant interaction indicated that differences between emotional conditions were approximately stable across n-back levels.

---

## Results

### Descriptive performance by condition and load

#### Accuracy

| Emotional condition |    1-back |    2-back |    3-back |    4-back |
| ------------------- | --------: | --------: | --------: | --------: |
| Positive            | `[value]` | `[value]` | `[value]` | `[value]` |
| Neutral             | `[value]` | `[value]` | `[value]` | `[value]` |
| Negative            | `[value]` | `[value]` | `[value]` | `[value]` |

#### Reaction time

| Emotional condition |    1-back |    2-back |    3-back |    4-back |
| ------------------- | --------: | --------: | --------: | --------: |
| Positive            | `[value]` | `[value]` | `[value]` | `[value]` |
| Neutral             | `[value]` | `[value]` | `[value]` | `[value]` |
| Negative            | `[value]` | `[value]` | `[value]` | `[value]` |

### Main effect of cognitive load

Cognitive load `[was/was not]` significantly associated with accuracy, `[test statistic] = [value]`, `p = [value]`.

Relative to 1-back:

* 2-back changed performance by `[value]`;
* 3-back changed performance by `[value]`;
* 4-back changed performance by `[value]`.

Cognitive load `[was/was not]` significantly associated with reaction time, `[test statistic] = [value]`, `p = [value]`.

The general pattern showed `[increasing/decreasing/stable]` reaction times as cognitive load increased.

### Emotion × load interaction for accuracy

The emotional condition × n-back level interaction `[was/was not]` statistically significant for accuracy, `[global statistic] = [value]`, `p = [value]`.

At 1-back, `[condition]` showed `[description]`.

At 2-back, `[condition]` showed `[description]`.

At 3-back, `[condition]` showed `[description]`.

At 4-back, `[condition]` showed `[description]`.

The largest emotional-condition contrast occurred at `[n-back level]`, where `[condition A]` differed from `[condition B]` by `[value]`, adjusted `p = [value]`.

### Emotion × load interaction for reaction time

The emotional condition × n-back level interaction `[was/was not]` statistically significant for reaction time, `[global statistic] = [value]`, `p = [value]`.

The estimated emotional effects were:

| N-back level | Positive vs neutral | Negative vs neutral | Positive vs negative |
| ------------ | ------------------: | ------------------: | -------------------: |
| 1-back       |           `[value]` |           `[value]` |            `[value]` |
| 2-back       |           `[value]` |           `[value]` |            `[value]` |
| 3-back       |           `[value]` |           `[value]` |            `[value]` |
| 4-back       |           `[value]` |           `[value]` |            `[value]` |

### Hypothesis assessment

The findings `[supported/partially supported/did not support]` Hypothesis 4.

The effect of emotional condition `[increased/decreased/remained stable]` as cognitive load increased. The clearest moderation pattern occurred at `[n-back level]`, where `[brief factual result]`.
