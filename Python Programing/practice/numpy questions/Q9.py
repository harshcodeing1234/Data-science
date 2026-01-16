# Flatten a 2d array into 1d array
import numpy as np # type: ignore

arr = np.arange(25).reshape(5,5)
print(f"array:\n{arr}")

print(f"flatten array: {arr.flatten()}")
