**This works:** is project ko ek proper end-to-end ML system ki tarah build karna chahiye, sirf Decision Tree notebook ki tarah nahi.

# Project Name

## **Predictive Maintenance & Machine Failure Risk Decision System**

**Short name:** `Predictive Maintenance System`

### Core objective

Machine ke operating data ko dekhkar predict karna:

> **“Kya machine failure hone ka risk hai?”**

Aur prediction ke baad system **recommended action** bhi dega:

```text
Machine Data
     ↓
Decision Tree
     ↓
Failure Risk
     ↓
Explain Why
     ↓
Maintenance Recommendation
```

---

# 1. Project Requirements

## A. Dataset

Use:

**AI4I 2020 Predictive Maintenance Dataset**

Source: UCI Machine Learning Repository.

Dataset mein approximately **10,000 observations** hain.

Important columns:

| Column | Meaning |
|---|---|
| Type | Machine type |
| Air temperature | Surrounding air temperature |
| Process temperature | Process temperature |
| Rotational speed | Machine RPM |
| Torque | Applied torque |
| Tool wear | Tool usage/wear |
| Machine failure | Target |
| TWF | Tool Wear Failure |
| HDF | Heat Dissipation Failure |
| PWF | Power Failure |
| OSF | Overstrain Failure |
| RNF | Random Failure |

### Important

Hum **TWF, HDF, PWF, OSF, RNF** ko normal predictive features ki tarah directly use nahi karenge.

Reason:

Ye columns failure modes ko directly indicate karte hain. Agar target `Machine failure` hai, to in features ko use karne se **data leakage** ka risk hai.

---

# 2. Technical Requirements

Tumhe ye tools chahiye:

### Python

Main language.

### Libraries

- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn
- joblib

Later:

- Streamlit
- SHAP — optional advanced stage

### Environment

Kuch bhi use kar sakte ho:

- VS Code
- Jupyter Notebook
- Google Colab

Main recommend karunga:

**VS Code + Jupyter Notebook + GitHub**

---

# 3. Complete Project Roadmap

Hum project ko **10 phases** mein karenge.

```text
PHASE 1
Understand Dataset
       ↓
PHASE 2
Data Cleaning
       ↓
PHASE 3
EDA
       ↓
PHASE 4
Feature Engineering
       ↓
PHASE 5
Decision Tree Baseline
       ↓
PHASE 6
Overfitting + Gini/Entropy
       ↓
PHASE 7
Hyperparameter Tuning
       ↓
PHASE 8
Imbalance + Evaluation
       ↓
PHASE 9
Explainability + Risk Engine
       ↓
PHASE 10
Streamlit Deployment
```

Ab ek-ek phase exactly kya karna hai:

---

# PHASE 1 — Understand the Dataset

### Goal

Model banane se pehle data ko samajhna.

Sabse pehle identify karo:

### 1. Rows

Kitne observations hain?

### 2. Columns

Kitne features hain?

### 3. Target

Our target:

**Machine failure**

```text
0 → No failure
1 → Failure
```

### 4. Feature types

Identify:

```text
Numerical
Categorical
Identifier
Target
Potential leakage
```

### 5. Basic statistics

Har numerical feature ka:

- Mean
- Median
- Minimum
- Maximum
- Standard deviation

dekho.

### 6. Missing values

Check karo:

> Kya kisi column mein missing data hai?

### 7. Duplicates

Check karo:

> Kya same observation multiple times exist karti hai?

---

# PHASE 2 — Data Cleaning

Ab dataset ko model-ready banana hai.

### Step 1 — Remove identifier

`UDI` jaise identifier ka predictive meaning nahi hai.

Isko remove karo.

### Step 2 — Handle categorical variable

`Type` categorical hai.

Isko numerical representation mein convert karna padega.

### Step 3 — Leakage columns

Initially remove:

```text
TWF
HDF
PWF
OSF
RNF
```

Reason:

Ye failure mechanisms ko directly encode karte hain.

### Step 4 — Check data again

Cleaning ke baad verify:

- Missing values
- Duplicates
- Data types
- Remaining columns

---

# PHASE 3 — EDA

Ab actual investigation start hoti hai.

## Question 1

### How many machines fail?

Target distribution dekho.

Expected situation roughly:

```text
No Failure → ~96%
Failure    → ~3–4%
```

Yahi project ka ek important challenge hai.

---

## Question 2

### Does temperature affect failure?

Compare:

```text
Temperature
     ↓
Failure / No Failure
```

---

## Question 3

### Does torque affect failure?

Compare failed vs non-failed machines.

---

## Question 4

### Does tool wear affect failure?

Ye particularly interesting feature hai.

---

## Question 5

### Does rotational speed matter?

RPM aur failure ke relationship ko investigate karo.

---

## Question 6

### Machine Type ka effect?

Compare:

```text
Type L
Type M
Type H
```

against failure rate.

---

# PHASE 4 — Feature Engineering

Ab raw features se meaningful features create karenge.

But rule:

> **Random features nahi banane hain.**

Feature ka logical reason hona chahiye.

### Feature 1 — Temperature Difference

Concept:

```text
Process Temperature
        -
Air Temperature
```

Ye machine/process ke temperature increase ko represent kar sakta hai.

---

### Feature 2 — Mechanical Load / Power Proxy

Conceptually:

```text
Torque × Rotational Speed
```

Ye machine ke mechanical workload ka proxy provide kar sakta hai.

---

### Feature 3 — Tool Wear Categories

Tool wear ko investigate kar sakte ho:

```text
Low Wear
Medium Wear
High Wear
```

Lekin ye tabhi use karna jab analysis mein useful lage.

---

# PHASE 5 — Train/Test Split

Dataset ko divide karo:

```text
Dataset
   │
   ├── 80% Training
   │
   └── 20% Testing
```

### Important

Because failure rare hai:

**Stratified splitting** use karo.

Meaning:

Training aur testing dono mein approximately same failure ratio maintain ho.

---

# PHASE 6 — Decision Tree Baseline

Ab first actual model.

### Model:

**Decision Tree Classifier**

Initially:

> **No tuning.**

Default/basic Decision Tree train karo.

Why?

Because we need a **baseline**.

---

## Evaluate

Initially calculate:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix

But ek important point:

### Accuracy ko blindly trust mat karna.

Suppose:

```text
96% machines don't fail
4% machines fail
```

Agar model har machine ko:

> No Failure

bol de,

to accuracy approximately 96% aa sakti hai.

But model practically useless hoga.

---

# PHASE 7 — Decision Tree Investigation

Ab actual Decision Tree concepts test karenge.

## Experiment 1 — Tree Depth

Different depths try karo:

```text
max_depth = 2
max_depth = 3
max_depth = 5
max_depth = 7
max_depth = 10
Unlimited
```

Compare:

```text
Training Performance
vs
Testing Performance
```

### Expected behavior

```text
Too shallow
     ↓
Underfitting

Optimal depth
     ↓
Good generalization

Too deep
     ↓
Overfitting
```

Ye experiment tumhe practically samjhayega ki **Decision Tree overfit kaise karta hai**.

---

# PHASE 8 — Gini vs Entropy

Tumne Gini Index padha hai, so yaha proper experiment karenge.

## Model A

```text
Criterion = Gini
```

## Model B

```text
Criterion = Entropy
```

Then compare:

| Metric | Gini | Entropy |
|---|---:|---:|
| Accuracy | ? | ? |
| Precision | ? | ? |
| Recall | ? | ? |
| F1 | ? | ? |

### Important

Result pehle assume nahi karna.

Ho sakta hai Gini better ho.

Ho sakta hai Entropy better ho.

Ho sakta hai difference negligible ho.

**Experiment decide karega.**

---

# PHASE 9 — Class Imbalance

Ye project ka major challenge hai.

Failure cases bahut kam hain.

Isliye experiment karo:

### Approach 1

Normal Decision Tree.

### Approach 2

Class weighting.

Concept:

```text
Failure class
     ↓
Higher penalty
```

So model failure ko ignore na kare.

Then compare:

```text
Recall
Precision
F1
```

Particularly:

> **Failure class recall**

important hoga.

Because real-world scenario mein:

```text
Actual Failure
       ↓
Model says No Failure
       ↓
Machine breaks
       ↓
Expensive
```

---

# PHASE 10 — Hyperparameter Tuning

Ab optimized Decision Tree banayenge.

Main parameters:

### `max_depth`

Controls maximum tree depth.

### `min_samples_split`

Controls minimum observations required before a node can split.

### `min_samples_leaf`

Controls minimum observations in a leaf.

### `criterion`

```text
Gini
Entropy
```

### `class_weight`

Helps deal with class imbalance.

---

# PHASE 11 — Feature Importance

Final Decision Tree se identify karo:

> **Which machine parameters are driving predictions?**

For example, result could look like:

```text
Torque             ███████████
Tool Wear          █████████
Temperature        ██████
RPM                ████
Type               ██
```

**These are only examples.**

Actual importance model train hone ke baad determine hogi.

Then explain:

> Why does the model consider these variables important?

---

# PHASE 12 — Risk Engine

Ab project ko ordinary ML project se **decision system** banayenge.

Instead of only:

```text
Prediction = 1
```

system output karega:

```text
                 MACHINE STATUS

Risk Level: HIGH

Prediction: Potential Failure

Recommended Action:
Immediate inspection
```

Similarly:

```text
LOW RISK
↓
Continue operation
```

```text
MEDIUM RISK
↓
Schedule inspection
```

```text
HIGH RISK
↓
Immediate inspection
```

### Important

Risk thresholds arbitrary nahi hone chahiye.

Probability + business cost ko consider karke define karenge.

---

# PHASE 13 — Explainable Prediction

User machine parameters enter kare:

```text
Air Temperature       298 K
Process Temperature   308 K
Rotational Speed      1500 RPM
Torque                50 Nm
Tool Wear             180 min
Machine Type          M
```

System output:

```text
────────────────────────────

FAILURE RISK: HIGH

Prediction:
Potential Machine Failure

Main contributing factors:
• High tool wear
• High torque
• Temperature conditions

Recommended action:
Schedule immediate inspection
```

Later **SHAP** add karke explanation aur powerful bana sakte ho.

---

# PHASE 14 — Streamlit Application

Finally notebook ko application mein convert karenge.

### Page structure

```text
Predictive Maintenance System
──────────────────────────────

Machine Information

Machine Type       [ Select ]

Air Temperature    [      ]
Process Temp       [      ]
RPM                [      ]
Torque             [      ]
Tool Wear          [      ]

       [ PREDICT ]

──────────────────────────────

Prediction

Risk Level: HIGH

Failure Probability: XX%

Recommended Action:
Immediate Inspection

──────────────────────────────

Why?

1. Torque
2. Tool Wear
3. Temperature
```

---

# PHASE 15 — Final Model Comparison

Final README mein experiment table:

| Model | Accuracy | Precision | Recall | F1 |
|---|---:|---:|---:|---:|
| Baseline DT | | | | |
| Tuned DT | | | | |
| Gini DT | | | | |
| Entropy DT | | | | |
| Class-weighted DT | | | | |

Then final model select karo.

**Highest accuracy automatically winner nahi hoga.**

Failure detection ke context mein recall/F1 and business cost matter karenge.

---

# 16. Final GitHub Structure

```text
predictive-maintenance/
│
├── data/
│
├── notebooks/
│   ├── 01_data_understanding
│   ├── 02_data_cleaning
│   ├── 03_eda
│   ├── 04_feature_engineering
│   ├── 05_decision_tree
│   └── 06_hyperparameter_tuning
│
├── models/
│
├── src/
│
├── app/
│
├── requirements.txt
│
└── README.md
```

# What you will actually learn

Is project ke end tak tum sirf Decision Tree nahi, balki practically ye sab cover karoge:

**Data Cleaning → EDA → Feature Engineering → Class Imbalance → Gini → Entropy → Decision Tree → Best Split → Overfitting → Hyperparameters → Model Evaluation → Feature Importance → Explainability → Business Decision → Deployment**

### Our working rule

**Main tumhe code directly nahi dunga.**

Hum **step-by-step** chalenge.

Har phase mein:

1. **Concept**
2. **Why we are doing it**
3. **What you need to check**
4. **What result expect karna hai**
5. **Tum khud code likhoge**
6. Tum output bhejoge
7. Main us output ko analyze karke **next step** dunga.

**Start point: Phase 1 — Dataset Understanding.** Pehle hum dataset ke **har column ko properly understand + classify** karenge, including exactly **kaunse columns remove karne hain aur kyun**.