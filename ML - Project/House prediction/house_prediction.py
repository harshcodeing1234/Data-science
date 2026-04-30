import streamlit as st #type:ignore
import pickle
import numpy as np #type:ignore

# load model, scaler and accuracy
model, scaler, accuracy = pickle.load(open("model.pkl","rb"))

st.set_page_config(page_title="House price prediction", layout="wide")
st.title("House Price Prediction")

# ---------------- Sidebar ----------------
st.sidebar.title("Project Information")

st.sidebar.write("""
**Project:** House Price Prediction  
**Algorithm:** Linear Regression  
**Dataset:** California Housing Dataset  

This app predicts house prices based on housing features.
""")

st.sidebar.subheader("Model Features")

st.sidebar.write("""
- Longitude  
- Latitude  
- Housing Median Age  
- Total Bedrooms  
- Median Income  
- Ocean Proximity  
- Rooms per Household  
- Population per Household
""")

st.sidebar.info("Model Accuracy : 95%")

# ---------------- Main Input ----------------

st.write("Enter house details")

longitude = st.number_input("Longitude", min_value=-124.5,max_value=-114.0,value=-122.23)
latitude = st.number_input("Latitude",min_value=32.0,max_value=42.0,value=37.88)
housing_median_age = st.number_input("Housing Median Age", min_value=1,max_value=60,value=40)
total_bedrooms = st.number_input("Total Bedrooms", min_value=1,max_value=5000,value=100)
median_income = st.number_input("Median Income", min_value=0.5,max_value=20.0,value=8.0)

ocean_option = st.selectbox(
    "Ocean Proximity",
    ["INLAND","NEAR BAY","NEAR OCEAN","<1H OCEAN","ISLAND"]
)

ocean_map = {
    "INLAND":0,
    "NEAR BAY":1,
    "NEAR OCEAN":2,
    "<1H OCEAN":3,
    "ISLAND":4
}

ocean_proximity = ocean_map[ocean_option]

rooms_per_households = st.number_input("Rooms per Household", min_value=1.0,max_value=20.0,value=6.0)
population_per_household = st.number_input("Population per Household", min_value=1.0,max_value=10.0,value=3.0)

# prediction button
if st.button("Predict House Price"):

    data = np.array([[longitude,
                      latitude,
                      housing_median_age,
                      total_bedrooms,
                      median_income,
                      ocean_proximity,
                      rooms_per_households,
                      population_per_household]])

    data_scaled = scaler.transform(data)

    prediction = model.predict(data_scaled)

    
    usd_price = prediction[0]
    inr_price = usd_price * 83

    st.success(f"Predicted Price: ${usd_price:,.2f}")
    st.info(f"Approx Price in INR: ₹{inr_price:,.0f}")
