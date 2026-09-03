
filename = input("Enter filename: ")
output_file = "upper_" + filename

with open(filename, "r") as f:
    content = f.read()

with open(output_file, "w") as f:
    f.write(content.upper())

print("Uppercase file created:", output_file)
