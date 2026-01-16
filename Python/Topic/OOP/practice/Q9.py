#  Create a class ‘Employee’ and add salary and increment properties to it.

class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        self.increment = 0

    def set_increment(self,percentage):
        self.increment = percentage
        
    
    def apply_increment(self):
        self.salary += self.salary * (self.increment/100)
    
    def get_salary(self):
        return self.salary
    def __str__(self):
        return f"Employee: {self.name}, Salary: {self.salary}, Increment: {self.increment}%"
    
E1 = Employee("Saksham",34000)
E1.set_increment(10)
E1.apply_increment()
print(f"Salary: {E1.get_salary()}")

print(E1)

        