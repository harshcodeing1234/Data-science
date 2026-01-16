# Create a 1D array [1,2,3,4,5,6,7,8,9,10]. Slice it from index 3 to 7. Change one element in the slice. Does the original array change?

import numpy as np #type: ignore

num = [1,2,3,4,5,6,7,8,9,10]

arr = np.array(num)

view = arr[3:7]
# arr.view()

view[0] = 12
print(view)
print(f"array:\n{arr}")

# Take the slice from Q1 and make a .copy(). Change an element. Does the original array change?

c = view.copy()
view[0] = 23
print(view)
print(c)


