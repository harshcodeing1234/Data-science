# Check whether a Numpy array contains a specified row
import numpy as np

arr = np.arange(6).reshape(2,3)
print(arr)

if arr.tolist():
    print("array contains a specific rows")
    
