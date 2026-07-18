## 🌐 Live Demo

👉 https://jamboree-admission-predictor-qsnq9pespymc26bkrkrweu.streamlit.app/

# 🎓 Graduate Admission Predictor

A Machine Learning web application that predicts the probability of admission to graduate programs based on a student's academic profile.

Built using **Python**, **Scikit-learn**, and **Streamlit**, this project demonstrates an end-to-end machine learning workflow—from data preprocessing and model training to deployment as an interactive web application.

---

## 📸 Application Preview

### Home Page

![Home Page](images/home.png)

### Prediction Result

![Prediction Result](images/prediction.png)

---

## 📌 Project Overview

Graduate school admissions depend on several academic factors such as GRE score, TOEFL score, CGPA, research experience, and recommendation strength.

This project uses a **Linear Regression** model trained on historical admission data to estimate a student's probability of admission.

The project follows a complete machine learning lifecycle:

- Data preprocessing
- Feature selection
- Model training
- Model evaluation
- Model serialization using Joblib
- Interactive prediction interface with Streamlit

---

## 🛠️ Tech Stack

| Category | Technologies |
|----------|--------------|
| Language | Python |
| Machine Learning | Scikit-learn |
| Data Processing | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Model Serialization | Joblib |
| Web App | Streamlit |
| Version Control | Git & GitHub |

---

## 📂 Project Structure

```text
Jamboree-Admission-Predictor/
│
├── app.py                     # Streamlit application
├── data/
│   └── jamboree.csv
├── images/
│   ├── home.png
│   └── prediction.png
├── models/
│   ├── linear_regression.pkl
│   ├── scaler.pkl
│   └── selected_features.pkl
├── notebooks/
│   └── Jamboree_EDA.ipynb
├── src/
│   ├── train.py
│   ├── predict.py
│   └── model_loader.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🧠 Machine Learning Workflow

1. Data Cleaning
2. Feature Selection
3. Train-Test Split
4. Feature Scaling using StandardScaler
5. Linear Regression Model Training
6. Model Evaluation
7. Model Serialization using Joblib
8. Streamlit Deployment

---

## 📊 Model Performance

| Metric | Value |
|---------|--------|
| Model | Linear Regression |
| R² Score | **0.8155** |
| RMSE | **0.0614** |

### Selected Features

- GRE Score
- TOEFL Score
- LOR
- CGPA
- Research

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/soumildiwan/Jamboree-Admission-Predictor.git
```

Navigate to the project

```bash
cd Jamboree-Admission-Predictor
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

## 🚀 Future Improvements

- Compare multiple regression models
- Hyperparameter tuning
- Deploy using Streamlit Community Cloud
- Add explainability using SHAP
- Improve UI/UX