marks = [70, 80, 65, 90, 55, 75, 85, 60, 95, 72,
         68, 88, 76, 92, 50, 82, 78, 69, 87, 73]

highest = max(marks)
lowest = min(marks)
average = sum(marks) / len(marks)

above = 0
below = 0

for m in marks:
    if m > average:
        above += 1
    elif m < average:
        below += 1

print("Highest:", highest)
print("Lowest:", lowest)
print("Average:", average)
print("Above average:", above)
print("Below average:", below)