import numpy as np # type: ignore

# tile: Repeats the whole array along specified axes.

# 1D
d1 = np.array([1,2,3])
print(np.tile(d1, 2))  # Repeat the whole array twice

# 2D
d2 = np.array([[1,2],[3,4]])
print(np.tile(d2, (2,3)))  # Repeat 2 times row-wise, 3 times column-wise

# 3D
d3 = np.arange(4).reshape(1,2,2)
print(np.tile(d3, (2,2,1)))  # Repeat along each axis