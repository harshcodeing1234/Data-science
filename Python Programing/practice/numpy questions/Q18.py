# WAP to Slice a 3D Array
import numpy as np # type: ignore
arr3 = np.arange(1, 25).reshape(2, 3, 4)
print(arr3)
print("\n.")

print(arr3[0, :, :])   
print(arr3[:, 1, :])   
print(arr3[:, :, 2])   


