# Social Network Ads - Purchase Prediction

A machine learning project that predicts whether a user will purchase a product based on social network advertisement data using Support Vector Machine (SVM) classification.

## Project Overview

This project analyzes social network advertisement data to predict customer purchase behavior based on demographic and salary information. The model achieves **93% accuracy** in predicting whether a customer will make a purchase.

## Dataset

**Source:** Social_Network_Ads.csv

**Features:**
- `User ID` - Unique identifier for each user
- `Gender` - Male/Female
- `Age` - Age of the user
- `EstimatedSalary` - Estimated annual salary
- `Purchased` - Target variable (0 = No Purchase, 1 = Purchase)

**Dataset Size:** 400 records

## Project Structure

```
Social network Ads/
├── app.py                          # Streamlit web application
├── svc.ipynb                       # Main notebook with model training
├── model.pkl                       # Trained model and scaler (pickled)
├── Social_Network_Ads.csv          # Dataset
├── data/
│   └── dataset.py                  # Kaggle dataset downloader
└── prediction/
    └── prediction.ipynb            # Prediction testing notebook
```

## Technology Stack

- **Python Libraries:**
  - `pandas` - Data manipulation
  - `numpy` - Numerical operations
  - `scikit-learn` - Machine learning (SVM, StandardScaler)
  - `matplotlib` & `seaborn` - Data visualization
  - `streamlit` - Web application framework
  - `joblib` - Model serialization
  - `kagglehub` - Dataset download

## Machine Learning Model

**Algorithm:** Support Vector Machine (SVM)

**Preprocessing:**
- Feature scaling using StandardScaler
- Gender encoding (Male=1, Female=0)

**Model Performance:** 93% accuracy

## Installation & Setup

1. Clone or download the project

2. Install required dependencies:
```bash
pip install streamlit pandas numpy scikit-learn matplotlib seaborn joblib kagglehub
```

3. Ensure the dataset and model files are in the project directory

## Usage

### Running the Web Application

Launch the Streamlit app:
```bash
streamlit run app.py
```

The web interface allows you to:
- Input customer details (Gender, Age, Estimated Salary)
- Get instant purchase predictions
- View model information and accuracy

### Making Predictions Programmatically

Use the prediction notebook or load the model directly:

```python
import joblib
import numpy as np

# Load model
data = joblib.load("model.pkl")
model = data['model']
scaler = data['scaler']

# Prepare input (Gender, Age, Salary)
new_data = np.array([[1, 35, 50000]])  # Male, 35 years, $50k
new_data_scaled = scaler.transform(new_data)

# Predict
prediction = model.predict(new_data_scaled)
print("Purchase" if prediction[0] == 1 else "No Purchase")
```

## Model Training

The model training process is documented in `svc.ipynb` and includes:
1. Data loading and exploration
2. Exploratory Data Analysis (EDA)
3. Feature engineering and encoding
4. Data preprocessing and scaling
5. Model training with SVM
6. Model evaluation
7. Model serialization

## Files Description

- **app.py** - Interactive Streamlit web application for real-time predictions
- **svc.ipynb** - Complete model development pipeline with EDA and training
- **model.pkl** - Serialized model bundle containing trained SVM and StandardScaler
- **prediction.ipynb** - Standalone prediction testing notebook
- **dataset.py** - Script to download dataset from Kaggle

## Features of Web App

- User-friendly interface
- Real-time predictions
- Model information sidebar
- Input validation
- Clear prediction results

## Future Enhancements

- Add more features for improved accuracy
- Implement additional ML algorithms for comparison
- Add model performance metrics visualization
- Deploy to cloud platform
- Add A/B testing capabilities

## Author

Data Science ML Project - 2026

## License

This project is for educational purposes.
