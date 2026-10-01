import numpy as np

arr = np.array([10, 60, 45, 80, 30, 55, 20, 90, 15, 70])

print("Original array:", arr)
arr[arr > 50] = 0
print("After replacing (>50 -> 0):", arr)
