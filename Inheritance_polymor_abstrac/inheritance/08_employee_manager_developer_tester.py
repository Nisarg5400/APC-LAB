# 8. Hierarchical inheritance - Employee -> Manager, Developer, Tester

class Employee:
    def __init__(self, emp_id, name, basic_salary):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary


class Manager(Employee):
    def calculate_salary(self):
        return self.basic_salary + 10000   # management allowance


class Developer(Employee):
    def calculate_salary(self):
        return self.basic_salary + 7000    # technical allowance


class Tester(Employee):
    def calculate_salary(self):
        return self.basic_salary + 5000    # testing allowance


employees = [Manager(1, "Ravi", 40000), Developer(2, "Priya", 35000), Tester(3, "Amit", 30000)]
for e in employees:
    print(f"{e.name} ({e.__class__.__name__}) Salary: {e.calculate_salary()}")
