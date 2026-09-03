

def read_employees(filename):
    employees = []
    with open(filename, "r") as f:
        for line in f:
            emp_id, name, dept, salary = line.strip().split(",")
            employees.append((emp_id, name, dept, float(salary)))
    return employees

def display_all(employees):
    for e in employees:
        print(e)

def highest_paid(employees):
    return max(employees, key=lambda e: e[3])

def average_salary(employees):
    return sum(e[3] for e in employees) / len(employees)

def above_salary(employees, limit):
    return [e for e in employees if e[3] > limit]

# Create sample file
with open("employees.csv", "w") as f:
    f.write("1,John,IT,50000\n")
    f.write("2,Meena,HR,45000\n")
    f.write("3,Ravi,Finance,60000\n")

employees = read_employees("employees.csv")

print("All Employees:")
display_all(employees)

print("\nHighest paid:", highest_paid(employees))
print("Average salary:", average_salary(employees))

limit = float(input("\nEnter salary limit: "))
print("Employees earning above", limit, ":")
display_all(above_salary(employees, limit))
