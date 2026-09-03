
filename = input("Enter filename: ")

with open(filename, "r") as file:
    lines = file.readlines()

for line in reversed(lines):
    print(line.rstrip("\n"))
