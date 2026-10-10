**This works:** Short README format:

| Parameter | Meaning | Example |
|---|---|---|
| `C` | Controls penalty for wrong predictions | `SVC(C=10)` |
| `kernel` | Type of decision boundary | `SVC(kernel="rbf")` |
| `gamma` | Influence of each data point | `SVC(gamma=0.1)` |
| `degree` | Polynomial complexity | `SVC(kernel="poly", degree=3)` |
| `class_weight` | Handles imbalanced classes | `SVC(class_weight="balanced")` |

**Most important:** `C`, `kernel`, `gamma`