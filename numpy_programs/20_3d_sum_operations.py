import numpy as np

arr = np.arange(1, 25).reshape(2, 3, 4)

print("Array:\n", arr)
print("Sum of all elements:", arr.sum())
print("Sum of each layer (axis=0 slices):", arr.sum(axis=(1, 2)))
print("Sum along rows (axis=2):\n", arr.sum(axis=2))
print("Sum along columns (axis=1):\n", arr.sum(axis=1))
