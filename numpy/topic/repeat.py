import numpy as np # type: ignore

# repeat: Repeats elements of an array.

# 1D
c1 = np.array([1,2,3])
print(np.repeat(c1, 2))  # Repeat each element 2 times

# 2D
c2 = np.array([[1,2],[3,4]])
print(np.repeat(c2, 2, axis=0))  # Repeat rows
print(np.repeat(c2, 2, axis=1))  # Repeat columns

# 3D
c3 = np.arange(8).reshape(2,2,2)
print(np.repeat(c3, 2, axis=1))  # Repeat along axis=1