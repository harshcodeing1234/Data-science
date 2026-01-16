# 
class Empolyee:
    def __init__(self,name,age,salary,):
        self.name = name
        self.age = age
        self.__salary = salary
    def details(self):
        print(f"name = {self.name}")
        print(f"age = {self.age}")
        print(f"salery = {self.__salary}") # Can access only in class
    
E1 = Empolyee("Surya kumar",23,"89,000") 
E1.details()
# print(E1.__salary) # cannot be access # it throw error
print(f"salary = {E1._Empolyee__salary}") # but can accacess using class name(_Empolyee)
