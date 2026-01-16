# WAP to Swapping Axes in a 2D Array.
import numpy as np # type: ignore
arr = np.array([[1, 2, 3], [4, 5, 6]])

result = np.swapaxes(arr, axis1=0, axis2=1)

print("Original array:\n", arr)
print("Array after swapping axes:\n", result)


