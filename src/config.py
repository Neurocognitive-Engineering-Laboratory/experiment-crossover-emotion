"""
Global configuration for the crossover emotion experiment.

Configuration is loaded from environment variables whenever
machine-specific information is required.

Project-wide scientific and statistical constants are defined
below.
"""

from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv


# =====================================================================
# ENVIRONMENT
# =====================================================================

# Location of this file:
# <project>/src/config.py
CONFIG_FILE = Path(__file__).resolve()

# Expected repository root inferred from src/config.py
INFERRED_PROJECT_ROOT = CONFIG_FILE.parents[1]

# Load .env located at the repository root
ENV_FILE = INFERRED_PROJECT_ROOT / ".env"

load_dotenv(
    dotenv_path=ENV_FILE,
    override=False,
)


# =====================================================================
# PROJECT ROOT
# =====================================================================

_project_root_env = os.getenv(
    "PROJECT_ROOT"
)

if _project_root_env:

    PROJECT_ROOT = Path(
        _project_root_env
    ).expanduser().resolve()

else:

    # Safe fallback:
    # infer repository root from src/config.py
    PROJECT_ROOT = INFERRED_PROJECT_ROOT


if not PROJECT_ROOT.exists():

    raise RuntimeError(
        "PROJECT_ROOT does not exist: "
        f"{PROJECT_ROOT}"
    )


PROJECT_NAME = PROJECT_ROOT.name


# =====================================================================
# DATA PATHS
# =====================================================================

DATA_DIR = PROJECT_ROOT / "data"

RAW_DATA_DIR = DATA_DIR / "raw"
INTERIM_DATA_DIR = DATA_DIR / "interim"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
DICTIONARY_DIR = DATA_DIR / "dictionary"

ANALYSIS_DATASET_FILE = (
    PROCESSED_DATA_DIR
    / "analysis_dataset.csv"
)

# =====================================================================
# RAW DATASETS
# =====================================================================

RAW_SAM_FILE = (
    RAW_DATA_DIR / "DBs_SAMs_V9_200626.csv"
)

RAW_NBACK2_FILE = (
    RAW_DATA_DIR / "DBS_N_back_2_01072026.sav"
)

RAW_NBACK4_FILE = (
    RAW_DATA_DIR / "n_back_4.xlsx"
)

# =====================================================================
# CONFISGURATION CONSTANTS MAPS
# =====================================================================

GROUP_ID_MAP = {
    1: "A to B",
    2: "B to A",
    3: "C to D",
    4: "D to C",
}

CATEGORY_MAP = {
    1: "I",
    2: "II",
    3: "III",
    4: "IV",
}

SEQUENCE_MAP = {
    1: "A_B",
    2: "B_A",
    3: "C_D",
    4: "D_C",
}

# =====================================================================
# FIGURE PATHS
# =====================================================================

FIGURES_DIR = PROJECT_ROOT / "figures"

FIGURES_DESIGN_DIR = FIGURES_DIR / "design"
FIGURES_EXPLORATORY_DIR = FIGURES_DIR / "exploratory"
FIGURES_MANIPULATION_DIR = FIGURES_DIR / "manipulation_check"
FIGURES_NBACK_DIR = FIGURES_DIR / "nback"
FIGURES_MEDIATION_DIR = FIGURES_DIR / "mediation"
FIGURES_MODELS_DIR = FIGURES_DIR / "models"
FIGURES_FINAL_DIR = FIGURES_DIR / "final"


# =====================================================================
# REPORT PATHS
# =====================================================================

REPORTS_DIR = PROJECT_ROOT / "reports"

REPORTS_TECHNICAL_DIR = REPORTS_DIR / "technical"
TABLES_DIR = REPORTS_DIR / "tables"
TABLES_DIR_EXPLORATORY = TABLES_DIR / "exploratory"
FINAL_REPORT_DIR = REPORTS_DIR / "final_report"

TABLES_DIR_HYPOTHESIS = TABLES_DIR / "hypothesis"

# =====================================================================
# DOCUMENTATION PATHS
# =====================================================================

DOCS_DIR = PROJECT_ROOT / "docs"


# =====================================================================
# REPRODUCIBILITY
# =====================================================================

RANDOM_SEED = 42

BOOTSTRAP_SEED = RANDOM_SEED

N_BOOTSTRAP = 5000


# =====================================================================
# STATISTICAL CONFIGURATION
# =====================================================================

ALPHA = 0.05

CONFIDENCE_LEVEL = 0.95

P_VALUE_DIGITS = 3

EFFECT_SIZE_DIGITS = 3

CORRELATION_METHOD = "pearson"


# =====================================================================
# REACTION TIME CONFIGURATION
# =====================================================================

RT_UNIT = "ms"

RT_MIN_MS = 100

RT_MAX_MS = 5000

RT_USE_ONLY_CORRECT_RESPONSES = True

RT_CALIBRATION_ENABLED = True


# =====================================================================
# FIGURE CONFIGURATION
# =====================================================================

FIGURE_FORMAT = "png"

FIGURE_DPI = 300

FIGURE_SIZE = (8, 6)

FIGURE_SIZE_WIDE = (10, 6)

FIGURE_SIZE_LARGE = (12, 8)

FONT_SIZE = 11

TITLE_FONT_SIZE = 14

LABEL_FONT_SIZE = 12

LEGEND_FONT_SIZE = 10

RAW_POINT_ALPHA = 0.60

PARTICIPANT_LINE_ALPHA = 0.20

SHOW_CONFIDENCE_INTERVAL = True


# =====================================================================
# EXPERIMENTAL GROUPS
# =====================================================================

GROUP_ORDER = [
    "A",
    "B",
    "C",
    "D",
]

GROUP_EMOTION_MAP = {
    "A": "Positive",
    "B": "Negative",
    "C": "Positive",
    "D": "Negative",
}

GROUP_INTERVENTION_ORDER_MAP = {
    "A": "Autobiography_First",
    "B": "Autobiography_First",
    "C": "Emotion_Induction_First",
    "D": "Emotion_Induction_First",
}


# =====================================================================
# CROSSOVER CATEGORIES
# =====================================================================

CATEGORY_ORDER = [
    "I",
    "II",
    "III",
    "IV",
]

SEQUENCE_MAP = {
    "I": "A_B",
    "II": "B_A",
    "III": "C_D",
    "IV": "D_C",
}


# =====================================================================
# EMOTION CONDITIONS
# =====================================================================

EMOTION_ORDER = [
    "Positive",
    "Neutral",
    "Negative",
]


# =====================================================================
# SESSIONS
# =====================================================================

SESSION_ORDER = [
    1,
    2,
]

EXPECTED_SESSIONS_PER_PARTICIPANT = 2

MIN_SESSION_INTERVAL_DAYS = 2


# =====================================================================
# N-BACK
# =====================================================================

NBACK_ORDER = [
    "1-back",
    "2-back",
    "3-back",
    "4-back",
]

NBACK_TRIALS = {
    "1-back": 30,
    "2-back": 45,
    "3-back": 30,
    "4-back": 30,
}

NBACK_MOMENT_ORDER = [
    "nback1",
    "nback2",
    "nback3",
]


# =====================================================================
# SAM
# =====================================================================

SAM_MIN = 1

SAM_MAX = 9

SAM_DIMENSIONS = [
    "valence",
    "arousal",
    "dominance",
]

SAM_TIMEPOINT_ORDER = [
    "start",
    "after_nback1",
    "after_intervention1",
    "after_nback2",
    "after_rest",
    "after_intervention2",
    "after_nback3",
]

SAM_TIMEPOINT_ORDER = [
    "1",
    "2",
    "3",
    "3_1",
    "3_2",
    "4",
    "5",
    "6",
    "6_3",
    "6_4",
    "7",
]

# =====================================================================
# VSAM
# =====================================================================

VSAM_MIN = 1

VSAM_MAX = 9

VSAM_TIMEPOINT_ORDER = [
    "after_nback2",
    "after_nback3",
]


# =====================================================================
# ERQ
# =====================================================================

ERQ_MIN = 1

ERQ_MAX = 7

ERQ_REAPPRAISAL_N_ITEMS = 6

ERQ_SUPPRESSION_N_ITEMS = 4

ERQ_REAPPRAISAL_MIN_SCORE = 6

ERQ_REAPPRAISAL_MAX_SCORE = 42

ERQ_SUPPRESSION_MIN_SCORE = 4

ERQ_SUPPRESSION_MAX_SCORE = 28


# =====================================================================
# STATE / TRAIT
# =====================================================================

STATE_TRAIT_MIN = 1

STATE_TRAIT_MAX = 4

STATE_TRAIT_N_ITEMS = 6

STATE_TRAIT_N_DIRECT_ITEMS = 3

STATE_TRAIT_N_REVERSE_ITEMS = 3


# =====================================================================
# DEFAULT COVARIATES
# =====================================================================

DEMOGRAPHIC_COVARIATES = [
    "age",
    "gender",
    "education",
    "hand_dominance",
]

EMOTION_REGULATION_COVARIATES = [
    "cognitive_reappraisal",
    "expressive_suppression",
]

CROSSOVER_COVARIATES = [
    "session",
    "sequence",
]

DEFAULT_MODEL_COVARIATES = (
    DEMOGRAPHIC_COVARIATES
    + EMOTION_REGULATION_COVARIATES
    + CROSSOVER_COVARIATES
)


# =====================================================================
# MODEL CONFIGURATION
# =====================================================================

MIXED_MODEL_METHOD = "lbfgs"

DEFAULT_RANDOM_EFFECT = "1"

GEE_CORRELATION_STRUCTURE = "exchangeable"

ROBUST_STANDARD_ERRORS = True


# =====================================================================
# OUTPUT COLUMN NAMES
# =====================================================================

PARTICIPANT_COLUMN = "participant_id"

SESSION_COLUMN = "session"

GROUP_COLUMN = "group"

CATEGORY_COLUMN = "category"

SEQUENCE_COLUMN = "sequence"

EMOTION_COLUMN = "emotion"

NBACK_LEVEL_COLUMN = "nback_level"

ACCURACY_COLUMN = "accuracy"

REACTION_TIME_COLUMN = "reaction_time"

CALIBRATED_RT_COLUMN = "calibrated_rt"

SAM_VALENCE_COLUMN = "sam_valence"

SAM_AROUSAL_COLUMN = "sam_arousal"

SAM_DOMINANCE_COLUMN = "sam_dominance"