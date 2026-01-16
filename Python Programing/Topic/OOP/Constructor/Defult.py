# Default constructor:
class Person:
    def __init__(self):
        self.name = "Harsh"
        self.age = 20
        self.occupation = "Student"

    def info(self):
        print(f"Name: {self.name},\nAge: {self.age},\nOccupation: {self.occupation}")

a = Person()
a.info() 