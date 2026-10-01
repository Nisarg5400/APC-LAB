import numpy as np

arr = np.array([34, 12, 89, 45, 7, 56, 23])

ascending = np.sort(arr)
descending = np.sort(arr)[::-1]

print("Original array:", arr)
print("Ascending order:", ascending)
print("Descending order:", descending)
