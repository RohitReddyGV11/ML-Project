# 🎓 Student Performance Prediction – End-to-End Machine Learning Project

This project is a **complete end-to-end Machine Learning application** that predicts a student’s **Math Score** based on demographic and academic attributes.  
It covers the full ML lifecycle — **data processing, model training, evaluation, serialization, and deployment** — and is deployed as an **interactive Streamlit web application**.

---

## 🚀 Live Application
🔗 **Live App:** https://student-performance-prediction-webapp.streamlit.app/

---

## 📌 Problem Statement

The objective of this project is to predict a student’s **Math Score** using the following input features:

- Gender  
- Race / Ethnicity  
- Parental Level of Education  
- Lunch Type  
- Test Preparation Course  
- Reading Score  
- Writing Score  

This prediction helps analyze how demographic and academic factors influence student performance.

---

## 🛠️ Tech Stack

- **Programming Language:** Python  
- **Machine Learning:** Scikit-learn  
- **Data Processing:** Pandas, NumPy  
- **Model Serialization:** Dill  
- **Web Framework:** Streamlit  
- **Version Control:** Git & GitHub  
- **Deployment Platform:** Streamlit Community Cloud

---

## 🧠 Machine Learning Workflow

### 1️⃣ Data Ingestion
- Raw dataset is loaded
- Data is split into training and testing sets

### 2️⃣ Data Transformation
- Categorical features are encoded
- Numerical features are scaled
- A preprocessing pipeline is created and saved as `preprocessor.pkl`

### 3️⃣ Model Training & Evaluation
- Multiple regression models are trained
- Models are evaluated using **R² Score**
- Best-performing model is selected
- Final trained model is saved as `model.pkl`

### 4️⃣ Prediction Pipeline
- Custom input handling using `CustomData` class
- Unified prediction flow using `PredictPipeline`
- Preprocessing + prediction executed seamlessly

### 5️⃣ Deployment
- Interactive frontend built using **Streamlit**
- Model inference served in real-time
- Deployed on **Streamlit Community Cloud**