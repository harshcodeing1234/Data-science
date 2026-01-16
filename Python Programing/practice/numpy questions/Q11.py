# 
import numpy as np # type: ignore

arr = np.array([1,2,6,0,0,5,0])

ar = np.count_nonzero(arr)
print(f"Non zero values: {ar}")
