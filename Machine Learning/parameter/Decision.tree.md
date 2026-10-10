**Decision Tree — Important Parameters**

| Parameter | Meaning | Example |
|---|---|---|
| `criterion` | Measures split quality | `criterion="gini"` |
| `max_depth` | Maximum tree depth | `max_depth=5` |
| `min_samples_split` | Minimum samples needed to split | `min_samples_split=2` |
| `min_samples_leaf` | Minimum samples in a leaf | `min_samples_leaf=1` |
| `max_features` | Features considered for each split | `max_features="sqrt"` |

**Most important:** `criterion`, `max_depth`, `min_samples_split`, `min_samples_leaf`

```python
from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier(
    criterion="gini",
    max_depth=5
)
```