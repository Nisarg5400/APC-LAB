marks = {"Amit": 78, "Riya": 92, "Sam": 85}
low_scorer = min(marks, key=marks.get)
print("Highest scorer:", low_scorer, "with", marks[low_scorer], "marks")