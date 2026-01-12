import numpy as np # type: ignore

# hsplit:Horizontal split (splits along columns).

# 1D array
b1 = np.array([1,2,3,4])
print(np.hsplit(b1, 2))  # Split 1D array horizontally (like split)

# 2D array
b2 = np.array([[1,2,3,4],
               [5,6,7,8]])
print(np.hsplit(b2, 2))  # Split into 2 column-wise arrays

# 3D array
b3 = np.arange(16).reshape(2,2,4)
print(np.hsplit(b3, 2))  # Horizontal split along last axis