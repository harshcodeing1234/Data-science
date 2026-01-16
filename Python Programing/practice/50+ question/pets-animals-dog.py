# Create a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ from ‘Pets’. Add a method ‘bark’ to class ‘Dog’.

class Animals:
    def __init__(self,name):
        self.name = name

    def sound(self):
        return f"{self.name} make a sound"
    
class pets(Animals):
    def __init__(self, name,owner):
        super().__init__(name) 
        self.owner = owner

    def info(self):
        return f"{self.name} is a pet owned by {self.owner}" 

class dog(pets):
    def __init__(self, name, owner,breed):
        super().__init__(name, owner)
        self.breed = breed
    def bark(self):
        return f"{self.name} Says: Woof! Woof!"  

dog1 = dog("lily","prashant","Golden Retriever")  

print(dog1.sound())
print(dog1.info())
print(dog1.bark())