file1 = input("Enter first filename: ")
file2 = input("Enter second filename: ")

with open(file1, "r") as f1, open(file2, "r") as f2:
    lines1 = f1.readlines()
    lines2 = f2.readlines()

if lines1 == lines2:
    print("Files are identical")
else:
    max_lines = max(len(lines1), len(lines2))
    for i in range(max_lines):
        line1 = lines1[i] if i < len(lines1) else ""
        line2 = lines2[i] if i < len(lines2) else ""
        if line1 != line2:
            print("Files differ at line", i + 1)
            print("File1:", line1.rstrip())
            print("File2:", line2.rstrip())
            break
