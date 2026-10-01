import numpy as np

marks = np.array([78, 85, 45, 92, 67, 88, 73, 55, 95, 60])

print("Marks:", marks)
print("Highest marks:", marks.max())
print("Lowest marks:", marks.min())
print("Average marks:", marks.mean())
print("Median:", np.median(marks))
print("Standard deviation:", np.std(marks))
