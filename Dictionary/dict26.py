salaries = {"Amit": 45000, "Rehan": 62000, "Soham": 38000, "Nisarg": 71000}
highest_paid = max(salaries, key=salaries.get)
lowest_paid = min(salaries, key=salaries.get)
avg_salary = sum(salaries.values()) / len(salaries)
print("Highest salary:", highest_paid, salaries[highest_paid])
print("Lowest salary:", lowest_paid, salaries[lowest_paid])
print("Average salary:", avg_salary)
print("Employees earning more than 50,000:")
for name, sal in salaries.items():
    if sal > 50000:
        print(name, ":", sal)