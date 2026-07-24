# Emotion Induction Crossover Experiment

This repository contains the data processing, exploratory analysis, statistical modeling, causal mediation/moderation analysis, figures, and reports for a crossover experiment evaluating the effects of emotional induction on cognitive performance.

## Study Design

The study follows a crossover design. Each participant completed two consecutive experimental sessions with a minimum interval of two days between sessions.

Participants were randomized into four categories:

- Category I: Session A followed by Session B
- Category II: Session B followed by Session A
- Category III: Session C followed by Session D
- Category IV: Session D followed by Session C

## Experimental Groups

- Group A: Positive emotion, autobiography first, emotion induction second
- Group B: Negative emotion, autobiography first, emotion induction second
- Group C: Positive emotion, emotion induction first, autobiography second
- Group D: Negative emotion, emotion induction first, autobiography second

## Repository Structure

```text
experiment-crossover-emotion/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── data/
│   ├── raw/
│   ├── interim/
│   ├── processed/
│   └── dictionary/
│
├── notebooks/
│   ├── 00_setup_colab.ipynb
│   ├── 01_data_cleaning.ipynb
│   ├── 02_exploratory_analysis.ipynb
│   ├── 03_manipulation_check.ipynb
│   ├── 04_nback_performance.ipynb
│   ├── 05_mediation_moderation_models.ipynb
│   └── 06_final_results.ipynb
│
├── src/
│   ├── config.py
│   ├── preprocessing.py
│   ├── scoring.py
│   │
│   ├── visualization/
│   │   ├── ggstats_figures.py
│   │   └── causal_diagrams.py
│   │
│   └── models/
│       ├── mixed_models.py
│       ├── mediation.py
│       ├── moderation.py
│       └── moderated_mediation.py
│
├── figures/
│   ├── design/
│   ├── exploratory/
│   ├── manipulation_check/
│   ├── nback/
│   ├── mediation/
│   └── final/
│
├── reports/
│   ├── technical/
│   ├── tables/
│   └── final_report/
│
└── docs/
    │
    ├── 01_study_design.md
    ├── 02_research_questions.md
    ├── 03_hypotheses.md
    ├── 04_variables_and_outcomes.md
    ├── 05_analysis_plan.md
    ├── 06_statistical_models.md
    ├── 07_causal_framework.md
    ├── 08_sensitivity_robustness.md
    │
    ├── data_dictionary/
    │   ├── participants.md
    │   ├── screening.md
    │   ├── sam_vsam.md
    │   ├── nback.md
    │   └── reaction_time.md
    │
    └── diagrams/
        ├── experimental_design.md
        ├── causal_models.md
        └── analysis_workflow.md
```

## Main Outcomes

- n-back accuracy
- n-back reaction time
- state anxiety change
- SAM valence, arousal and dominance
- VSAM valence consistency

## Modeling Strategy

The main statistical strategy includes:

1. Descriptive analysis
2. Manipulation checks
3. Mixed-effects models
4. Mediation analysis
5. Moderation analysis
6. Moderated mediation analysis

## Dataset

The dataset contains information from screening, training and
experimental sessions.

**Screening variables**
- Age
- Gender
- Education
- Hand dominance
- Cognitive Reappraisal
- Expressive Suppression

**Experimental measures**
- Trait anxiety
- State anxiety
- SAM
- VSAM
- Reaction time
- n-back performance

## Analysis Strategy

The analysis workflow consists of:

1. Data validation and preprocessing
2. Exploratory data analysis
3. Manipulation checks
4. Analysis of n-back performance
5. Mixed-effects modeling
6. Mediation analysis
7. Moderation analysis
8. Moderated mediation
9. Sensitivity and robustness analyses

## How to Run

The analyses are primarily executed using Jupyter noteboooks (or Google Colab).

Run the notebooks sequentially:

1. ```00_setup_colab.ipynb```
2. ```01_data_cleaning.ipynb```
3. ```02_exploratory_analysis.ipynb```
4. ```03_manipulation_check.ipynb```
5. ```04_nback_performance.ipynb```
6. ```05_mediation_moderation_models.ipynb```
7. ```06_final_results.ipynb```

## Results

Final figures are stored in:

```figures/final/```

Statistical tables are stored in:

```reports/tables/```

The final analysis report is stored in:

```reports/final_report/```