import streamlit as st #type:ignore
import joblib #type:ignore
import numpy as np #type:ignore

data = joblib.load("models/loan_model.pkl")
model = data["model"]
scaler = data["scaler"]

st.set_page_config(page_title="Loan Approval Prediction", layout="wide")
st.title("Loan Approval Prediction")

st.sidebar.title("Project Information")
st.sidebar.write("""
**Project:** Loan Approval Prediction 
**Algorithm:** K-Nearest Neighbours  
**Dataset:** data/loan_prediction.csv  
""")

st.write("Enter loan details")

col1, col2 = st.columns(2)

with col1:
    gender = 1 if st.selectbox("Gender", ["Male", "Female"]) == "Male" else 0
    dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
    self_employed = 1 if st.selectbox("Self Employed", ["Yes", "No"]) == "Yes" else 0
    coapplicant_income = st.number_input("Coapplicant Income", min_value=0.0, value=0.0)
    loan_amount_term = st.number_input("Loan Amount Term (days)", min_value=0.0, value=360.0)
    property_area = 1 if st.selectbox("Property Area", ["Urban", "Rural"]) == "Urban" else 0

with col2:
    married = 1 if st.selectbox("Married", ["Yes", "No"]) == "Yes" else 0
    education = 1 if st.selectbox("Education", ["Not Graduate", "Graduate"]) == "Graduate" else 0
    applicant_income = st.number_input("Applicant Income", min_value=0, value=5000)
    loan_amount = st.number_input("Loan Amount", min_value=0.0, value=100.0)
    credit_history = st.selectbox("Credit History", [1.0, 0.0])

if st.button("Predict Loan Approval"):
    data = np.array([[gender, married, dependents, education, self_employed, 
                      applicant_income, coapplicant_income, loan_amount, 
                      loan_amount_term, credit_history, property_area]])
    
    data_scaled = scaler.transform(data)
    prediction = model.predict(data_scaled)
    status = "Approved" if prediction[0] == 1 else "Not Approved" 
    st.success(f"Prediction: {status}")

