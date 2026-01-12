import numpy as np

# Default data type
arr = np.array([1, 2, 3, "4"])
print(f"Array: {arr}")
print(f"Data type: {arr.dtype}")

# Specify data type
arr_float = np.array([1, 2, 3, 4], dtype=np.float32)
print(f"Float array: {arr_float}")
print(f"Data type: {arr_float.dtype}")
