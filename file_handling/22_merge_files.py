file1 = input("Enter first filename: ")
file2 = input("Enter second filename: ")
output_file = input("Enter output filename: ")

with open(file1, "r") as f1:
    content1 = f1.read()

with open(file2, "r") as f2:
    content2 = f2.read()

with open(output_file, "w") as f:
    f.write(content1)
    f.write(content2)

print("Files merged into", output_file)
