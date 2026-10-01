import numpy as np

arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 16]])

print("Array:\n", arr)
print("First row:", arr[0])
print("Last column:", arr[:, -1])
print("Diagonal elements:", np.diagonal(arr))
print("2nd and 3rd rows:\n", arr[1:3])
