class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def display(self):
        print(f"ID: {self.emp_id}, Name: {self.name}, Salary: {self.salary}")


class Manager(Employee):
    def __init__(self, emp_id, name, salary, department):
        super().__init__(emp_id, name, salary)
        self.department = department

    def display(self):
        super().display()
        print(f"Department: {self.department}")

    def annual_salary(self):
        return self.salary * 12


m1 = Manager(1, "Ravi", 60000, "IT")
m1.display()
print("Annual Salary:", m1.annual_salary())
