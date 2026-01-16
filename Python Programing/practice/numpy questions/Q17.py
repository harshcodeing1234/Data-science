# WAP to Accessing Element in a 3D Array
import numpy as np # type: ignore

arr = np.array([[[11, 2], [3, 4]], [[5, 6], [7, 8]]])

ind = arr[1,0,1]
print(ind)