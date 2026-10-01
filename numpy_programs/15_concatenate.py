import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

horizontal = np.concatenate((a, b), axis=1)
vertical = np.concatenate((a, b), axis=0)

print("Array A:\n", a)
print("Array B:\n", b)
print("Horizontal concatenation:\n", horizontal)
print("Vertical concatenation:\n", vertical)
