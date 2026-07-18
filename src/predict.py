import pandas as pd

from src.model_loader import load_artifacts


# ==========================================================
# Load Saved Artifacts
# ==========================================================

model, scaler, selected_features = load_artifacts()


# ==========================================================
# Prediction Function
# ==========================================================

def predict_admission(
    gre_score,
    toefl_score,
    university_rating,
    sop,
    lor,
    cgpa,
    research
):
    """
    Predict admission probability.
    """

    # Create input dataframe
    input_df = pd.DataFrame({
        "GRE Score": [gre_score],
        "TOEFL Score": [toefl_score],
        "University Rating": [university_rating],
        "SOP": [sop],
        "LOR": [lor],
        "CGPA": [cgpa],
        "Research": [research]
    })

    # Scale data
    scaled = scaler.transform(input_df)

    scaled_df = pd.DataFrame(
        scaled,
        columns=input_df.columns
    )

    # Select required features
    scaled_df = scaled_df[selected_features]

    # Predict
    prediction = model.predict(scaled_df)

    return prediction[0]


# ==========================================================
# Testing
# ==========================================================

if __name__ == "__main__":

    result = predict_admission(
        gre_score=330,
        toefl_score=115,
        university_rating=5,
        sop=4.5,
        lor=4.5,
        cgpa=9.2,
        research=1
    )

    print(f"Predicted Chance of Admission: {result:.2f}")