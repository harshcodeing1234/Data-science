import streamlit as st #type:ignore
import joblib #type:ignore
import numpy as np #type:ignore

# load model, scaler and threshold
data = joblib.load("model.pkl")
model = data['model']
scaler = data['scaler']


st.set_page_config(page_title="Social network ads Prediction", layout="wide")
st.title("Ads Prediction")

# ---------------- Sidebar ----------------
st.sidebar.title("Project Information")

st.sidebar.write("""
**Project:** Ads Prediction 
**Algorithm:** Support vector machine  
**Dataset:** Social_Network_Ads.csv  

This app predicts product purchased chance based on Advertisment features.
""")

st.sidebar.subheader("Model Features")

st.sidebar.write("""
- Gender
- Age
- EstimatedSalary
- Purchased(Target)
""")

st.sidebar.info("Model Accuracy : 93%")

# ---------------- Main Input ----------------

st.write("Enter student details")

gender_option = st.selectbox("Gender", ["Male", "Female"])
gender = 1 if gender_option == "Male" else 0

Age = st.number_input("Age", min_value=1, max_value=100, value=18)

Estimate_Salary = st.number_input("EstimatedSalary", min_value=0.0)

# prediction button
if st.button("Predict Purchased"):

    data = np.array([[gender, Age, Estimate_Salary]])

    new_data_scaled = scaler.transform(data)

    prediction = model.predict(new_data_scaled)
    
    status = "Customer will PURCHASE" if prediction[0] == 1 else "Customer will NOT PURCHASE"
    
    st.success(f"Prediction: {status}")
