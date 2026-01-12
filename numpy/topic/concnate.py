# Concatenate: Meaning: Joins arrays along an existing axis.
import numpy as np #type: ignore
# 1D
a = np.array([1,2,3])
b = np.array([4,5,6])
print(np.concatenate([a,b]))
# [1 2 3 4 5 6]

# 2D
A = np.array([[1,2,3],[4,5,6]])
B = np.array([[7,8,9],[10,11,12]])
print(np.concatenate([A,B], axis=0))  # row wise
print(np.concatenate([A,B], axis=1))  # column wise

# 3D
X = np.arange(1,13).reshape(2,2,3)
Y = np.arange(13,25).reshape(2,2,3)
print(np.concatenate([X,Y], axis=0))  # depth
print(np.concatenate([X,Y], axis=1))  # row
print(np.concatenate([X,Y], axis=2))  # col