import numpy as np

# 0-D Array (Scalar)
arr_0d = np.array(56)
print(f"0-D array: {arr_0d}, dimensions: {arr_0d.ndim}")

# 1-D Array
arr_1d = np.array([2, 3, 8, 6])
print(f"1-D array: {arr_1d}, dimensions: {arr_1d.ndim}")

# 2-D Array
arr_2d = np.array([[2, 4, 3], [6, 5, 8]])
print(f"2-D array: {arr_2d}, dimensions: {arr_2d.ndim}")

# 3-D Array
arr_3d = np.array([[[2, 4, 7], [34, 67, 89], [67, 23, 56]]])
print(f"3-D array: {arr_3d}, dimensions: {arr_3d.ndim}")

# Higher Dimensional Array
arr_5d = np.array([1, 2, 3, 4], ndmin=5)
print(f"5-D array: {arr_5d}, dimensions: {arr_5d.ndim}")
