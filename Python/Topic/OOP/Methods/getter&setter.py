# 
class Student:
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    def get_age(self):
        return self._age
    
    def set_age(self, value):
        self._age = value

s = Student("Harsh", 20)
print(s.get_age())  # Get age
s.set_age(23)       # Try to set invalid age
print(s.get_age())

