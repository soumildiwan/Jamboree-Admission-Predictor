import streamlit as st

from src.predict import predict_admission

st.set_page_config(
    page_title="Graduate Admission Predictor",
    page_icon="🎓",
    layout="wide"
)
# ==========================================================
# Sidebar
# ==========================================================

st.sidebar.title("📊 Model Information")

st.sidebar.markdown("---")

st.sidebar.subheader("Algorithm")
st.sidebar.write("Linear Regression")

st.sidebar.subheader("Performance")
st.sidebar.metric("R² Score", "0.8155")
st.sidebar.metric("RMSE", "0.0614")

st.sidebar.markdown("---")

st.sidebar.subheader("Selected Features")

features = [
    "GRE Score",
    "TOEFL Score",
    "LOR",
    "CGPA",
    "Research"
]

for feature in features:
    st.sidebar.write(f"✅ {feature}")

st.sidebar.markdown("---")

st.sidebar.subheader("Dataset")

st.sidebar.write("Graduate Admission Dataset")

st.sidebar.write("Records: **500**")

st.sidebar.write("Target: **Chance of Admit**")

st.sidebar.markdown("---")

st.sidebar.info(
    """
This application predicts graduate admission probability using a trained Linear Regression model.
"""
)
# ==========================================================
# User Inputs
# ==========================================================

# ==========================================================
# Page Header
# ==========================================================

st.title("🎓 Graduate Admission Predictor")

st.markdown(
    """
Estimate the probability of admission to a graduate program using a
Machine Learning model trained on historical admission data.
"""
)

st.divider()

col1, col2 = st.columns(2)

with col1:
    gre_score = st.number_input(
        "GRE Score",
        min_value=260,
        max_value=340,
        value=320
    )

    toefl_score = st.number_input(
        "TOEFL Score",
        min_value=0,
        max_value=120,
        value=110
    )

    university_rating = st.selectbox(
        "University Rating",
        [1, 2, 3, 4, 5]
    )

with col2:
    sop = st.slider(
        "Statement of Purpose (SOP)",
        min_value=1.0,
        max_value=5.0,
        value=4.0,
        step=0.5
    )

    lor = st.slider(
        "Letter of Recommendation (LOR)",
        min_value=1.0,
        max_value=5.0,
        value=4.0,
        step=0.5
    )

    cgpa = st.number_input(
        "CGPA",
        min_value=0.0,
        max_value=10.0,
        value=8.5,
        step=0.01
    )

research = st.checkbox(
    "Research Experience",
    value=True
)

# ==========================================================
# Predict Button
# ==========================================================

if st.button("Predict Admission", use_container_width=True):

    prediction = predict_admission(
        gre_score=gre_score,
        toefl_score=toefl_score,
        university_rating=university_rating,
        sop=sop,
        lor=lor,
        cgpa=cgpa,
        research=int(research)
    )

    # -------------------------
    # Result Section
    # -------------------------

    st.divider()

    st.subheader("🎯 Admission Prediction")

    st.metric(
        label="Chance of Admission",
        value=f"{prediction:.2%}"
    )

    st.progress(float(prediction))

    if prediction >= 0.80:
        st.success("Excellent chance of admission 🎉")

    elif prediction >= 0.60:
        st.info("Good chance of admission 👍")

    elif prediction >= 0.40:
        st.warning("Moderate chance of admission")

    else:
        st.error("Low chance of admission")