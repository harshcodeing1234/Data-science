import numpy as np

# Reshape
arr = np.arange(6)
reshaped = arr.reshape(2, 3)
print(f"Original: {arr}")
print(f"Reshaped: {reshaped}")

# Ravel (returns view)
arr_2d = np.array([[1, 3], [4, 5]])
raveled = arr_2d.ravel()
print(f"2-D array: {arr_2d}")
print(f"Raveled: {raveled}")

# Flatten (returns copy)
arr_flat = np.array([[1, 2, 3], [4, 5, 6]])
flattened = arr_flat.flatten()
print(f"Original: {arr_flat}")
print(f"Flattened: {flattened}")
