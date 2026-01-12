import numpy as np #type: ignore

# stack Meaning: Joins arrays by adding a new axis.

# 1D
a = np.array([1,2,3])
b = np.array([4,5,6])
print(np.stack([a,b], axis=0))  # shape (2,3)
print(np.stack([a,b], axis=1))  # shape (3,2)

# 2D
A = np.array([[1,2,3],[4,5,6]])
B = np.array([[7,8,9],[10,11,12]])
print(np.stack([A,B], axis=0))  # depth
print(np.stack([A,B], axis=1))  # row axis

# 3D
X = np.arange(1,13).reshape(2,2,3)
Y = np.arange(13,25).reshape(2,2,3)
print(np.stack([X,Y], axis=0))  # shape (2,2,2,3)
print(np.stack([X,Y], axis=1))  # shape (2,2,2,3) but axes swapped