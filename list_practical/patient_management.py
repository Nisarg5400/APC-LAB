names = ["Amit", "Rahul", "Nisarg"]
ages = [20, 25, 21]

# Add patient
names.append("Sahil")
ages.append(30)

# Search patient
name = input("Enter patient name: ")

if name in names:
    index = names.index(name)
    print("Patient found")
    print("Name:", names[index])
    print("Age:", ages[index])
else:
    print("Patient not found")

# Delete patient
name = "Rahul"

if name in names:
    index = names.index(name)
    names.pop(index)
    ages.pop(index)

print("All patients:")

for i in range(len(names)):
    print(names[i], ages[i])

print("Total patients:", len(names))