import numpy as np # type: ignore
# 1D
a = np.array([1, 2, 3, 4, 5])
b = a[1:4]   # slicing creates a view
b[0] = 99

print("Original:", a)   
print("View:", b)   

# 2D
arr = np.arange(18).reshape(3,6)
view = arr[0:2,2:5]
view[0,2] = 89
print("Original:", arr)   
print("View:", view)

# 3D
x = np.arange(1, 25).reshape(2, 3, 4)
print("Original 3D array:\n", x)

# View (slicing 3D)
y = x[:, 1:, :2]   # all depth, rows 1→end, cols 0–1 
y[0, 0, 0] = 999

print("\nAfter modifying view:")
print("Original:\n", x)
print("View:\n", y)
