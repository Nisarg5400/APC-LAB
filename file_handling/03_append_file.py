
filename = input("Enter filename: ")
new_info = input("Enter information to append: ")

with open(filename, "a") as file:
    file.write(new_info + "\n")

print("Information appended successfully")
