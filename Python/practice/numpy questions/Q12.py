# Reverse a numpy array.
import numpy as np # type: ignore

arr = np.arange(9).reshape(3,3)

print(f"array:\n{arr}")

reverse = arr[::-1]
print(f"Reverse array: {reverse}")
