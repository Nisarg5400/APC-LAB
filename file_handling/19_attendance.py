with open("attendance.csv", "w") as f:
    f.write("Amit,60,80\n")
    f.write("Priya,70,80\n")
    f.write("Rahul,50,80\n")

with open("attendance.csv", "r") as f:
    print("Attendance below 75%:")
    for line in f:
        name, attended, total = line.strip().split(",")
        attended = int(attended)
        total = int(total)
        percentage = (attended / total) * 100
        print(f"{name}: {percentage:.2f}%")
        if percentage < 75:
            print(f"  -> {name} is below 75% attendance")
