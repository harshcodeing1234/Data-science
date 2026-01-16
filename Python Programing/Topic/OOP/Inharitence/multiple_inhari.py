# Parent class
class Person:
    def __init__(self, name, pid):
        self.name = name
        self.__id = pid

    def show(self):
        print(f"The person is {self.name}")


# Child class (single inheritance)
class Student(Person):
    def __init__(self, name, pid, roll_no, department):
        super().__init__(name, pid)
        self.department = department
        self.roll_no = roll_no

    def about(self):
        print(f"The Student {self.name} from {self.department} department, Enrollment no. is {self.roll_no}")


# New class for company details (for real multiple inheritance)
class Company:
    def __init__(self, company, branch):
        self.company = company
        self.branch = branch

    def company_info(self):
        print(f"Company: {self.company}, Branch: {self.branch}")


# Child class (multiple inheritance)
class Employee(Student, Company):
    def __init__(self, name, pid, roll_no, department, company, branch, emp_id):
        Student.__init__(self, name, pid, roll_no, department)
        Company.__init__(self, company, branch)
        self.__emp_id = emp_id
    
    def employee_details(self):
        print(f"Employee {self.name} works in {self.company}, branch {self.branch}, department {self.department}")


# ------------------ Testing ------------------

# Person instance
p1 = Person("Raghav", "234")
p1.show()

# Student instance 
s1 = Student("Raghav", "234", "A45349524003", "AIIT")
s1.show()
s1.about()

# Employee instance (multiple inheritance)
e1 = Employee("Tapshi", "234", "ST12345", "IT", "Wipro", "Bengaluru", "EMP001")
e1.show()
e1.about()
e1.company_info()
e1.employee_details()
print("")
print(Employee.mro())  # Show MRO
