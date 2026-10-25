# Real-World Machine Learning Projects

## Portfolio Track

These 4 projects are designed as **company-oriented, real-world ML projects** rather than basic algorithm demonstrations.

| # | Project | ML Area | Dataset | Main Goal |
|---|---|---|---|---|
| 1 | Intrusion Detection System | Classification + Anomaly Detection | CICIDS2017 | Detect malicious network traffic |
| 2 | Recommendation System | Recommender Systems | MovieLens 25M | Recommend relevant items to users |
| 3 | Human Activity Recognition | Sequential / Time-Series Classification | UCI HAR | Recognize human activities from sensor data |
| 4 | Dynamic Demand Forecasting | Regression + Time Series | M5 Forecasting - Accuracy | Forecast product demand for inventory planning |

---

# 1. Intrusion Detection System

## Company Problem

A company receives huge amounts of network traffic every second. Manually identifying malicious traffic is impossible.

The system should:

- Detect normal vs malicious traffic
- Identify the type of attack
- Handle highly imbalanced data
- Produce an attack/risk probability
- Generate alerts for suspicious traffic

## Dataset

**CICIDS2017 — Canadian Institute for Cybersecurity Intrusion Detection System Dataset**

Source: https://www.unb.ca/cic/datasets/ids-2017.html

### Dataset contains

- Network flow information
- Protocol information
- Packet statistics
- Duration
- Source/Destination information
- Normal traffic
- Multiple attack types

### Example attack categories

- DDoS
- DoS
- Brute Force
- Port Scan
- Bot
- Web Attack

## ML Pipeline

```text
Network Traffic
      ↓
Data Cleaning
      ↓
EDA
      ↓
Feature Engineering
      ↓
Imbalance Handling
      ↓
Classification Model
      ↓
Attack Prediction
      ↓
Risk Score
      ↓
Security Alert
```

## Models

Start with:

- Logistic Regression
- Random Forest

Then move to:

- XGBoost
- LightGBM

Advanced:

- Anomaly Detection
- Isolation Forest
- Autoencoder

## Evaluation

Do not rely only on accuracy.

Use:

- Precision
- Recall
- F1-score
- Confusion Matrix
- ROC-AUC / PR-AUC

For security, **False Negatives are especially important** because a missed attack can be costly.

## Advanced Features

- Attack-type classification
- Probability-based risk score
- Threshold optimization
- SHAP explainability
- Anomaly detection
- Real-time prediction API
- Monitoring dashboard

## Deployment Idea

```text
Network Flow
     ↓
FastAPI / Flask
     ↓
ML Model
     ↓
Risk Score
     ↓
Alert
     ↓
Dashboard
```

---

# 2. Recommendation System

## Company Problem

Platforms such as Netflix, Amazon and YouTube have millions of users and items.

Showing the same content to everyone is ineffective.

The system should learn from user behavior and recommend relevant items.

## Dataset

**MovieLens 25M**

Source: https://grouplens.org/datasets/movielens/25m/

### Dataset contains

- 25M+ ratings
- Users
- Movies
- Ratings
- Tags
- Movie metadata

## ML Pipeline

```text
User Behavior
     ↓
User Profile + Item Profile
     ↓
Candidate Generation
     ↓
Recommendation Model
     ↓
Ranking
     ↓
Top-K Recommendations
```

## Recommendation Approaches

### Level 1 — Collaborative Filtering

Learn:

```text
User ↔ Movie
```

using ratings/interactions.

Possible methods:

- User-User similarity
- Item-Item similarity
- Matrix Factorization

### Level 2 — Content-Based

Use movie information such as:

- Genres
- Tags
- Metadata

Then recommend similar items.

### Level 3 — Hybrid

Combine:

```text
Collaborative Filtering
        +
Content-Based
```

### Advanced Architecture

```text
User
 ↓
User Embedding
 ↓
Candidate Generation
 ↓
Item Embeddings
 ↓
Ranking Model
 ↓
Top-K Recommendations
```

## Evaluation

Do not evaluate only with RMSE.

For recommendation systems use:

- Precision@K
- Recall@K
- MAP@K
- NDCG@K

Example:

```text
Top 10 recommendations
        ↓
How many were actually relevant?
```

## Advanced Features

- Cold-start handling
- Hybrid recommendation
- User/item embeddings
- Candidate generation
- Ranking model
- Personalized recommendations
- Recommendation API
- Feedback loop

## Deployment Idea

```text
User
 ↓
API
 ↓
Recommendation Engine
 ↓
Candidate Generation
 ↓
Ranking
 ↓
Top 10 Movies
```

---

# 3. Human Activity Recognition

## Company Problem

Smartphones and wearable devices continuously collect sensor data.

The system can use this data to identify what a person is doing.

Possible applications:

- Fitness tracking
- Healthcare monitoring
- Smart devices
- Elderly monitoring
- Activity analytics

## Dataset

**UCI Human Activity Recognition Using Smartphones**

Source: https://archive.ics.uci.edu/dataset/240/human+activity+recognition+using+smartphones

## Sensors

The dataset uses:

- Accelerometer
- Gyroscope

## Activities

- Walking
- Walking Upstairs
- Walking Downstairs
- Sitting
- Standing
- Laying

## ML Pipeline

```text
Sensor Data
     ↓
Time Windows
     ↓
Feature Extraction
     ↓
Preprocessing
     ↓
Classification
     ↓
Activity Prediction
```

## Important Concept

This is different from normal tabular classification.

Instead of:

```text
One Row → One Prediction
```

we have:

```text
Sequence of Sensor Readings
            ↓
       One Activity
```

## Models

Start with:

- Logistic Regression
- Random Forest
- XGBoost

Advanced:

- 1D CNN
- LSTM
- GRU

## Evaluation

Use:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix

Important:

Use a **subject-wise split** so that the model does not simply memorize individual users.

## Advanced Features

- Sensor fusion
- Sliding-window prediction
- Real-time activity prediction
- 1D CNN
- LSTM/GRU
- Mobile/API deployment
- Activity dashboard

## Deployment Idea

```text
Sensor Data
     ↓
Sliding Window
     ↓
ML/DL Model
     ↓
Activity
     ↓
Real-Time Dashboard
```

---

# 4. Dynamic Demand Forecasting

## Company Problem

A retail company needs to know how many products will be sold in the future.

If demand is underestimated:

```text
Stockout → Lost Sales
```

If demand is overestimated:

```text
Excess Inventory → Higher Cost
```

The goal is therefore not simply to predict sales, but to support inventory decisions.

## Dataset

**M5 Forecasting - Accuracy**

Source: https://www.kaggle.com/competitions/m5-forecasting-accuracy

## Dataset Contains

- Walmart sales
- Products
- Stores
- States
- Calendar information
- Prices
- Historical daily demand
- Events
- Promotional information

## ML Pipeline

```text
Historical Sales
       ↓
Data Cleaning
       ↓
Time-Series Analysis
       ↓
Feature Engineering
       ↓
Lag Features
       ↓
Rolling Statistics
       ↓
ML Model
       ↓
Future Demand
       ↓
Inventory Decision
```

## Important Features

### Lag Features

Examples:

```text
sales_lag_1
sales_lag_7
sales_lag_28
```

### Rolling Features

Examples:

```text
7-day average
28-day average
7-day standard deviation
```

### Other Features

- Day of week
- Month
- Year
- Holiday
- Price
- Promotion
- Store
- Product

## Models

Start with:

- Linear Regression
- Random Forest

Then:

- XGBoost
- LightGBM

Advanced:

- Ensemble Forecasting
- Deep Learning Time-Series Models

## Important Rule

Do **not** use random `train_test_split()` for this project.

Use a **time-based split**:

```text
Past Data ─────────────→ Future Data

Train       Validation      Test
```

Otherwise future information can leak into training.

## Evaluation

Use forecasting metrics such as:

- MAE
- RMSE
- WMAPE

The final goal should connect prediction with business decisions.

## Advanced Features

- Multi-step forecasting
- Store-level forecasting
- Product-level forecasting
- Stockout risk
- Reorder recommendation
- Forecast dashboard
- Model monitoring

## Deployment Idea

```text
Historical Sales
       ↓
Forecasting API
       ↓
Predicted Demand
       ↓
Inventory Logic
       ↓
Reorder Recommendation
```

---

# Overall Project Architecture

These projects should not be treated as:

```text
Dataset → Model → Accuracy → Done
```

Instead, build them as:

```text
Real Business Problem
        ↓
Data Collection / Dataset
        ↓
Data Cleaning
        ↓
EDA
        ↓
Feature Engineering
        ↓
Baseline Model
        ↓
Advanced Model
        ↓
Proper Evaluation
        ↓
Explainability
        ↓
API / Application
        ↓
Monitoring
```

---

# Project Difficulty

| Project | Difficulty | Main Challenge |
|---|---:|---|
| Dynamic Demand Forecasting | ★★★★★ | Time-series + leakage + forecasting |
| Intrusion Detection | ★★★★★ | Imbalance + anomaly detection + realistic validation |
| Recommendation System | ★★★★★ | Candidate generation + ranking |
| Human Activity Recognition | ★★★★☆ | Sequential data + sensor signals |

---

# Recommended Order

For your portfolio, follow this order:

### 1. Intrusion Detection System

Learn:

- Imbalanced classification
- Anomaly detection
- Threshold optimization
- Explainability

### 2. Recommendation System

Learn:

- Collaborative filtering
- Embeddings
- Ranking
- Recommendation evaluation

### 3. Human Activity Recognition

Learn:

- Sequential data
- Time windows
- Sensor data
- CNN/LSTM/GRU

### 4. Dynamic Demand Forecasting

Learn:

- Time-series feature engineering
- Lag/rolling features
- Forecasting
- Business optimization

---

# Final Portfolio Goal

Each project should eventually contain:

```text
Dataset
   ↓
EDA
   ↓
Feature Engineering
   ↓
Baseline
   ↓
Advanced ML
   ↓
Model Comparison
   ↓
Error Analysis
   ↓
Explainability
   ↓
API
   ↓
Web Dashboard
   ↓
Docker
   ↓
Deployment
   ↓
README + Architecture
```

The final projects should demonstrate **ML problem-solving and system thinking**, not just that you know how to call `fit()` on an algorithm.
