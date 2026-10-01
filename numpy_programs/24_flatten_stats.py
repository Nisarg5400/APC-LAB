import numpy as np

arr = np.arange(1, 28).reshape(3, 3, 3)
flattened = arr.flatten()

print("Flattened array:", flattened)
print("Sum:", flattened.sum())
print("Average:", flattened.mean())
print("Maximum:", flattened.max())
print("Minimum:", flattened.min())
