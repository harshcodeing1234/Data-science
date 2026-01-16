# Mean of a Numpy Array
import numpy as np # type: ignore

arr = np.arange(6).reshape(2,3)
print(f"array:\n{arr}")
print(f"mean of element:{np.mean(arr)}")

# Standard deviation
print("Standard deviation:", np.std(arr))