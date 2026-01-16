# 1. Create a class (2-D vector) and use it to create another class representing a 3-D vector.
import math
class vector2D:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def magnitute(self):
        return math.sqrt(self.x**2+self.y**2)
    def add(self,other):
        return vector2D(self.x + other.x , self.y + other.y)
    def sub(self,other):
        return vector2D(self.x - other.x , self.y - other.y)
    def product(self,other):
        return vector2D(self.x*other.x , self.y * other.y)
    def __str__(self):
        return f"vector2D {self.x}, {self.y}"
    
v1 = vector2D(5,1)
v2 = vector2D(7,9)

print(v1)
print(f"magnitute {v1.magnitute()}")

v3 = v1.add(v2)

print(f"sum : {v3}")

print(f"product : {v1.product(v2)}")

class vector3D(vector2D):
    def __init__(self, x, y,z):
        super().__init__(x, y)
        self.z = z
    def magnitute(self):
        return math.sqrt(self.x**2+self.y**2 + self.z**2)
    def add(self,other):
        return vector3D(self.x + other.x , self.y + other.y , self.z + other.z)
    def sub(self,other):
        return vector3D(self.x - other.x , self.y - other.y , self.z - other.z)
    def product(self,other):
        return (self.x*other.x + self.y * other.y + self.z * other.z)
    def cross_product(self, other):
        cx = self.y * other.z - self.z * other.y
        cy = self.z * other.x - self.x * other.z
        cz = self.x * other.y - self.y * other.x
        return vector3D(cx, cy, cz)
    
    def __str__(self):
        return f"vector2D {self.x}, {self.y}, {self.z}"

v1 = vector3D(1, 2, 3)
v2 = vector3D(4, 5, 6)

print(v1)                       
print("Magnitude:", v1.magnitute())  
print("Sum:", v1.add(v2))       
print("Dot Product:", v1.product(v2)) 
print("Cross Product:", v1.cross_product(v2))  
