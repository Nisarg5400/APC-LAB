student_dept = {"Amit": "CSE", "Rehan": "IT", "Soham": "CSE", "Nisarg": "ENTC", "Nikhil": "IT"}
grouped = {}
for name, dept in student_dept.items():
    if dept not in grouped:
        grouped[dept] = []
    grouped[dept].append(name)
print("Students grouped by department:", grouped)