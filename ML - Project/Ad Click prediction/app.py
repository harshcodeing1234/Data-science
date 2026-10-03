import os
import joblib
import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Set page configuration
st.set_page_config(
    page_title="Ad Click Predictor AI",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for polished styling
st.markdown("""
    <style>
    .main-header {
        font-size: 2.2rem;
        font-weight: 700;
        color: #1E3A8A;
        margin-bottom: 0.2rem;
    }
    .sub-header {
        font-size: 1.05rem;
        color: #4B5563;
        margin-bottom: 1.5rem;
    }
    .metric-card {
        background: linear-gradient(135deg, #F0F4FF 0%, #E0E7FF 100%);
        border-radius: 10px;
        padding: 16px;
        border: 1px solid #C7D2FE;
        box-shadow: 0 2px 4px rgba(0,0,0,0.04);
    }
    .result-card-click {
        background-color: #ECFDF5;
        border-left: 6px solid #10B981;
        padding: 20px;
        border-radius: 8px;
        margin-top: 15px;
    }
    .result-card-noclick {
        background-color: #FEF2F2;
        border-left: 6px solid #EF4444;
        padding: 20px;
        border-radius: 8px;
        margin-top: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# Resolve Base Directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR = os.path.join(BASE_DIR, "models")
DATA_DIR = os.path.join(BASE_DIR, "data")

@st.cache_resource
def load_model_pipeline():
    """Load model pipeline or components gracefully."""
    pipeline_path = os.path.join(MODEL_DIR, "ad_click_pipeline.pkl")
    model_path = os.path.join(MODEL_DIR, "ad_click_model.pkl")
    scaler_path = os.path.join(MODEL_DIR, "scaler.pkl")
    
    if os.path.exists(pipeline_path):
        return joblib.load(pipeline_path)
    elif os.path.exists(model_path) and os.path.exists(scaler_path):
        model = joblib.load(model_path)
        scaler = joblib.load(scaler_path)
        from sklearn.pipeline import Pipeline
        return Pipeline([('scaler', scaler), ('classifier', model)])
    else:
        raise FileNotFoundError("Model artifacts not found. Please train and save model first.")

@st.cache_data
def load_dataset():
    """Load dataset for EDA and benchmarks."""
    cleaned_path = os.path.join(DATA_DIR, "cleaned_ad_10000records.csv")
    raw_path = os.path.join(DATA_DIR, "ad_10000records.csv")
    if os.path.exists(cleaned_path):
        return pd.read_csv(cleaned_path)
    elif os.path.exists(raw_path):
        return pd.read_csv(raw_path)
    return None

try:
    pipeline = load_model_pipeline()
    model_loaded = True
except Exception as e:
    model_loaded = False
    model_load_error = str(e)

df_data = load_dataset()

# Sidebar Navigation
with st.sidebar:
    st.title("🎯 Ad Click AI")
    st.caption("Machine Learning powered user ad engagement predictor")
    st.markdown("---")
    
    navigation = st.radio(
        "Navigation Menu",
        ["🎯 Real-time Prediction", "📁 Batch Prediction (CSV)", "📊 Dataset & EDA Insights", "⚙️ Model Metrics & Info"]
    )
    
    st.markdown("---")
    st.markdown("### 📌 About Project")
    st.info(
        "**Target:** Predict whether an online user will click on a digital ad (`Clicked on Ad: 1/0`).\n\n"
        "**Algorithm:** Tuned Logistic Regression (`SAGA` solver + `L1` Regularization).\n\n"
        "**Dataset Size:** 10,000 user profiles."
    )

# Header
st.markdown('<div class="main-header">🎯 Online Ad Click Prediction Platform</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Analyze user behavioral attributes and forecast click-through probability in real-time.</div>', unsafe_allow_html=True)

if not model_loaded:
    st.error(f"⚠️ Error loading model: {model_load_error}")
    st.stop()

FEATURE_COLUMNS = ['Time on Site', 'Age', 'Area Income', 'Daily Internet Usage', 'Gender']

# --- TAB 1: REAL-TIME PREDICTION ---
if navigation == "🎯 Real-time Prediction":
    st.subheader("👤 User Profile Input")
    st.write("Adjust the behavioral and demographic features below to predict ad interaction:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        time_on_site = st.slider(
            "⏱️ Daily Time Spent on Site (minutes)",
            min_value=20.0,
            max_value=100.0,
            value=61.5,
            step=0.5,
            help="Average daily minutes the user spends on the website."
        )
        
        age = st.slider(
            "🎂 User Age (years)",
            min_value=18,
            max_value=70,
            value=35,
            step=1,
            help="Age of the targeted user."
        )
        
        gender_label = st.selectbox(
            "⚧️ Gender",
            options=["Male", "Female"],
            index=0,
            help="User's gender identity."
        )
        gender = 1 if gender_label == "Female" else 0

    with col2:
        area_income = st.number_input(
            "💰 Area Income ($ / year)",
            min_value=10000.0,
            max_value=100000.0,
            value=55000.0,
            step=500.0,
            help="Average income of the geographical area of the user."
        )
        
        daily_internet_usage = st.slider(
            "🌐 Daily Internet Usage (minutes)",
            min_value=90.0,
            max_value=300.0,
            value=180.0,
            step=1.0,
            help="Total daily minutes the user spends browsing the internet."
        )

    st.markdown("---")
    
    predict_btn = st.button("🚀 Predict Ad Click", type="primary", use_container_width=True)
    
    if predict_btn:
        input_data = pd.DataFrame([[
            time_on_site,
            age,
            area_income,
            daily_internet_usage,
            gender
        ]], columns=FEATURE_COLUMNS)
        
        prediction = pipeline.predict(input_data)[0]
        probabilities = pipeline.predict_proba(input_data)[0]
        click_prob = probabilities[1] * 100
        no_click_prob = probabilities[0] * 100
        
        st.markdown("### 📈 Prediction Results")
        
        res_col1, res_col2, res_col3 = st.columns([1.2, 1, 1])
        
        with res_col1:
            if prediction == 1:
                st.markdown(f"""
                <div class="result-card-click">
                    <h3 style="color: #065F46; margin:0;">🎯 LIKELY TO CLICK</h3>
                    <p style="color: #047857; margin-top:5px; font-size:1.1rem;">
                        The model predicts this user has a <b>high likelihood</b> of interacting with the ad.
                    </p>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class="result-card-noclick">
                    <h3 style="color: #991B1B; margin:0;">❌ UNLIKELY TO CLICK</h3>
                    <p style="color: #B91C1C; margin-top:5px; font-size:1.1rem;">
                        The model predicts this user is <b>unlikely</b> to click on the ad.
                    </p>
                </div>
                """, unsafe_allow_html=True)
                
        with res_col2:
            st.metric(label="Click Probability", value=f"{click_prob:.2f}%", delta=f"{click_prob - 50:.1f}% vs baseline")
            st.progress(float(click_prob / 100))
            
        with res_col3:
            st.metric(label="No-Click Probability", value=f"{no_click_prob:.2f}%")
            st.progress(float(no_click_prob / 100))

        st.markdown("---")
        
        # User vs Baseline Comparison
        st.subheader("🔍 Feature Profile Comparison (vs Dataset Median)")
        if df_data is not None:
            comparison_df = pd.DataFrame({
                "Feature": ["Time on Site (min)", "Age (years)", "Area Income ($)", "Daily Internet Usage (min)"],
                "User Input": [time_on_site, age, area_income, daily_internet_usage],
                "Dataset Median": [
                    df_data["Time on Site"].median(),
                    df_data["Age"].median(),
                    df_data["Area Income"].median(),
                    df_data["Daily Internet Usage"].median()
                ]
            })
            st.dataframe(comparison_df.style.format({"User Input": "{:,.2f}", "Dataset Median": "{:,.2f}"}), use_container_width=True)
            
        # Marketing Recommendations
        st.subheader("💡 Marketing Action Recommendations")
        if prediction == 1:
            st.success("""
            - **High Priority Impression:** Bid aggressively for this demographic segment.
            - **Action-Oriented Ad Creative:** Deliver immediate Call-To-Action (e.g., 'Claim Offer Now', 'Shop Now').
            - **Retargeting Strategy:** Include this profile in high-frequency conversion campaigns.
            """)
        else:
            st.warning("""
            - **Optimize Bid Cost:** Lower bid ceiling or suppress impression to minimize wasted ad spend.
            - **Brand Awareness Format:** If targeting is mandatory, test non-intrusive native sponsored content.
            - **Creative Refresh:** Test alternative messaging tailored for higher engagement.
            """)

# --- TAB 2: BATCH PREDICTION ---
elif navigation == "📁 Batch Prediction (CSV)":
    st.subheader("📁 Batch File Prediction")
    st.write("Upload a CSV file containing user records to run predictions in bulk.")
    
    sample_format = pd.DataFrame({
        'Time on Site': [68.95, 80.23, 45.12],
        'Age': [35, 31, 48],
        'Area Income': [61833.90, 68441.85, 41250.00],
        'Daily Internet Usage': [256.09, 193.77, 120.45],
        'Gender': [0, 1, 1]
    })
    
    with st.expander("ℹ️ Expected CSV Format & Template"):
        st.write("Columns required (or raw naming `Daily Time Spent on Site`):")
        st.dataframe(sample_format)
        csv_template = sample_format.to_csv(index=False).encode('utf-8')
        st.download_button("📥 Download Sample Template CSV", csv_template, "ad_click_sample_template.csv", "text/csv")
        
    uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])
    
    if uploaded_file is not None:
        try:
            batch_df = pd.read_csv(uploaded_file)
            st.write(f"**Loaded {len(batch_df)} rows.**")
            
            # Map column names if raw format is provided
            col_rename_map = {
                'Daily Time Spent on Site': 'Time on Site',
                'Male': 'Gender'
            }
            batch_df = batch_df.rename(columns=col_rename_map)
            
            # Encode gender if strings
            if 'Gender' in batch_df.columns and batch_df['Gender'].dtype == 'object':
                batch_df['Gender'] = batch_df['Gender'].astype(str).str.strip().map({'Male': 0, 'Female': 1, '0': 0, '1': 1})
            
            # Check for required features
            missing_cols = [c for c in FEATURE_COLUMNS if c not in batch_df.columns]
            if missing_cols:
                st.error(f"Missing required columns in CSV: {missing_cols}")
            else:
                X_batch = batch_df[FEATURE_COLUMNS]
                preds = pipeline.predict(X_batch)
                probs = pipeline.predict_proba(X_batch)[:, 1]
                
                result_df = batch_df.copy()
                result_df['Predicted_Click'] = preds
                result_df['Click_Probability (%)'] = np.round(probs * 100, 2)
                result_df['Decision'] = result_df['Predicted_Click'].map({1: '🎯 Likely Click', 0: '❌ No Click'})
                
                st.success("✅ Batch predictions calculated successfully!")
                
                bcol1, bcol2, bcol3 = st.columns(3)
                total_records = len(result_df)
                total_clicks = int(result_df['Predicted_Click'].sum())
                click_rate = (total_clicks / total_records) * 100
                
                bcol1.metric("Total Records", total_records)
                bcol2.metric("Predicted Clicks", total_clicks)
                bcol3.metric("Predicted Click Rate", f"{click_rate:.2f}%")
                
                st.dataframe(result_df, use_container_width=True)
                
                output_csv = result_df.to_csv(index=False).encode('utf-8')
                st.download_button(
                    label="📥 Download Predictions as CSV",
                    data=output_csv,
                    file_name="ad_click_predictions_output.csv",
                    mime="text/csv",
                    type="primary"
                )
        except Exception as err:
            st.error(f"Error processing CSV: {err}")

# --- TAB 3: DATASET & EDA INSIGHTS ---
elif navigation == "📊 Dataset & EDA Insights":
    st.subheader("📊 Exploratory Data Analysis & Statistics")
    
    if df_data is not None:
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Total Dataset Records", f"{len(df_data):,}")
        m2.metric("Features Count", len(df_data.columns))
        click_pct = (df_data['Clicked on Ad'].mean() * 100) if 'Clicked on Ad' in df_data.columns else 50.0
        m3.metric("Click-Through Rate", f"{click_pct:.1f}%")
        avg_age = df_data['Age'].mean() if 'Age' in df_data.columns else 36.0
        m4.metric("Average User Age", f"{avg_age:.1f} yrs")
        
        st.markdown("---")
        
        tab_eda1, tab_eda2, tab_eda3 = st.tabs(["📈 Distributions", "🔥 Correlations", "👥 Demographic Trends"])
        
        with tab_eda1:
            st.write("#### Feature Distributions")
            fig, axes = plt.subplots(2, 2, figsize=(12, 8))
            
            sns.histplot(df_data['Time on Site'], kde=True, ax=axes[0, 0], color='#3B82F6')
            axes[0, 0].set_title('Daily Time on Site Distribution')
            
            sns.histplot(df_data['Age'], kde=True, ax=axes[0, 1], color='#10B981')
            axes[0, 1].set_title('Age Distribution')
            
            sns.histplot(df_data['Area Income'], kde=True, ax=axes[1, 0], color='#F59E0B')
            axes[1, 0].set_title('Area Income Distribution')
            
            sns.histplot(df_data['Daily Internet Usage'], kde=True, ax=axes[1, 1], color='#8B5CF6')
            axes[1, 1].set_title('Daily Internet Usage Distribution')
            
            plt.tight_layout()
            st.pyplot(fig)
            
        with tab_eda2:
            st.write("#### Correlation Heatmap")
            fig_corr, ax_corr = plt.subplots(figsize=(8, 6))
            numeric_df = df_data.select_dtypes(include=[np.number])
            sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', fmt=".2f", ax=ax_corr)
            plt.title("Correlation Matrix of Numeric Features")
            st.pyplot(fig_corr)
            
        with tab_eda3:
            st.write("#### Click Behavior by Demographics")
            col_d1, col_d2 = st.columns(2)
            
            with col_d1:
                fig_age, ax_age = plt.subplots(figsize=(6, 4))
                sns.boxplot(x='Clicked on Ad', y='Age', data=df_data, palette=['#60A5FA', '#F87171'], ax=ax_age)
                ax_age.set_xticklabels(['No Click (0)', 'Clicked (1)'])
                ax_age.set_title("Age vs Ad Click Status")
                st.pyplot(fig_age)
                
            with col_d2:
                fig_net, ax_net = plt.subplots(figsize=(6, 4))
                sns.scatterplot(
                    x='Time on Site', 
                    y='Daily Internet Usage', 
                    hue='Clicked on Ad', 
                    data=df_data.sample(min(1000, len(df_data)), random_state=42),
                    palette=['#3B82F6', '#EF4444'],
                    alpha=0.7,
                    ax=ax_net
                )
                ax_net.set_title("Time on Site vs Internet Usage (Sampled)")
                st.pyplot(fig_net)
    else:
        st.warning("Dataset CSV not found to display EDA charts.")

# --- TAB 4: MODEL METRICS & INFO ---
elif navigation == "⚙️ Model Metrics & Info":
    st.subheader("⚙️ Model Architecture & Evaluation Performance")
    
    st.markdown("""
    ### 🏆 Best Model Details:
    - **Classifier:** Logistic Regression
    - **Optimization Solver:** `SAGA`
    - **Regularization:** `L1` (Lasso) penalty ($C = 0.01$)
    - **Pre-processing:** `StandardScaler` (Zero Mean, Unit Variance)
    """)
    
    mcol1, mcol2, mcol3, mcol4 = st.columns(4)
    mcol1.metric("Validation Accuracy", "72.25%")
    mcol2.metric("ROC-AUC Score", "0.774")
    mcol3.metric("Precision (Clicks)", "0.74")
    mcol4.metric("Recall (Clicks)", "0.67")
    
    st.markdown("---")
    
    st.subheader("⚖️ Feature Weights (Logistic Regression Coefficients)")
    if hasattr(pipeline.named_steps.get('classifier'), 'coef_'):
        coefs = pipeline.named_steps['classifier'].coef_[0]
        coef_df = pd.DataFrame({
            "Feature": FEATURE_COLUMNS,
            "Coefficient": coefs,
            "Impact": ["Positive (Increases Click Chance)" if c > 0 else "Negative (Decreases Click Chance)" for c in coefs]
        }).sort_values(by="Coefficient", ascending=False)
        
        st.dataframe(coef_df.style.format({"Coefficient": "{:.4f}"}), use_container_width=True)
        
        fig_coef, ax_coef = plt.subplots(figsize=(8, 4))
        colors = ['#10B981' if c > 0 else '#EF4444' for c in coef_df['Coefficient']]
        ax_coef.barh(coef_df['Feature'], coef_df['Coefficient'], color=colors)
        ax_coef.set_xlabel('Coefficient Value (Normalized Scale)')
        ax_coef.set_title('Feature Importance & Directional Impact')
        ax_coef.axvline(0, color='black', linewidth=0.8, linestyle='--')
        plt.tight_layout()
        st.pyplot(fig_coef)
