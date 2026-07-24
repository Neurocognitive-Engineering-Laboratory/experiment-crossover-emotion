## Dependencies

                    config.py
                       │
              configura o projeto
                       │
         ┌─────────────┼─────────────┐
         ▼             ▼             ▼
      utils.py    preprocessing   scoring
         │
         ├─────────────┬─────────────┐
         ▼             ▼             ▼
 visualization       models       notebooks



## Architeture

src/
│
├── __init__.py
│
├── config.py
│
├── utils.py
│
├── preprocessing.py
│
├── scoring.py
│
├── visualization/
│   ├── __init__.py
│   ├── theme.py
│   ├── utils.py
│   ├── univariate.py
│   ├── between.py
│   ├── within.py
│   ├── correlation.py
│   ├── categorical.py
│   ├── model.py
│   └── experimental.py
│
└── models/
    ├── __init__.py
    ├── utils.py
    ├── linear.py
    ├── mixed.py
    ├── binary.py
    ├── moderation.py
    ├── mediation.py
    └── diagnostics.py