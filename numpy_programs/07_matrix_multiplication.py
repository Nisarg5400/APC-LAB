import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

result = np.matmul(a, b)   # or a @ b, or np.dot(a, b)

print("Matrix A:\n", a)
print("Matrix B:\n", b)
print("Matrix Multiplication:\n", result)
