# 1. Transpose: Meaning: Rearranges axes of an array. For 2D it flips rows ↔ columns. For higher dimensions, you can specify axis order.

import numpy as np # type: ignore

# 1D
a = np.array([1, 2, 3])
print(f" transpose {a.T}")

# 2D
A = np.array([[1, 2, 3],
              [4, 5, 6]])
print(f" transpose {A.T}")


# 3D
X = np.arange(1, 13).reshape(2,2,3)
t= X.transpose(0,2,1) 
print(f" transpose {t.T}")