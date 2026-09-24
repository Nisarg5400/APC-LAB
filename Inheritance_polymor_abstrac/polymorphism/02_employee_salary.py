# 2. Employee base class, calculate_salary() overridden

class Employee:
    def calculate_salary(self):
        pass


class Manager(Employee):
    def calculate_salary(self):
        return 60000


class Developer(Employee):
    def calculate_salary(self):
        return 50000


class Tester(Employee):
    def calculate_salary(self):
        return 40000


employees = [Manager(), Developer(), Tester()]
for e in employees:
    print(f"{e.__class__.__name__} Salary: {e.calculate_salary()}")
