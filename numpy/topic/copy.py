# copy()
import numpy as np # type: ignore

# 1D
a = np.array([ 1 ,99 , 3 , 4  ,5 ])
c = a.copy()   # makes a deep copy
c[0] = 111

print("Original:", a)  
print("Copy:", c)      

# 2D

a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

b = a[0:2, 1:3].copy()
b[0, 0] = 111 

print("Original:\n", a)
print("Copy:\n", b)

# 3D
x = np.arange(1, 25).reshape(2, 3, 4)
print("Original 3D array:\n", x)

# Copy
z = x[:, 1:, :2].copy()
z[0, 0, 0] = 555

print("\nAfter modifying copy:")
print("Original:\n", x)
print("Copy:\n", z)
