# parameter constructor:
class Person:
    def __init__(self, name, age, occupation):
        self.name = name
        self.age = age
        self.occupation = occupation

    def info(self):
        print(f"Name: {self.name},\nAge: {self.age},\nOccupation: {self.occupation}")

a = Person("shubham", 25, "Engineer")
b = Person("Divya", 30, "Doctor")
a.info()
b.info()