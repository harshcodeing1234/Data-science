# 
import numpy as np

arr3 = np.arange(1, 25).reshape(2, 3, 4)
print(arr3)
print("end")
# Shape: (2 blocks, 3 rows, 4 columns)
print(arr3[0, :, :])   # First block (all rows, all cols)
print(arr3[:, 1, :])   # Second row from each block
print(arr3[:, :, 2])   # Third column from all rows & blocks
print("end")



# np.take()
arr = np.array([10, 20, 30, 40, 50])

print(np.take(arr, [0, 2, 4]))  
print("end")
# [10 30 50]

arr2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(np.take(arr2, [0,4,8])) 
print("end") 


# Specify axis
print(np.take(arr2, [0,2], axis=1)) 
print("end") 

# enumrate
for ind, x in np.ndenumerate(arr):
    print(ind , x)




