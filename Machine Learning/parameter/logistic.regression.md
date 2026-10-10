**Logistic Regression — Important Parameters**

| Parameter | Meaning | Example |
|---|---|---|
| `C` | Controls regularization strength | `LogisticRegression(C=10)` |
| `penalty` | Type of regularization | `LogisticRegression(penalty="l2")` |
| `solver` | Algorithm used for optimization | `LogisticRegression(solver="liblinear")` |
| `max_iter` | Maximum training iterations | `LogisticRegression(max_iter=1000)` |
| `class_weight` | Handles imbalanced classes | `LogisticRegression(class_weight="balanced")` |

**Main attributes:**

| Attribute | Meaning |
|---|---|
| `coef_` | Feature coefficients |
| `intercept_` | Intercept |
| `predict_proba()` | Prediction probabilities |
| `predict()` | Final class prediction |