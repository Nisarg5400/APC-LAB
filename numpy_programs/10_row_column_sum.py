import numpy as np

arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 16]])

print("Matrix:\n", arr)
print("Sum of each row:", arr.sum(axis=1))
print("Sum of each column:", arr.sum(axis=0))
