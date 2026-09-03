
filename = input("Enter filename: ")

with open(filename, "r") as file:
    content = file.read()

words = content.split()
print("Total number of words:", len(words))
