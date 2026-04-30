# Loan Approval Prediction

A machine learning project that predicts loan approval status using K-Nearest Neighbors (KNN) algorithm.

## Overview

This project analyzes loan application data and predicts whether a loan will be approved or rejected based on applicant information such as income, credit history, education, and other factors.

## Project Structure

```
loan prediction/
├── app.py                  # Streamlit web application
├── knn_project.ipynb       # Jupyter notebook with model training
├── README.md               # Project documentation
├── data/                   # Dataset files
│   ├── loan_prediction.csv
│   └── cleaned_load_approval.csv
├── models/                 # Trained models
│   └── loan_model.pkl
└── src/                    # Source code
    └── data.py
```

## Features

- **Data Preprocessing**: Handles missing values, encodes categorical variables
- **KNN Model**: Trained K-Nearest Neighbors classifier
- **Feature Scaling**: StandardScaler for normalized predictions
- **Web Interface**: Interactive Streamlit app for real-time predictions

## Installation

1. Clone the repository
2. Install required packages:
```bash
pip install streamlit joblib numpy pandas scikit-learn
```

## Usage

### Run the Streamlit App
```bash
streamlit run app.py
```

### Run the Jupyter Notebook
```bash
jupyter notebook knn_project.ipynb
```

## Input Features

- **Gender**: Male/Female
- **Married**: Yes/No
- **Dependents**: 0, 1, 2, 3+
- **Education**: Graduate/Not Graduate
- **Self Employed**: Yes/No
- **Applicant Income**: Monthly income
- **Coapplicant Income**: Co-applicant's monthly income
- **Loan Amount**: Requested loan amount
- **Loan Amount Term**: Loan duration in days
- **Credit History**: 1.0 (good) / 0.0 (bad)
- **Property Area**: Urban/Rural

## Model

- **Algorithm**: K-Nearest Neighbors (KNN)
- **Preprocessing**: StandardScaler
- **Output**: Binary classification (Approved/Not Approved)

## Dataset

Source: Loan Prediction Problem Dataset
