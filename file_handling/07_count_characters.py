
filename = input("Enter filename: ")

with open(filename, "r") as file:
    content = file.read()

print("Total number of characters:", len(content))
