import numpy as np

# Type casting
arr = np.array([1, 2, 3, 4])
print(f"Original dtype: {arr.dtype}")

new_arr = arr.astype(np.float64)
print(f"Converted array: {new_arr}")
print(f"New dtype: {new_arr.dtype}")

# Note: Mixed string/numeric arrays cannot be converted to numeric types
# arr_mixed = np.array(["1", 2, 3, "text"])  # This would cause errors in conversion
