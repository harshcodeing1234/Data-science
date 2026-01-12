import numpy as np
def array(i,j):
    return i+j

ar1 = np.fromfunction(array,(2,3))
print(f"array {ar1}")

ar2 = np.fromfunction(array,(3,6))
print(f"array {ar2}")

