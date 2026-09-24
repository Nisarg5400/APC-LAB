class PersonalDetails:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class ProfessionalDetails:
    def __init__(self, emp_id, designation, salary):
        self.emp_id = emp_id
        self.designation = designation
        self.salary = salary


class Employee(PersonalDetails, ProfessionalDetails):
    def __init__(self, name, age, emp_id, designation, salary):
        PersonalDetails.__init__(self, name, age)
        ProfessionalDetails.__init__(self, emp_id, designation, salary)

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")
        print(f"Emp ID: {self.emp_id}, Designation: {self.designation}, Salary: {self.salary}")


e1 = Employee("Priya", 28, 101, "Software Engineer", 60000)
e1.display()
