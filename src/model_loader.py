import joblib
from pathlib import Path


# ==========================================================
# Project Paths
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

MODEL_PATH = PROJECT_ROOT / "models" / "linear_regression.pkl"
SCALER_PATH = PROJECT_ROOT / "models" / "scaler.pkl"
FEATURE_PATH = PROJECT_ROOT / "models" / "selected_features.pkl"


# ==========================================================
# Load Saved Artifacts
# ==========================================================

def load_artifacts():
    """
    Load the trained model, scaler and selected features.
    """

    model = joblib.load(MODEL_PATH)

    scaler = joblib.load(SCALER_PATH)

    selected_features = joblib.load(FEATURE_PATH)

    return model, scaler, selected_features