import numpy as np

marks = np.array([45, 67, 89, 34, 78, 90, 56, 23, 88, 76,
                   65, 54, 92, 41, 70, 83, 59, 77, 95, 62])

average = marks.mean()
above_average = marks[marks > average]

print("Marks:", marks)
print("Class Average:", average)
print("Students above average:", above_average)
