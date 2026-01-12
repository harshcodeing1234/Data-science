# split: Splits an array into multiple sub-arrays. Works for 1D, 2D (by rows), etc.

import numpy as np #type: ignore

# 1D array
a1 = np.array([1, 2, 3, 4, 5, 6])
print(np.split(a1, 3))  # Split into 3 equal parts

# 2D array
a2 = np.array([[1, 2, 3, 4],
               [5, 6, 7, 8]])
print(np.split(a2, 2, axis=1))  # Split columns into 2 parts

# 3D array
a3 = np.arange(24).reshape(2,3,4)
print(np.split(a3, 2, axis=2))  # Split along last axis
