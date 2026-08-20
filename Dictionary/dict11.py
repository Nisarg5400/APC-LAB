marks = {"Amit": 78, "Riya": 92, "Sam": 85}
topper = max(marks, key=marks.get)
print("Highest scorer:", topper, "with", marks[topper], "marks")