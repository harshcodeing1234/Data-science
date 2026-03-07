# Automated ML Pipeline - Regression Analysis

import streamlit as st #type:ignore
import numpy as np #type:ignore
import pandas as pd #type:ignore
import matplotlib.pyplot as plt #type:ignore
import seaborn as sns #type:ignore
from sklearn.model_selection import train_test_split #type:ignore
from sklearn.preprocessing import StandardScaler, LabelEncoder #type:ignore
from sklearn.linear_model import LinearRegression, Lasso, RidgeCV, ElasticNet, ElasticNetCV #type:ignore
from sklearn.metrics import mean_absolute_error, r2_score #type:ignore
import warnings #type:ignore
warnings.filterwarnings('ignore') #type:ignore

# Page configuration
st.set_page_config(page_title="Auto ML Pipeline", layout="wide")
st.title("🤖 Automated ML Pipeline - Regression Analysis")

# HELPER FUNCTIONS

def check_data_quality(df):
    """Check if data needs cleaning"""
    issues = []
    if df.isnull().sum().sum() > 0:
        issues.append(f"⚠️ Found {df.isnull().sum().sum()} missing values")
    if (df.dtypes == 'object').any():
        obj_cols = df.select_dtypes(include=['object']).columns.tolist()
        issues.append(f"⚠️ Found object columns: {', '.join(obj_cols)}")
    return issues

def encode_categorical(df):
    """Encode categorical columns"""
    encoders = {}
    encoded_cols = []
    for col in df.select_dtypes(include=['object']).columns:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col].astype(str))
        encoders[col] = le
        encoded_cols.append(col)
    return df, encoders, encoded_cols

def remove_correlated_features(x_train, x_test, threshold=0.85):
    """Remove highly correlated features"""
    col_corr = set()
    corr_matrix = x_train.corr()
    for i in range(len(corr_matrix.columns)):
        for j in range(i):
            if abs(corr_matrix.iloc[i, j]) > threshold:
                col_corr.add(corr_matrix.columns[i])
    if col_corr:
        x_train = x_train.drop(columns=col_corr)
        x_test = x_test.drop(columns=col_corr)
    return x_train, x_test, list(col_corr)

def train_all_models(x_train, x_test, y_train, y_test):
    """Train multiple regression models"""
    models = {
        "Linear Regression": LinearRegression(),
        "Lasso": Lasso(),
        "Ridge (CV)": RidgeCV(),
        "ElasticNet": ElasticNet(),
        "ElasticNet (CV)": ElasticNetCV()
    }
    results = []
    trained_models = {}
    for name, model in models.items():
        model.fit(x_train, y_train)
        y_pred = model.predict(x_test)
        mae = mean_absolute_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        results.append({"Model": name, "MAE": round(mae, 4), "R² Score": round(r2, 4)})
        trained_models[name] = (model, y_pred)
    return results, trained_models

# SIDEBAR 
st.sidebar.header("📁 Upload Dataset")
uploaded_file = st.sidebar.file_uploader("Upload Clean CSV File", type=['csv'])

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
        
        # Check data quality
        issues = check_data_quality(df)
        if issues:
            st.warning("### ⚠️ Data Quality Issues:")
            for issue in issues:
                st.write(issue)
            st.error("**Please upload cleaned data!**")
            st.stop()
        
        # Configuration
        st.sidebar.header("⚙️ Configuration")
        target_column = st.sidebar.selectbox("Select Target Column", df.columns.tolist())
        test_size = st.sidebar.slider("Test Size (%)", 10, 40, 25) / 100
        correlation_threshold = st.sidebar.slider("Correlation Threshold", 0.70, 0.95, 0.85, 0.05)
        
        # Navigation
        st.sidebar.header("📑 Navigation")
        section = st.sidebar.radio("Go to Section:", [
            "1. Data Overview",
            "2. Encoding",
            "3. EDA",
            "4. Feature Split",
            "5. Train-Test Split",
            "6. Correlation Analysis",
            "7. Standard Scaling",
            "8. Model Training",
            "9. Prediction"
        ])
        
        # Process data for all sections
        df_encoded = df.copy()
        encoded_cols = []
        if (df.dtypes == 'object').any():
            df_encoded, _, encoded_cols = encode_categorical(df.copy())
        
        #  SECTION 1: DATA OVERVIEW
        if section == "1. Data Overview":
            st.header("📊 1. Data Overview")
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Total Rows", df.shape[0])
            with col2:
                st.metric("Total Columns", df.shape[1])
            with col3:
                st.metric("Missing Values", df.isnull().sum().sum())
            
            st.subheader("Dataset Preview")
            st.dataframe(df.head(10), width='stretch')
            
            st.subheader("Data Types")
            st.dataframe(df.dtypes.astype(str).to_frame(name='Type'), width='stretch')
        
        # SECTION 2: ENCODING 
        elif section == "2. Encoding":
            st.header("🔤 2. Encoding Categorical Variables")
            
            if encoded_cols:
                st.success(f"✅ Encoded columns: {', '.join(encoded_cols)}")
                
                col1, col2 = st.columns(2)
                with col1:
                    st.subheader("Before Encoding")
                    st.dataframe(df.head(), width='stretch')
                with col2:
                    st.subheader("After Encoding")
                    st.dataframe(df_encoded.head(), width='stretch')
            else:
                st.info("ℹ️ No categorical columns found. Data is already numeric.")
                st.dataframe(df_encoded.head(), width='stretch')
        
        # SECTION 3: EDA 
        elif section == "3. EDA":
            st.header("📈 3. Exploratory Data Analysis")
            
            tab1, tab2, tab3 = st.tabs(["Distribution", "Correlation", "Statistics"])
            
            with tab1:
                st.subheader("Feature Distribution")
                numeric_cols = df_encoded.select_dtypes(include=[np.number]).columns.tolist()
                selected_cols = st.multiselect("Select columns", numeric_cols, default=numeric_cols[:4])
                
                if selected_cols:
                    fig, axes = plt.subplots(2, 2, figsize=(10, 6))
                    axes = axes.flatten()
                    for idx, col in enumerate(selected_cols[:4]):
                        df_encoded[col].hist(bins=20, ax=axes[idx], edgecolor='black', alpha=0.7)
                        axes[idx].set_title(col, fontsize=10)
                    for idx in range(len(selected_cols), 4):
                        axes[idx].axis('off')
                    plt.tight_layout()
                    st.pyplot(fig)
            
            with tab2:
                st.subheader("Correlation Heatmap")
                numeric_df = df_encoded.select_dtypes(include=[np.number])
                fig, ax = plt.subplots(figsize=(10, 6))
                sns.heatmap(numeric_df.corr(), annot=True, fmt='.2f', cmap='coolwarm', 
                           ax=ax, cbar_kws={'shrink': 0.8}, linewidths=0.5)
                plt.tight_layout()
                st.pyplot(fig)
            
            with tab3:
                st.subheader("Statistical Summary")
                st.dataframe(df_encoded.describe(), width='stretch')
        
        #  SECTION 4: FEATURE SPLIT 
        elif section == "4. Feature Split":
            st.header("🔧 4. Feature & Target Split")
            
            X = df_encoded.drop(columns=[target_column])
            y = df_encoded[target_column]
            
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Number of Features", X.shape[1])
                st.write("**Features:**")
                st.write(list(X.columns))
            with col2:
                st.metric("Target Variable", target_column)
                st.write("**Target Info:**")
                st.write(f"- Min: {y.min():.2f}")
                st.write(f"- Max: {y.max():.2f}")
                st.write(f"- Mean: {y.mean():.2f}")
            
            st.subheader("Features (X)")
            st.dataframe(X.head(), width='stretch')
            
            st.subheader("Target (y)")
            st.dataframe(y.head().to_frame(), width='stretch')
        
        #  SECTION 5: TRAIN-TEST SPLIT 
        elif section == "5. Train-Test Split":
            st.header("✂️ 5. Train-Test Split")
            
            X = df_encoded.drop(columns=[target_column])
            y = df_encoded[target_column]
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Total Samples", len(X))
            with col2:
                st.metric("Training Samples", len(X_train))
            with col3:
                st.metric("Testing Samples", len(X_test))
            
            st.subheader("Training Set")
            st.dataframe(X_train.head(), width='stretch')
            
            st.subheader("Testing Set")
            st.dataframe(X_test.head(), width='stretch')
        
        # SECTION 6: CORRELATION ANALYSIS 
        elif section == "6. Correlation Analysis":
            st.header("🔗 6. Correlation Analysis & Feature Selection")
            
            X = df_encoded.drop(columns=[target_column])
            y = df_encoded[target_column]
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)
            
            st.subheader(f"Removing features with correlation > {correlation_threshold}")
            
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Features Before", X_train.shape[1])
            
            X_train_fs, X_test_fs, removed_features = remove_correlated_features(
                X_train.copy(), X_test.copy(), correlation_threshold
            )
            
            with col2:
                st.metric("Features After", X_train_fs.shape[1])
            
            if removed_features:
                st.warning(f"🗑️ Removed {len(removed_features)} highly correlated features:")
                st.write(removed_features)
            else:
                st.success("✅ No highly correlated features found!")
            
            st.subheader("Remaining Features")
            st.write(list(X_train_fs.columns))
        
        # SECTION 7: STANDARD SCALING
        elif section == "7. Standard Scaling":
            st.header("⚖️ 7. Standard Scaling")
            
            X = df_encoded.drop(columns=[target_column])
            y = df_encoded[target_column]
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)
            X_train_fs, X_test_fs, _ = remove_correlated_features(X_train.copy(), X_test.copy(), correlation_threshold)
            
            scaler = StandardScaler()
            X_train_scaled = scaler.fit_transform(X_train_fs)
            X_test_scaled = scaler.transform(X_test_fs)
            
            st.success("✅ Standard scaling applied using StandardScaler!")
            
            col1, col2 = st.columns(2)
            with col1:
                st.subheader("Before Scaling")
                st.dataframe(pd.DataFrame(X_train_fs.head(5)), width='stretch')
                st.write(f"Mean: {X_train_fs.mean().mean():.2f}")
                st.write(f"Std: {X_train_fs.std().mean():.2f}")
            
            with col2:
                st.subheader("After Scaling")
                st.dataframe(pd.DataFrame(X_train_scaled[:5], columns=X_train_fs.columns), width='stretch')
                st.write(f"Mean: {X_train_scaled.mean():.2f}")
                st.write(f"Std: {X_train_scaled.std():.2f}")
            
            # Visualization
            st.subheader("Scaling Visualization")
            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
            ax1.boxplot(X_train_fs.values)
            ax1.set_title("Before Scaling")
            ax1.set_ylabel("Value")
            ax2.boxplot(X_train_scaled)
            ax2.set_title("After Scaling")
            ax2.set_ylabel("Value")
            plt.tight_layout()
            st.pyplot(fig)
        
        # SECTION 8: MODEL TRAINING 
        elif section == "8. Model Training":
            st.header("🤖 8. Model Training & Evaluation")
            
            X = df_encoded.drop(columns=[target_column])
            y = df_encoded[target_column]
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)
            X_train_fs, X_test_fs, _ = remove_correlated_features(X_train.copy(), X_test.copy(), correlation_threshold)
            
            scaler = StandardScaler()
            X_train_scaled = scaler.fit_transform(X_train_fs)
            X_test_scaled = scaler.transform(X_test_fs)
            
            with st.spinner("Training models..."):
                results, trained_models = train_all_models(X_train_scaled, X_test_scaled, y_train, y_test)
            
            results_df = pd.DataFrame(results).sort_values('R² Score', ascending=False)
            
            st.subheader("📊 Model Performance Comparison")
            st.dataframe(
                results_df.style.highlight_max(subset=['R² Score'], color='lightgreen')
                               .highlight_min(subset=['MAE'], color='lightgreen'),
                width='stretch'
            )
            
            # Best model
            best_model_name = results_df.iloc[0]['Model']
            best_mae = results_df.iloc[0]['MAE']
            best_r2 = results_df.iloc[0]['R² Score']
            
            st.success(f"### 🏆 Best Model: **{best_model_name}**")
            col1, col2 = st.columns(2)
            with col1:
                st.metric("MAE", f"{best_mae:.4f}")
            with col2:
                st.metric("R² Score", f"{best_r2:.4f}")
            
            # Visualizations
            st.subheader("Model Predictions Visualization")
            for name, (model, y_pred) in trained_models.items():
                with st.expander(f"📊 {name}"):
                    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
                    
                    ax1.scatter(y_test, y_pred, alpha=0.6, s=30)
                    ax1.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
                    ax1.set_xlabel('Actual')
                    ax1.set_ylabel('Predicted')
                    ax1.set_title('Actual vs Predicted')
                    ax1.grid(True, alpha=0.3)
                    
                    residuals = y_test - y_pred
                    ax2.scatter(y_pred, residuals, alpha=0.6, s=30)
                    ax2.axhline(y=0, color='r', linestyle='--', lw=2)
                    ax2.set_xlabel('Predicted')
                    ax2.set_ylabel('Residuals')
                    ax2.set_title('Residual Plot')
                    ax2.grid(True, alpha=0.3)
                    
                    plt.tight_layout()
                    st.pyplot(fig)
            
            # Store in session state
            st.session_state['scaler'] = scaler
            st.session_state['all_models'] = trained_models
            st.session_state['best_model'] = trained_models[best_model_name][0]
            st.session_state['features'] = X_train_fs.columns.tolist()
            st.session_state['target'] = target_column
            st.session_state['best_model_name'] = best_model_name
        
        # SECTION 9: PREDICTION 
        elif section == "9. Prediction":
            st.header("🔮 9. Make New Predictions")
            
            if 'all_models' not in st.session_state:
                st.warning("⚠️ Please train the model first in Section 8!")
                st.stop()
            
            # Model selection
            st.subheader("Select Model for Prediction")
            available_models = list(st.session_state['all_models'].keys())
            
            col1, col2 = st.columns([2, 1])
            with col1:
                selected_model_name = st.selectbox(
                    "Choose a model:",
                    available_models,
                    index=available_models.index(st.session_state['best_model_name'])
                )
            with col2:
                st.metric("Best Model", st.session_state['best_model_name'])
            
            selected_model = st.session_state['all_models'][selected_model_name][0]
            
            if selected_model_name == st.session_state['best_model_name']:
                st.success(f"✅ Using **{selected_model_name}** (Best Model)")
            else:
                st.info(f"Using **{selected_model_name}**")
            
            st.subheader("Enter Feature Values")
            features = st.session_state['features']
            input_data = {}
            
            cols = st.columns(3)
            for idx, feature in enumerate(features):
                with cols[idx % 3]:
                    input_data[feature] = st.number_input(
                        feature,
                        value=0.0,
                        format="%.2f",
                        key=f"input_{feature}"
                    )
            
            if st.button("🎯 Predict", type="primary"):
                input_df = pd.DataFrame([input_data])
                input_scaled = st.session_state['scaler'].transform(input_df)
                prediction = selected_model.predict(input_scaled)[0]
                
                st.success(f"### 🎯 Predicted {st.session_state['target']}: **{prediction:.4f}**")
                
                col1, col2, col3 = st.columns(3)
                with col1:
                    if prediction > 10:
                        st.error("🔴 High Risk")
                    elif prediction > 5:
                        st.warning("🟡 Medium Risk")
                    else:
                        st.info("🟢 Low Risk")
                
                with col2:
                    st.metric("Prediction Value", f"{prediction:.4f}")
                
                with col3:
                    st.metric("Model Used", selected_model_name)
    
    except Exception as e:
        st.error(f"❌ Error: {str(e)}")
        st.exception(e)

else:
    st.info("👈 Please upload a CSV file to begin")
    st.markdown("""
    ### 📋 Pipeline Sections:
    1. **Data Overview** - View dataset information
    2. **Encoding** - Auto-encode categorical variables
    3. **EDA** - Exploratory data analysis
    4. **Feature Split** - Separate features and target
    5. **Train-Test Split** - Split data for training/testing
    6. **Correlation Analysis** - Remove correlated features
    7. **Standard Scaling** - Normalize features
    8. **Model Training** - Train and compare 5 models
    9. **Prediction** - Make predictions with best model
    
    ### ⚠️ Requirements:
    - Upload **cleaned data** (no missing values)
    """)
