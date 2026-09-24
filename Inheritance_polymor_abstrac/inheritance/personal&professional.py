class PersonalDetails:
    def __init__(self, name, age) :
        self.name = name
        self.age = age 

class ProfessionalDetails:
    def __init__(self, Id, Position, Salary ):
        self.Id = Id
        self.Position = Position 
        self.Salary = Salary 

class Employee(PersonalDetails, ProfessionalDetails):
    def __init__(self, name, age, Id, Position, Salary):
        PersonalDetails.__init__(self, name, age)
        ProfessionalDetails.__init__(self, Id, Position, Salary)

    def display(self):
         print(f"Name  :{self.name}, Age : {self.age}")
         print(f"Emp ID :{self.Id}, Designation :{self.Position}, Salary :{self.Salary}")

e1 = Employee("Nisarg", 21, 70, "Software Engineer", 60000)
e1.display() 