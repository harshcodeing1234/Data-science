import numpy as np

x = np.linspace(0,9,3)
y = np.linspace(0,6,2)

x,y = np.meshgrid(x,y)

print("X coordinates:")
print(x)
print("Y coordinates:")
print(y)
