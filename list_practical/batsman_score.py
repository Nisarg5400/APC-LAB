scores = [45, 100, 75, 120, 50, 30, 85, 110, 25, 60]

print("Highest:", max(scores))
print("Lowest:", min(scores))
print("Total runs:", sum(scores))
print("Average:", sum(scores) / len(scores))

centuries = 0
half_centuries = 0

for score in scores:
    if score >= 100:
        centuries += 1
    elif score >= 50:
        half_centuries += 1

print("Centuries:", centuries)
print("Half-centuries:", half_centuries)