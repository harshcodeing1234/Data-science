import streamlit as st
import pandas as pd
import joblib
import os
import warnings

# Ignore minor warnings (e.g., scikit-learn version mismatch warnings)
warnings.filterwarnings('ignore')

# ----------------------------------------------------
# PAGE CONFIGURATION
# ----------------------------------------------------
st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="🔮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------------------------------------------
# MODEL & ASSET LOADING
# ----------------------------------------------------
@st.cache_resource
def load_ml_assets():
    """
    Loads the trained Random Forest model and the list of feature columns.
    Uses st.cache_resource to prevent reloading the assets on every rerun.
    """
    model_path = os.path.join("models", "random_forest_model.pkl")
    features_path = os.path.join("models", "feature_columns.pkl")
    
    # Handle missing asset files gracefully
    if not os.path.exists(model_path):
        st.error(f"❌ Model file not found at: `{model_path}`. Please ensure the model is trained and saved.")
        st.stop()
        
    if not os.path.exists(features_path):
        st.error(f"❌ Feature columns file not found at: `{features_path}`. Please check your project folder.")
        st.stop()
        
    try:
        model = joblib.load(model_path)
        feature_columns = joblib.load(features_path)
        return model, feature_columns
    except Exception as e:
        st.error(f"❌ Error loading models: {str(e)}")
        st.stop()

# Load the model and feature columns
model, feature_columns = load_ml_assets()

# ----------------------------------------------------
# CUSTOM CSS STYLING
# ----------------------------------------------------
# Injects custom CSS to style components (e.g., buttons, backgrounds, headings)
st.markdown("""
<style>
    /* Styling the main title and subheader */
    .title-container {
        text-align: center;
        padding: 1.5rem;
        background: linear-gradient(135deg, #1E3A8A, #3B82F6);
        color: white;
        border-radius: 12px;
        margin-bottom: 2rem;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .title-container h1 {
        margin: 0;
        font-size: 2.2rem;
        font-weight: 700;
    }
    .title-container p {
        margin: 0.5rem 0 0 0;
        font-size: 1.1rem;
        opacity: 0.9;
    }
    
    /* Premium cards for input groups */
    div[data-testid="column"] {
        background-color: #F8FAFC;
        padding: 1.5rem;
        border-radius: 12px;
        border: 1px solid #E2E8F0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.02);
    }
    
    /* Footer styles */
    .footer {
        position: relative;
        left: 0;
        bottom: 0;
        width: 100%;
        text-align: center;
        color: #64748B;
        font-size: 0.9rem;
        padding: 1.5rem 0;
        border-top: 1px solid #E2E8F0;
        margin-top: 4rem;
    }
</style>
""", unsafe_allow_html=True)

# ----------------------------------------------------
# SIDEBAR
# ----------------------------------------------------
with st.sidebar:
    st.markdown("## 🔮 Telco Churn Analysis")
    st.markdown(
        """
        Customer churn occurs when customers stop doing business with a company. 
        Predicting churn helps businesses identify high-risk customers and take proactive retention actions.
        """
    )
    st.divider()
    
    st.markdown("### ⚙️ Model Details")
    st.info(
        """
        - **Algorithm**: Random Forest Classifier
        - **Number of Features**: 23 Features
        - **Framework**: Scikit-Learn
        """
    )
    
    st.divider()
    st.markdown("### 📋 Steps Performed")
    st.markdown(
        """
        1. **Collect User Input** via widgets.
        2. **Map Binary Features** to `1` / `0`.
        3. **Generate Dummy variables** for categories.
        4. **Align Columns** to match training features.
        5. **Predict probability & class** using Random Forest.
        """
    )
    
    st.divider()
    st.markdown("Developed by: **Harsh**")

# ----------------------------------------------------
# MAIN CONTENT / TITLE
# ----------------------------------------------------
st.markdown("""
<div class="title-container">
    <h1>Customer Churn Prediction using Random Forest</h1>
    <p>Interactive dashboard to predict customer churn probability and analyze risk factors</p>
</div>
""", unsafe_allow_html=True)

# ----------------------------------------------------
# USER WIDGETS LAYOUT
# ----------------------------------------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 👤 Demographics & Basic")
    
    gender = st.selectbox(
        "gender", 
        ["Male", "Female"], 
        help="Select customer gender"
    )
    
    senior_citizen = st.selectbox(
        "SeniorCitizen", 
        [0, 1], 
        format_func=lambda x: "Yes (1)" if x == 1 else "No (0)",
        help="Is the customer a senior citizen?"
    )
    
    partner = st.selectbox(
        "Partner", 
        ["Yes", "No"], 
        help="Does the customer have a partner?"
    )
    
    dependents = st.selectbox(
        "Dependents", 
        ["Yes", "No"], 
        help="Does the customer have dependents?"
    )
    
    phone_service = st.selectbox(
        "PhoneService", 
        ["Yes", "No"], 
        help="Does the customer have a phone service?"
    )
    
    multiple_lines = st.selectbox(
        "MultipleLines", 
        ["Yes", "No"], 
        help="Does the customer have multiple lines?"
    )

with col2:
    st.markdown("### 🌐 Internet Services")
    
    internet_service = st.selectbox(
        "InternetService", 
        ["Fiber optic", "DSL", "No"], 
        help="Select type of internet service provider"
    )
    
    online_security = st.selectbox(
        "OnlineSecurity", 
        ["Yes", "No"], 
        help="Does the customer have online security?"
    )
    
    online_backup = st.selectbox(
        "OnlineBackup", 
        ["Yes", "No"], 
        help="Does the customer have online backup?"
    )
    
    device_protection = st.selectbox(
        "DeviceProtection", 
        ["Yes", "No"], 
        help="Does the customer have device protection?"
    )
    
    tech_support = st.selectbox(
        "TechSupport", 
        ["Yes", "No"], 
        help="Does the customer have tech support?"
    )
    
    streaming_tv = st.selectbox(
        "StreamingTV", 
        ["Yes", "No"], 
        help="Does the customer have streaming TV?"
    )

with col3:
    st.markdown("### 💳 Contract & Financials")
    
    contract = st.selectbox(
        "Contract", 
        ["Month-to-month", "One year", "Two year"], 
        help="The contract term of the customer"
    )
    
    paperless_billing = st.selectbox(
        "PaperlessBilling", 
        ["Yes", "No"], 
        help="Whether the customer has paperless billing"
    )
    
    payment_method = st.selectbox(
        "PaymentMethod", 
        [
            "Electronic check", 
            "Mailed check", 
            "Bank transfer (automatic)", 
            "Credit card (automatic)"
        ], 
        help="The customer's payment method"
    )
    
    streaming_movies = st.selectbox(
        "StreamingMovies", 
        ["Yes", "No"], 
        help="Does the customer have streaming movies?"
    )
    
    tenure = st.number_input(
        "tenure (months)", 
        min_value=0, 
        max_value=72, 
        value=12, 
        step=1,
        help="Number of months the customer has stayed with the company"
    )
    
    monthly_charges = st.number_input(
        "MonthlyCharges ($)", 
        min_value=0.0, 
        max_value=200.0, 
        value=65.0, 
        step=0.5,
        help="The amount charged to the customer monthly"
    )
    
    # Propose a smart, user-friendly default for total charges based on monthly_charges * tenure
    suggested_total = float(tenure * monthly_charges)
    total_charges = st.number_input(
        "TotalCharges ($)", 
        min_value=0.0, 
        max_value=15000.0, 
        value=suggested_total if suggested_total > 0 else 65.0, 
        step=5.0,
        help="The total amount charged to the customer (suggested based on tenure and monthly charges)"
    )

# ----------------------------------------------------
# VALIDATION AND ANALYSIS PRE-PROCESSING
# ----------------------------------------------------
# Handle user inputs validation
validation_ok = True

if total_charges < 0:
    st.error("❌ Total Charges cannot be negative.")
    validation_ok = False

if monthly_charges < 0:
    st.error("❌ Monthly Charges cannot be negative.")
    validation_ok = False

if tenure < 0:
    st.error("❌ Tenure cannot be negative.")
    validation_ok = False

# Warn user if total charges is physically impossible compared to monthly charges & tenure
if validation_ok and tenure > 0 and total_charges < monthly_charges:
    st.warning("⚠️ Warning: Total Charges are less than Monthly Charges. While allowed, this is unusual for a customer with active tenure.")

# ----------------------------------------------------
# PREDICT TRIGGER
# ----------------------------------------------------
st.write("")
predict_clicked = st.button("🔮 Predict Churn Status", use_container_width=True, type="primary")

if predict_clicked and validation_ok:
    # --- Step 1: Create a dataframe from user input ---
    input_data = {
        'gender': gender,
        'SeniorCitizen': senior_citizen,
        'Partner': partner,
        'Dependents': dependents,
        'tenure': tenure,
        'PhoneService': phone_service,
        'MultipleLines': multiple_lines,
        'OnlineSecurity': online_security,
        'OnlineBackup': online_backup,
        'DeviceProtection': device_protection,
        'TechSupport': tech_support,
        'StreamingTV': streaming_tv,
        'StreamingMovies': streaming_movies,
        'PaperlessBilling': paperless_billing,
        'MonthlyCharges': monthly_charges,
        'TotalCharges': total_charges,
        'Contract': contract,
        'PaymentMethod': payment_method,
        'InternetService': internet_service
    }
    
    input_df = pd.DataFrame([input_data])
    
    # --- Step 2: Map binary values exactly like training ---
    binary_map = {
        'Male': 1, 'Female': 0,
        'Yes': 1, 'No': 0
    }
    
    binary_cols = [
        'gender', 'Partner', 'Dependents', 'PhoneService', 'MultipleLines',
        'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport',
        'StreamingTV', 'StreamingMovies', 'PaperlessBilling'
    ]
    
    for col in binary_cols:
        input_df[col] = input_df[col].map(binary_map)
        
    # --- Step 3: Apply pd.get_dummies() only on Contract, PaymentMethod, InternetService ---
    input_df = pd.get_dummies(input_df, columns=['Contract', 'PaymentMethod', 'InternetService'], dtype=int)
    
    # --- Step 4: Reindex to match the training feature columns ---
    input_df = input_df.reindex(columns=feature_columns, fill_value=0)
    
    # --- Step 5: Predict class and probabilities ---
    try:
        prediction = model.predict(input_df)
        probability = model.predict_proba(input_df)
        
        # Get probability of Churn (class 1)
        churn_prob = probability[0][1]
        churn_prob_pct = churn_prob * 100
        
        # Display Results Header
        st.divider()
        st.markdown("## 📊 Prediction Result")
        
        res_col1, res_col2 = st.columns(2)
        
        with res_col1:
            st.markdown("### Decision")
            if prediction[0] == 1:
                st.error("⚠️ Customer is likely to Churn")
            else:
                st.success("✅ Customer is likely to Stay")
                
        with res_col2:
            st.markdown("### Churn Likelihood")
            st.write(f"**Probability of Churn:** {churn_prob_pct:.2f}%")
            st.progress(float(churn_prob))
            
        # Display actionable insights / recommendations based on feature analysis
        st.write("")
        with st.expander("💡 Customer Retention Recommendations"):
            if prediction[0] == 1:
                st.markdown("This customer is at risk of churning. Consider the following retention strategies:")
                
                recs = []
                if contract == "Month-to-month":
                    recs.append("📧 **Contract Upgrade Offer**: Offer a promotional discount if they sign up for a **1-year** or **2-year** contract. Long-term contracts significantly decrease churn risk.")
                if payment_method == "Electronic check":
                    recs.append("💳 **Automated Billing Incentive**: Provide a one-time bill credit (e.g., $5) if they enroll in **Auto-Pay** (Credit card or Bank transfer).")
                if internet_service == "Fiber optic" and (online_security == "No" or tech_support == "No"):
                    recs.append("🛡️ **Value-Added Service Bundle**: Offer a free trial of **Online Security** or **Tech Support**. Customers with more connected service add-ons are generally more loyal.")
                if tenure < 6:
                    recs.append("🤝 **Early-Stage Support**: Check in with the customer. Early-tenure month-to-month customers have the highest risk of churn.")
                if monthly_charges > 80.0:
                    recs.append("📉 **Plan Optimization**: Review their plan to see if they can be moved to a more cost-effective bundle that maintains service levels but reduces cost friction.")
                
                if not recs:
                    recs.append("📞 **Proactive Outreach**: Reach out to check on customer satisfaction and offer a small loyalty discount.")
                    
                for rec in recs:
                    st.markdown(rec)
            else:
                st.markdown("This customer is currently stable. To maintain loyalty:")
                st.markdown("✨ Send occasional appreciation emails or loyalty points.")
                if payment_method == "Electronic check":
                    st.markdown("💳 Suggest transitioning to Auto-Pay for convenience and long-term stability.")
                    
    except Exception as e:
        st.error(f"❌ Error during model prediction: {str(e)}")

# ----------------------------------------------------
# FOOTER
# ----------------------------------------------------
st.markdown("""
<div class="footer">
    <p>Customer Churn Prediction App &bull; Powered by Random Forest &bull; Developed by <strong>Harsh</strong></p>
</div>
""", unsafe_allow_html=True)
