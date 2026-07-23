# 🎓 Graduate Admission Prediction System

An end-to-end Machine Learning application that predicts the probability of admission to graduate programs based on a student's academic profile.

The project demonstrates the complete ML lifecycle—from data preprocessing and model development to cloud deployment using Docker and AWS.

---

# 🌐 Live Demo

### 🚀 Streamlit Web Application

👉 https://jamboree-admission-predictor-qsnq9pespymc26bkrkrweu.streamlit.app/

---

# ☁️ REST API Deployment

The trained model is also exposed as a **Flask REST API**.

The API is:

- Containerized using Docker
- Stored in Amazon Elastic Container Registry (ECR)
- Deployed on Amazon Elastic Container Service (ECS)

> **Note**
>
> The ECS deployment uses a temporary public IP for demonstration purposes.
> The endpoint may not remain active after the cloud resources are stopped.

### API Endpoints

#### Home Endpoint

```
GET /
```

Example Response

```json
{
    "message":"Welcome to the Graduate Admission Prediction API!",
    "status":"API is running successfully."
}
```

---

#### Prediction Endpoint

```
POST /predict
```

Example Request

```json
{
    "gre":320,
    "toefl":110,
    "university_rating":4,
    "sop":4,
    "lor":4.5,
    "cgpa":9.1,
    "research":1
}
```

Example Response

```json
{
    "chance_of_admit":0.8303
}
```

---

# 📸 Application Preview

## Home Page

![Home Page](images/home.png)

---

## Prediction Result

![Prediction Result](images/prediction.png)

---

# 🏗️ System Architecture

```
                User
                  │
                  ▼
        Streamlit Web Application
                  │
                  ▼
          Flask REST API
                  │
                  ▼
     Linear Regression Model (.pkl)
                  ▲
                  │
        Docker Container (Flask)
                  │
                  ▼
        Amazon ECS (Fargate)
                  ▲
                  │
      Docker Image (Amazon ECR)
```

---

# 📌 Project Overview

Graduate school admissions depend on multiple academic factors such as:

- GRE Score
- TOEFL Score
- CGPA
- SOP
- LOR
- University Rating
- Research Experience

This project predicts a student's admission probability using a **Linear Regression** model trained on historical admission data.

The application demonstrates an end-to-end production-ready ML workflow:

- Data preprocessing
- Exploratory Data Analysis
- Feature Selection
- Model Training
- Model Evaluation
- Model Serialization
- REST API Development
- Streamlit Web Application
- Docker Containerization
- AWS Cloud Deployment

---

# 🛠️ Tech Stack

| Category | Technologies |
|-----------|--------------|
| Language | Python |
| Machine Learning | Scikit-learn |
| Data Processing | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Web Framework | Streamlit, Flask |
| Model Serialization | Joblib |
| Containerization | Docker |
| Cloud | Amazon ECS, Amazon ECR |
| Version Control | Git & GitHub |

---

# 📂 Project Structure

```text
Jamboree-Admission-Predictor/
│
├── app.py
├── api.py
├── Dockerfile
├── requirements.txt
├── requirements_api.txt
│
├── data/
│   └── jamboree.csv
│
├── images/
│   ├── home.png
│   └── prediction.png
│
├── models/
│   ├── linear_regression.pkl
│   ├── scaler.pkl
│   └── selected_features.pkl
│
├── notebooks/
│   └── Jamboree_EDA.ipynb
│
├── src/
│   ├── train.py
│   ├── predict.py
│   └── model_loader.py
│
└── README.md
```

---

# 🧠 Machine Learning Workflow

- Data Cleaning
- Exploratory Data Analysis
- Feature Selection
- Train-Test Split
- Feature Scaling
- Linear Regression
- Ridge Regression
- Lasso Regression
- Model Evaluation
- Model Serialization
- Streamlit Deployment
- Flask REST API
- Docker Deployment
- AWS ECS Deployment

---

# 📊 Model Performance

| Metric | Value |
|---------|---------|
| Best Model | Linear Regression |
| R² Score | **0.8155** |
| RMSE | **0.0614** |

## Selected Features

- GRE Score
- TOEFL Score
- LOR
- CGPA
- Research

---

# ⚙️ Local Installation

Clone the repository

```bash
git clone https://github.com/soumildiwan/Jamboree-Admission-Predictor.git
```

Move into the project

```bash
cd Jamboree-Admission-Predictor
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Streamlit application

```bash
streamlit run app.py
```

Run the Flask API

```bash
python api.py
```

---

# 🐳 Docker

Build Docker Image

```bash
docker build -t jamboree-api .
```

Run Container

```bash
docker run -p 5000:5000 jamboree-api
```

---

# 🚀 Future Improvements

- Deploy with a custom domain and HTTPS
- Add CI/CD using GitHub Actions
- Integrate SHAP for model explainability
- Add authentication for API endpoints
- Compare additional regression algorithms
- Improve UI/UX

---

# 👨‍💻 Author

**Soumil Diwan**

If you found this project useful, feel free to ⭐ the repository.
