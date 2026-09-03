
filename = input("Enter filename: ")

with open(filename, "r") as file:
    content = file.read()

print(content)
