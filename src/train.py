import joblib
import numpy as np
import pandas as pd
from pathlib import Path

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error


# ==========================================================
# Project Paths
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_PATH = PROJECT_ROOT / "data" / "jamboree.csv"

MODEL_DIR = PROJECT_ROOT / "models"
MODEL_DIR.mkdir(exist_ok=True)

MODEL_PATH = MODEL_DIR / "linear_regression.pkl"
SCALER_PATH = MODEL_DIR / "scaler.pkl"
FEATURE_PATH = MODEL_DIR / "selected_features.pkl"


# ==========================================================
# Load Dataset
# ==========================================================

def load_data():
    """Load dataset and clean column names."""

    df = pd.read_csv(DATA_PATH)

    # Remove leading/trailing spaces from column names
    df.columns = df.columns.str.strip()

    return df


# ==========================================================
# Data Preprocessing
# ==========================================================

def preprocess_data(df):
    """Prepare features and target."""

    # Drop Serial Number
    df = df.drop(columns=["Serial No."])

    X = df.drop(columns=["Chance of Admit"])
    y = df["Chance of Admit"]

    return X, y


# ==========================================================
# Train Test Split
# ==========================================================

def split_data(X, y):

    return train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42
    )


# ==========================================================
# Scaling
# ==========================================================

def scale_data(X_train, X_test):

    scaler = StandardScaler()

    X_train_scaled = pd.DataFrame(
        scaler.fit_transform(X_train),
        columns=X_train.columns,
        index=X_train.index
    )

    X_test_scaled = pd.DataFrame(
        scaler.transform(X_test),
        columns=X_test.columns,
        index=X_test.index
    )

    return X_train_scaled, X_test_scaled, scaler


# ==========================================================
# Feature Selection
# ==========================================================

def select_features(X_train_scaled, X_test_scaled):

    print("\nAvailable Columns:")
    print(X_train_scaled.columns.tolist())

    selected_features = [
        "GRE Score",
        "TOEFL Score",
        "LOR",
        "CGPA",
        "Research"
    ]

    X_train_final = X_train_scaled[selected_features]
    X_test_final = X_test_scaled[selected_features]

    return X_train_final, X_test_final, selected_features


# ==========================================================
# Model Training
# ==========================================================

def train_model(X_train, y_train):

    model = LinearRegression()

    model.fit(X_train, y_train)

    return model


# ==========================================================
# Evaluation
# ==========================================================

def evaluate_model(model, X_test, y_test):

    predictions = model.predict(X_test)

    r2 = r2_score(y_test, predictions)

    rmse = np.sqrt(mean_squared_error(y_test, predictions))

    print("\n==============================")
    print("Model Performance")
    print("==============================")
    print(f"R² Score : {r2:.4f}")
    print(f"RMSE     : {rmse:.4f}")

    return predictions


# ==========================================================
# Save Artifacts
# ==========================================================

def save_artifacts(model, scaler, feature_names):

    joblib.dump(model, MODEL_PATH)
    joblib.dump(scaler, SCALER_PATH)
    joblib.dump(feature_names, FEATURE_PATH)

    print("\nSaved Successfully")
    print(f"Model   : {MODEL_PATH}")
    print(f"Scaler  : {SCALER_PATH}")
    print(f"Features: {FEATURE_PATH}")


# ==========================================================
# Main Pipeline
# ==========================================================

def main():

    print("Loading dataset...")

    df = load_data()

    print(f"Dataset Shape : {df.shape}")

    X, y = preprocess_data(df)

    X_train, X_test, y_train, y_test = split_data(X, y)

    X_train_scaled, X_test_scaled, scaler = scale_data(
        X_train,
        X_test
    )

    X_train_final, X_test_final, feature_names = select_features(
        X_train_scaled,
        X_test_scaled
    )

    model = train_model(
        X_train_final,
        y_train
    )

    evaluate_model(
        model,
        X_test_final,
        y_test
    )

    save_artifacts(
        model,
        scaler,
        feature_names
    )


if __name__ == "__main__":
    main()