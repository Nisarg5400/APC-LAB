
with open("students.csv", "w") as f:
    f.write("101,Amit,85\n")
    f.write("102,Priya,92\n")
    f.write("103,Rahul,78\n")

# Read records into a list
records = []
with open("students.csv", "r") as f:
    for line in f:
        roll, name, marks = line.strip().split(",")
        records.append((roll, name, int(marks)))

# Display all records
print("All Records:")
for roll, name, marks in records:
    print(roll, name, marks)

# Highest marks
topper = max(records, key=lambda r: r[2])
print("\nHighest marks:", topper)

# Average marks
average = sum(r[2] for r in records) / len(records)
print("Average marks:", average)

# Students scoring more than 80
print("\nStudents scoring more than 80:")
for roll, name, marks in records:
    if marks > 80:
        print(roll, name, marks)
