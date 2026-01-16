# Write a class ‘Complex’ to represent complex numbers, along with overloaded operators ‘+’ and ‘*’ which adds and multiplies them.

class complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img
    
    def __add__(self,other):
        return complex(self.real + other.real , self.img + other.img)
    
    def __mul__(self,other):
        real = self.real * other.real - self.img * other.img
        img =  self.real * other.real + self.img * other.img
        return complex(real , img)
    
    def __str__(self):
        return f"{self.real} + {self.img}i"

c1 = complex(12,34)
c2 = complex(9,6)
print(c1)

print(f"sum = {c1+c2}")
print(f"product = {c1*c2}")
