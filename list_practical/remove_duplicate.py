numbers = [1, 2, 2, 3, 1, 4, 3]

unique = []

for n in numbers:
    if n not in unique:
        unique.append(n)

print(unique)