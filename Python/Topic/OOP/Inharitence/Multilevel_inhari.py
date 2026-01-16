# 
# Base class
class Person:
    def __init__(self, name, pid):
        self.name = name
        self.__pid = pid  # private attribute

    def show_person(self):
        print(f"Person: {self.name}, ID: {self.__pid}")


# Intermediate class (inherits from Person)
class Student(Person):
    def __init__(self, name, pid, roll_no, department):
        super().__init__(name, pid)
        self.roll_no = roll_no
        self.department = department

    def show_student(self):
        print(f"Student: {self.name}, Roll No: {self.roll_no}, Department: {self.department}")


# Derived class (inherits from Student)
class Graduate(Student):
    def __init__(self, name, pid, roll_no, department, degree, year):
        super().__init__(name, pid, roll_no, department)
        self.degree = degree
        self.year = year

    def show_graduate(self):
        print(f"Graduate: {self.name}, Degree: {self.degree}, Year: {self.year}")


# ----------------- Testing -----------------
g1 = Graduate("Raghav", "234", "A45349524003", "AIIT", "B.Tech", 2025)

g1.show_person()   # From Person
g1.show_student()  # From Student
g1.show_graduate() # From Graduate
