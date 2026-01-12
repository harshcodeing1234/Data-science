import numpy as np

# Random floats between 0 and 1
arr_1d = np.random.rand(10)
print(f"1-D random floats: {arr_1d}")

# 2-D random floats
arr_2d = np.random.rand(2, 5)
print(f"2-D random floats: {arr_2d}")

# Random integers
arr_int = np.random.randint(5, 100, size=(2, 3))
print(f"Random integers: {arr_int}")
