import numpy as np

# 1-D array indexing
arr_1d = np.array([1, 2, 3, 4])
print(f"First element: {arr_1d[0]}")
print(f"Sum of 2nd and 3rd: {arr_1d[1] + arr_1d[2]}")

# 2-D array indexing
arr_2d = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(f"2nd element on 1st row: {arr_2d[0, 1]}")
print(f"2nd element of 2nd row: {arr_2d[1, 1]}")

# 3-D array indexing
arr_3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(f"3-D element: {arr_3d[0, 1, 2]}")

# Negative indexing
print(f"Last element from 2nd row: {arr_2d[1, -1]}")
