# 
class Person(object):
  
  def __init__(self, name, id):
    self.name = name
    self.id = id


  def Display(self):
    print(self.name, self.id)



emp = Person("Elon", 102) 
emp.Display()

# Child Class
class Emp(Person):
  
  def Print(self):
    print("Emp class called")
    
Emp_details = Emp("Mayank", 103)

# calling parent class function
Emp_details.Display()

# Calling child class function 
Emp_details.Print()
