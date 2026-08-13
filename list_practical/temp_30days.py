temperature = [30, 32, 29, 35, 31, 33, 28, 36, 34, 30,
               29, 31, 37, 32, 33, 35, 30, 28, 34, 36,
               31, 29, 32, 38, 35, 30, 33, 34, 29, 31]

average = sum(temperature) / len(temperature)

print("Hottest:", max(temperature))
print("Coldest:", min(temperature))
print("Average:", average)

print("Above average:")

for t in temperature:
    if t > average:
        print(t)

print("Below average:")

for t in temperature:
    if t < average:
        print(t)