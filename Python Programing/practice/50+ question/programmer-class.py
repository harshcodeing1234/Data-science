# Create a class “Programmer” for storing information of few programmers working at Microsoft.

class Programer:
    def __init__(self,name,age,id,company,department,salery,skills,Exprience_year,):
        self.name = name
        self.age = age
        self.id = id
        self.company = company
        self.deppartment = department
        self.__salery = salery
        self.skills = skills
        self.Expprience_year = Exprience_year

    def showDetails(self):
        return f"Programer details:\nName: {self.name}\nAge: {self.age}\nId: {self.id}\nWorking in: {self.company}\nDepartment: {self.deppartment}\nSalery: Hidden\nskills: {self.skills}\nYear of Exprience: {self.Expprience_year} Years of Exprience"

p1 = Programer("Harshita",22,3456,"Microsoft","Security","1,20,000",['Python','Web devlopment','Data science','Java','Data Structure','Microsoft 365'],4)

print(p1.showDetails())