class Person:
    name = "Harsh"
    age = 20
    occupation = "Student"

    def info(self):
        print(f"Name: {self.name},\nAge: {self.age},\nOccupation: {self.occupation}")

a = Person()
a.name = "shubham"
a.info()
b = Person()
b.name = "Rinku"
b.age = 35
b.info()