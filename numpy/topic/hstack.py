import numpy as np #type: ignore

# hstack Meaning: Horizontal stack = column-wise join (axis=1 for 2D).

# 1D
a = np.array([1,2,3])
b = np.array([4,5,6])
print(np.hstack([a,b]))
# [1 2 3 4 5 6]

# 2D
A = np.array([[1,2,3]])
B = np.array([[4,5,6]])
print(np.hstack([A,B]))
# [[1 2 3 4 5 6]]

# 3D
X = np.arange(1,7).reshape(1,2,3)
Y = np.arange(7,13).reshape(1,2,3)
print(np.hstack([X,Y]))   
