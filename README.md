# Diabetes_msc_mvp
A Django-based Decision Tree clinical decision support system for diabetes risk prediction in Nigerian Primary Healthcare Centres.
# Decision Tree-Based Diabetes Risk Prediction System

## Overview

This project is a Django-based machine learning clinical decision support system developed for early diabetes risk prediction in Nigerian Primary Healthcare Centres (PHCs).

The application uses a Decision Tree (CART) machine learning algorithm to classify patients into different diabetes risk levels and generate healthcare recommendations.

The system is designed as an MSc project MVP focused on:
- early diabetes detection,
- explainable AI,
- lightweight deployment,
- and low-resource healthcare environments.

---

# Features

## Patient Screening
Healthcare workers can input patient health information including:
- Age
- Gender
- BMI
- Blood Pressure
- Glucose Level
- Family History

---

## Diabetes Risk Prediction
The system predicts patient risk levels using a trained Decision Tree model.

Risk Classes:
- LOW
- MEDIUM
- HIGH

---

## Recommendation Engine

The system automatically generates recommendations based on prediction results.

Examples:
- Lifestyle advice
- Repeat testing
- Referral to secondary healthcare

---

## Screening History

Stores all patient screening records for future reference and monitoring.

---

## Metrics Dashboard

Displays machine learning evaluation metrics including:
- Accuracy
- Precision
- Recall
- Specificity
- ROC/AUC

---

# Technologies Used

- Django
- SQLite
- Scikit-learn
- NumPy
- Pandas
- Joblib

---

# Machine Learning Model

The system uses:

## CART Decision Tree Classifier

The model predicts diabetes risk based on:
- Age
- BMI
- Blood Pressure
- Glucose Level
- Family History
- Gender

---

# Mathematical Formulation

## Feature Vector

\[
X = [x_1, x_2, x_3, x_4, x_5, x_6]
\]

Where:
- \(x_1\) = Gender
- \(x_2\) = Age
- \(x_3\) = BMI
- \(x_4\) = Blood Pressure
- \(x_5\) = Glucose Level
- \(x_6\) = Family History

---

## Classification Function

\[
f(X) \rightarrow Y
\]

Where:
- \(X\) = Patient feature vector
- \(Y\) = Predicted diabetes risk

---

## Gini Index

\[
Gini(D) = 1 - \sum_{i=1}^{c} p_i^2
\]

---

## Accuracy Formula

\[
Accuracy = \frac{TP + TN}{TP + TN + FP + FN}
\]

---

# System Architecture

```text
Healthcare Worker
        ↓
Patient Data Input
        ↓
Data Preprocessing
        ↓
Decision Tree Model
        ↓
Risk Prediction
        ↓
Recommendation Engine
        ↓
Result Display
```

---

# Project Structure

```text
config/
screening/
templates/
static/
train_model.py
manage.py
requirements.txt
README.md
```

---

# Installation

## Clone Repository

```bash
git clone <repo_url>
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

---

## Activate Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux/Mac

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Run Migrations

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

---

# Train The Model

```bash
python train_model.py
```

---

# Run Server

```bash
python manage.py runserver
```

---

# Admin Panel

Create superuser:

```bash
python manage.py createsuperuser
```

Admin URL:

```text
http://127.0.0.1:8000/admin
```

---

# Objectives

This project aims to:
- Support early diabetes diagnosis
- Improve PHC screening efficiency
- Demonstrate explainable machine learning
- Reduce late-stage diabetes detection
- Provide low-cost clinical decision support

---

# Future Improvements

- Real healthcare dataset integration
- Mobile application support
- Offline-first architecture
- PDF medical report generation
- Advanced analytics dashboard
- Multi-user authentication
- SMS notifications
- Real-time model retraining

---

# Academic Relevance

This project demonstrates:
- Clinical Decision Support Systems
- Machine Learning in Healthcare
- Explainable AI
- Decision Tree Classification
- Diabetes Risk Prediction
- Healthcare Informatics

---

# License

This project is for academic and research purposes.
