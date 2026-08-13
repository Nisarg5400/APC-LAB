numbers = [1, 2, 2, 3, 3, 3, 4]

frequency = {}

for n in numbers:
    if n in frequency:
        frequency[n] += 1
    else:
        frequency[n] = 1

print(frequency)