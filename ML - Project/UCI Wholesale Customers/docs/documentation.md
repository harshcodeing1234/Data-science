# K-Means Clustering — Wholesale Customers Dataset

## Dataset

**Name:** Wholesale Customers  
**Source:** UCI Machine Learning Repository  
**Dataset ID:** 292  
**DOI:** 10.24432/C5030X  
**Instances:** 440 customers  
**Features:** 8 columns  
**Task:** Clustering / Classification  
**Domain:** Business

Source: UCI Machine Learning Repository.

## Purpose

The dataset contains customer information from a wholesale distributor, including annual spending on different product categories.

For this K-Means project, the main goal is:

> **Group customers with similar purchasing/spending behavior into clusters.**

This is an **unsupervised learning** problem because the clusters are not provided as the answer. K-Means discovers the groups from the customer spending patterns.

## Columns

| Column | Type | Meaning |
|---|---|---|
| `Channel` | Categorical | Customer channel: Horeca or Retail |
| `Region` | Categorical | Customer region: Lisbon, Oporto, or Other |
| `Fresh` | Numerical | Annual spending on fresh products |
| `Milk` | Numerical | Annual spending on milk products |
| `Grocery` | Numerical | Annual spending on grocery products |
| `Frozen` | Numerical | Annual spending on frozen products |
| `Detergents_Paper` | Numerical | Annual spending on detergents and paper |
| `Delicassen` | Numerical | Annual spending on delicatessen products |

## Main Features for Clustering

For customer segmentation, the six spending features are the main candidates:

```text
Fresh
Milk
Grocery
Frozen
Detergents_Paper
Delicassen
```

`Channel` and `Region` are categorical variables. They can be kept for later cluster interpretation rather than directly used as ordinary numerical inputs to K-Means.

## Business Problem

A wholesale distributor has many customers with different purchasing patterns.

The company wants to answer:

- Which customers have similar purchasing behavior?
- Which product categories are important for each customer group?
- Can customers be divided into meaningful segments?
- Can different strategies be used for different customer segments?

## Expected Clusters

The actual clusters are **not known beforehand**.

After applying K-Means, we may discover groups such as:

```text
Cluster 1 → Customers with high Fresh spending
Cluster 2 → Customers with high Grocery/Milk spending
Cluster 3 → Customers with high Detergents_Paper spending
...
```

These names are only examples. The final cluster meaning must be determined by analyzing the actual cluster statistics.

## Practical Workflow

```text
Load Dataset
      ↓
Understand Dataset
      ↓
Check Missing Values & Duplicates
      ↓
Explore Distributions & Outliers
      ↓
Select Spending Features
      ↓
Scale Features
      ↓
Find Optimal K using Elbow Method
      ↓
Train K-Means
      ↓
Assign Cluster Labels
      ↓
Evaluate using Inertia / Silhouette Score
      ↓
Analyze Cluster Profiles
      ↓
Visualize & Interpret Clusters
```

## Important Preprocessing

### 1. Missing Values

The UCI documentation reports **no missing values** in this dataset.

### 2. Outliers

Spending variables have very different ranges and can contain large values.

Check their distributions and outliers before clustering.

### 3. Feature Scaling

K-Means is distance-based, so scaling is important.

Example:

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```

### 4. Feature Selection

For the main customer-segmentation experiment:

```python
features = [
    "Fresh",
    "Milk",
    "Grocery",
    "Frozen",
    "Detergents_Paper",
    "Delicassen"
]

X = df[features]
```

## Choosing K

Use the **Elbow Method**.

```text
K = 1 → Calculate Inertia
K = 2 → Calculate Inertia
K = 3 → Calculate Inertia
...
K = 10 → Calculate Inertia
          ↓
      Plot K vs Inertia
          ↓
      Find Elbow Point
          ↓
        Select K
```

Inertia:

\[
Inertia = \sum (distance\ to\ centroid)^2
\]

The elbow is the point after which increasing K gives a much smaller improvement.

## Model

```python
from sklearn.cluster import KMeans

kmeans = KMeans(
    n_clusters=K,
    random_state=42,
    n_init=10
)

clusters = kmeans.fit_predict(X_scaled)
```

Add the result:

```python
df["Cluster"] = clusters
```

## Evaluation

### Inertia

Lower inertia means points are closer to their cluster centroids, but inertia always tends to decrease as K increases. Therefore, use the **Elbow Method** rather than simply choosing the lowest value.

### Silhouette Score

Use it as an additional validation method:

```python
from sklearn.metrics import silhouette_score

score = silhouette_score(X_scaled, clusters)
print(score)
```

A higher silhouette score generally indicates better-separated and more cohesive clusters.

## Cluster Interpretation

After training, calculate the average spending of each cluster:

```python
cluster_profile = df.groupby("Cluster")[features].mean()
```

This tells us what makes each customer group different.

Example interpretation format:

```text
Cluster 0 → High Grocery + Milk spending
Cluster 1 → High Fresh + Frozen spending
Cluster 2 → High Detergents_Paper spending
```

Do **not** assign these names before analyzing the actual results.

## Final Objective

The final goal is not just to create clusters.

The goal is to:

> **Discover meaningful customer segments from purchasing behavior and explain what makes each segment different.**

## Dataset Source

UCI Machine Learning Repository — Wholesale Customers

https://archive.ics.uci.edu/dataset/292/wholesale+customers

Citation:

Cardoso, M. (2013). *Wholesale customers*. UCI Machine Learning Repository. DOI: 10.24432/C5030X
