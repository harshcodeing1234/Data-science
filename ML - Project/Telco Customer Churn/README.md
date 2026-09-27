# Telco Customer Churn Prediction Dashboard

A professional, interactive Streamlit web application for predicting customer churn in a telecommunications company. The application leverages a pre-trained **Random Forest Classifier** to assess the likelihood of a customer churning based on demographic details, subscribed services, and contract/billing characteristics.

## Technology Stack
- **Python 3.11+**
- **Streamlit** (interactive dashboard framework)
- **Joblib** (serializing and loading the ML model)
- **Pandas** (data processing and mapping)
- **Scikit-Learn** (machine learning prediction backend)

---

## Folder Structure
```
project/
│
├── app.py                     # Main Streamlit web application
├── models/
│   ├── random_forest_model.pkl # Pre-trained Random Forest Classifier
│   └── feature_columns.pkl    # Serialized list of feature columns
│
├── requirements.txt           # Python dependency specifications
└── README.md                  # Project documentation
```

---

## Installation & Setup

1. **Clone or navigate** to the project directory:
   ```bash
   cd "C:\Upskill\Data Science\ML - Project\Telco Customer Churn"
   ```

2. **Install the dependencies** listed in `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit application**:
   ```bash
   streamlit run app.py
   ```

---

## Application Workflows
1. **Interactive Inputs**: The app exposes user-friendly sliders, numeric input fields, and selectboxes for the 19 user input features. No manual one-hot encoding is required from the user.
2. **Data Pipeline**:
   - **Step 1**: Converts user inputs into a single-row Pandas DataFrame.
   - **Step 2**: Maps binary columns exactly like the training phase (`Male` &rarr; `1`, `Female` &rarr; `0`, `Yes` &rarr; `1`, `No` &rarr; `0`).
   - **Step 3**: Generates dummies using `pd.get_dummies()` for categorical variables (`Contract`, `PaymentMethod`, `InternetService`).
   - **Step 4**: Reindexes columns matching the training schema `feature_columns` and fills missing dummy columns with `0`.
   - **Step 5**: Predicts binary class (Churn/Stay) and probability.
3. **Actionable Recommendations**: If a customer is identified as likely to churn, the app generates custom, data-driven retention strategies to help mitigate the churn risk.

---

## Developed By
Developed by **Harsh**
