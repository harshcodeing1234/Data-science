# vstack Meaning: Vertical stack = row-wise join (axis=0).

import numpy as np #type: ignore

# 1D
a = np.array([1,2,3])
b = np.array([4,5,6])
print(np.vstack([a,b]))


# 2D
A = np.array([[1,2,3]])
B = np.array([[4,5,6]])
print(np.vstack([A,B]))

# 3D
X = np.arange(1,7).reshape(1,2,3)
Y = np.arange(7,13).reshape(1,2,3)
print(np.vstack([X,Y]))
