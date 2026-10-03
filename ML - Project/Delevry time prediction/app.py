import streamlit as st
import pandas as pd
import numpy as np
import joblib
from pathlib import Path

# Set Streamlit page configuration
st.set_page_config(
    page_title="Food Delivery Time Prediction",
    page_icon="⏱️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.2rem;
        font-weight: 700;
        color: #FF4B4B;
        margin-bottom: 0.2rem;
    }
    .sub-header {
        font-size: 1.05rem;
        color: #555555;
        margin-bottom: 1.5rem;
    }
    .metric-card {
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        border: 1px solid #dee2e6;
        border-radius: 12px;
        padding: 20px;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    .metric-value {
        font-size: 2.8rem;
        font-weight: 800;
        color: #FF4B4B;
    }
    .metric-label {
        font-size: 1.1rem;
        color: #495057;
        font-weight: 600;
    }
    .status-badge {
        display: inline-block;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

# Base directory for artifacts
BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "models" / "linear_regression_model.pkl"
SCALER_PATH = BASE_DIR / "models" / "scaler.pkl"
FEATURES_PATH = BASE_DIR / "models" / "feature_columns.pkl"


@st.cache_resource
def load_artifacts():
    """Load model, scaler, and feature columns with caching."""
    try:
        model = joblib.load(MODEL_PATH)
        scaler = joblib.load(SCALER_PATH)
        feature_columns = joblib.load(FEATURES_PATH)
        return model, scaler, feature_columns
    except Exception as e:
        st.error(f"Error loading model artifacts: {e}")
        return None, None, None


def predict_delivery_time(model, scaler, feature_columns, input_dict):
    """Preprocess user input and generate prediction."""
    df_input = pd.DataFrame([input_dict])
    
    # One-hot encode categorical features
    df_encoded = pd.get_dummies(
        df_input,
        columns=["Weather", "Traffic_Level", "Time_of_Day", "Vehicle_Type"],
        dtype=int
    )
    
    # Align columns to match training feature set exactly
    df_aligned = df_encoded.reindex(columns=feature_columns, fill_value=0)
    
    # Standardize input features using the trained scaler
    df_scaled = scaler.transform(df_aligned)
    
    # Generate prediction
    pred = model.predict(df_scaled)[0]
    return max(0.0, float(pred))


# Load artifacts
model, scaler, feature_columns = load_artifacts()

# Sidebar Configuration
with st.sidebar:
    st.markdown("## 🛵 Delivery Predictor")
    st.caption("AI-powered delivery duration estimator")
    
    st.divider()
    
    st.subheader("💡 Quick Presets")
    preset = st.selectbox(
        "Choose a sample scenario:",
        ["Custom Input", "⚡ Fast Sunny Scooter", "🌧️ Rainy Peak Rush Hour", "🌙 Night Long Distance Car", "❄️ Snowy Heavy Traffic"]
    )

    st.divider()
    st.markdown("### 📊 Model Info")
    st.markdown("""
    - **Algorithm:** Linear Regression
    - **Scaling:** StandardScaler
    - **Encoding:** One-Hot Encoding
    - **Trained Features:** 18
    """)
    
    st.info("Ensure all input variables are accurate for the best estimate.")

# Set preset defaults
default_distance = 8.5
default_prep = 15
default_exp = 3.0
default_weather = "Clear"
default_traffic = "Medium"
default_time = "Evening"
default_vehicle = "Bike"

if preset == "⚡ Fast Sunny Scooter":
    default_distance = 3.5
    default_prep = 10
    default_exp = 5.0
    default_weather = "Clear"
    default_traffic = "Low"
    default_time = "Afternoon"
    default_vehicle = "Scooter"
elif preset == "🌧️ Rainy Peak Rush Hour":
    default_distance = 12.0
    default_prep = 25
    default_exp = 1.5
    default_weather = "Rainy"
    default_traffic = "High"
    default_time = "Evening"
    default_vehicle = "Bike"
elif preset == "🌙 Night Long Distance Car":
    default_distance = 18.0
    default_prep = 20
    default_exp = 6.0
    default_weather = "Clear"
    default_traffic = "Low"
    default_time = "Night"
    default_vehicle = "Car"
elif preset == "❄️ Snowy Heavy Traffic":
    default_distance = 15.0
    default_prep = 30
    default_exp = 2.0
    default_weather = "Snowy"
    default_traffic = "High"
    default_time = "Evening"
    default_vehicle = "Car"

# Main Layout
st.markdown('<div class="main-header">🛵 Food Delivery Time Predictor</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="sub-header">Accurately forecast food delivery times based on route distance, preparation time, courier experience, and environmental conditions.</div>',
    unsafe_allow_html=True
)

if model is None or scaler is None or feature_columns is None:
    st.error("⚠️ Model artifacts could not be loaded. Please ensure model files are present in the `models/` directory.")
    st.stop()

# Input Form
with st.container():
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("📍 Order & Route")
        distance_km = st.number_input(
            "Delivery Distance (km)",
            min_value=0.1,
            max_value=50.0,
            value=float(default_distance),
            step=0.1,
            help="Total travel distance from restaurant to customer destination."
        )
        
        prep_time_min = st.number_input(
            "Preparation Time (mins)",
            min_value=1,
            max_value=120,
            value=int(default_prep),
            step=1,
            help="Time taken by the kitchen to prepare and pack the order."
        )
        
    with col2:
        st.subheader("🌦️ Environment & Conditions")
        weather = st.selectbox(
            "Weather Condition",
            options=["Clear", "Foggy", "Rainy", "Snowy", "Windy"],
            index=["Clear", "Foggy", "Rainy", "Snowy", "Windy"].index(default_weather)
        )
        
        traffic_level = st.selectbox(
            "Traffic Level",
            options=["Low", "Medium", "High"],
            index=["Low", "Medium", "High"].index(default_traffic)
        )
        
        time_of_day = st.selectbox(
            "Time of Day",
            options=["Morning", "Afternoon", "Evening", "Night"],
            index=["Morning", "Afternoon", "Evening", "Night"].index(default_time)
        )

    with col3:
        st.subheader("🚴 Courier & Vehicle")
        vehicle_type = st.selectbox(
            "Vehicle Type",
            options=["Bike", "Scooter", "Car"],
            index=["Bike", "Scooter", "Car"].index(default_vehicle)
        )
        
        courier_exp = st.slider(
            "Courier Experience (years)",
            min_value=0.0,
            max_value=15.0,
            value=float(default_exp),
            step=0.5,
            help="Courier experience level in food delivery."
        )

# Prepare dictionary of inputs
input_data = {
    "Distance_km": distance_km,
    "Weather": weather,
    "Traffic_Level": traffic_level,
    "Time_of_Day": time_of_day,
    "Vehicle_Type": vehicle_type,
    "Preparation_Time_min": prep_time_min,
    "Courier_Experience_yrs": courier_exp
}

st.markdown("---")

# Prediction Action
col_btn, col_empty = st.columns([1, 4])
with col_btn:
    predict_btn = st.button("🚀 Predict Delivery Time", use_container_width=True, type="primary")

# Execute prediction if button is clicked or user interacts
if predict_btn or preset != "Custom Input":
    predicted_time = predict_delivery_time(model, scaler, feature_columns, input_data)
    
    hours = int(predicted_time // 60)
    mins = int(predicted_time % 60)
    
    st.markdown("### 🎯 Prediction Results")
    
    res_col1, res_col2, res_col3 = st.columns([1.5, 1, 1])
    
    with res_col1:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Estimated Delivery Time</div>
            <div class="metric-value">{predicted_time:.1f} <span style="font-size: 1.5rem;">min</span></div>
            <div style="color: #6c757d; font-size: 0.95rem; margin-top: 5px;">
                ⏱️ Equivalent to: <b>{f"{hours} hr " if hours > 0 else ""}{mins} mins</b>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
    with res_col2:
        # Estimated speed / pacing metric
        transit_time_est = max(1.0, predicted_time - prep_time_min)
        avg_speed_est = (distance_km / (transit_time_est / 60)) if transit_time_est > 0 else 0
        st.metric(
            label="Estimated Transit Speed",
            value=f"{avg_speed_est:.1f} km/h",
            help="Calculated estimated average speed on road excluding prep time."
        )
        st.metric(
            label="Kitchen Prep Ratio",
            value=f"{(prep_time_min / predicted_time * 100):.0f}% of total",
            help="Percentage of overall delivery duration dedicated to meal preparation."
        )
        
    with res_col3:
        # Delivery Window range
        min_window = max(5, int(predicted_time - 5))
        max_window = int(predicted_time + 5)
        st.metric(
            label="Estimated Delivery Window",
            value=f"{min_window} - {max_window} min",
            help="Expected delivery arrival interval (+/- 5 minutes)."
        )
        
        # Delivery status badge
        if predicted_time < 35:
            st.success("🟢 Fast Delivery Expected")
        elif predicted_time < 65:
            st.info("🟡 Standard Delivery Time")
        else:
            st.warning("🔴 Extended Delivery Window")

    st.markdown("---")
    
    # Input summary review
    with st.expander("📋 Review Provided Input Data"):
        summary_df = pd.DataFrame([
            {"Feature": k.replace("_", " "), "Value": str(v)}
            for k, v in input_data.items()
        ])
        st.dataframe(summary_df, use_container_width=True, hide_index=True)

# Footer
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown(
    """
    <div style="text-align: center; color: #888888; font-size: 0.85rem;">
        Developed with Streamlit & Scikit-Learn | Food Delivery Time Prediction Project
    </div>
    """,
    unsafe_allow_html=True
)
