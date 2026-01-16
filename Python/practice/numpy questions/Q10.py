# Move axes of an array to new positions
import numpy as np # type: ignore

arr = np.arange((9)).reshape(3,3)
print(f"array:\n{arr}")
print()

# move axis
moved_arr = np.moveaxis(arr, 0, 1)
print(f"move axis:\n{moved_arr}")


