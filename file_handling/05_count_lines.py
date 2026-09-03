
filename = input("Enter filename: ")

with open(filename, "r") as file:
    lines = file.readlines()

print("Total number of lines:", len(lines))
