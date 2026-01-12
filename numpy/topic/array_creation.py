import numpy as np

# Range arrays
arr_range = np.arange(1, 10, 2)
print(f"Range array: {arr_range}")

# Linear space
arr_linspace = np.linspace(0, 1, 10)
print(f"Linear space: {arr_linspace}")

# Logarithmic space
arr_logspace = np.logspace(1, 3, 4)
print(f"Log space: {arr_logspace}")

# Zeros
arr_zeros = np.zeros((2, 3))
print(f"Zeros array: {arr_zeros}")

# Ones
arr_ones = np.ones((4, 2), dtype=int)
print(f"Ones array: {arr_ones}")

# Full array
arr_full = np.full((4, 5), 6.5)
print(f"Full array: {arr_full}")

# Empty array
arr_empty = np.empty((2, 4))
print(f"Empty array: {arr_empty}")
