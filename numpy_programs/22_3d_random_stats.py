import numpy as np

arr = np.random.randint(1, 100, size=(3, 4, 5))

print("Array:\n", arr)
print("Mean:", arr.mean())
print("Median:", np.median(arr))
print("Standard deviation:", arr.std())
print("Variance:", arr.var())
print("Minimum:", arr.min())
print("Maximum:", arr.max())
