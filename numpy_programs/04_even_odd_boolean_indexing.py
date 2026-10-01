import numpy as np

arr = np.arange(1, 21)

even_numbers = arr[arr % 2 == 0]
odd_numbers = arr[arr % 2 != 0]

print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)
