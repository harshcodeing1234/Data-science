# Write a class “Calculator” capable of finding square(a² = a × a), cube(V = a³) and square root(√a = a^(1/2)) of a number.
class calculator:
    def __init__(self,a):
        self.a = a
        
    def add(self,b):
        return f"Sum = {self.a+b}"
    def sub(self,b):
        return f"Subtract: {self.a-b}"
    def mul(self,b):
        return f"Multiply: {self.a*b}"
    def div(self,b):
        if b != 0:
            return f"division: {self.a/b}"
        else:
            print("Num is cannot divided by 0")
    def module(self,b):
        return f"module: {self.a%b}"
    def square(self):
        return f"square: {self.a*self.a}"
    def volume(self):
        return f"volume: {self.a*self.a*self.a}"
    def square_root(self):
        if self.a >= 0:
            return f"Square root: {self.a ** 0.5}"  
        else:
            return "Error: Square root of negative number cannot real"


c1 = calculator(12)
print(c1.add(34))
print(c1.square_root())

    

