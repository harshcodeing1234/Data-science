# Swapaxes: Meaning: Swap two axes of the array.

import numpy as np # type: ignore

# 1D
a = np.array([1,2,3])

# 2D
A = np.array([[1,2,3],
              [4,5,6]])
print(np.swapaxes(A, 0, 1))   

# 3D
X = np.arange(1, 13).reshape(2,2,3)
print(np.swapaxes(X, 0, 1))   