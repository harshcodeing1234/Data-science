# 
class student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def showdetails(self):
        print(f"name = {self.name}")
        print(f"age = {self.age}")

s1 = student("Harsh",19)
s1.showdetails()

        