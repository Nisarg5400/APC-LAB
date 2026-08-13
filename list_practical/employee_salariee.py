salaries = [25000, 45000, 60000, 30000, 75000, 28000]

print("Highest:", max(salaries))
print("Lowest:", min(salaries))
print("Average:", sum(salaries) / len(salaries))

print("Above 50000:")

for salary in salaries:
    if salary > 50000:
        print(salary)

print("Below 30000:")

for salary in salaries:
    if salary < 30000:
        print(salary)