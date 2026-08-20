students25 = {"Amit": 78, "Riya": 92, "Sam": 85}

students25["Neha"] = 88
students25["Amit"] = 82
students25.pop("Sam")
search_name = "Riya"
if search_name in students25:
    print(search_name, "found with marks:", students25[search_name])
print("All students:", students25)
topper25 = max(students25, key=students25.get)
print("Highest marks:", topper25, students25[topper25])
print("Average marks:", sum(students25.values()) / len(students25))