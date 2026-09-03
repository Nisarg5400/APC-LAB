
filename = input("Enter Python filename: ")
output_file = "no_comments_" + filename

with open(filename, "r") as f:
    lines = f.readlines()

with open(output_file, "w") as f:
    for line in lines:
        if "#" in line:
            line = line[:line.index("#")]
            if line.strip() == "":
                continue
            line += "\n"
        f.write(line)

print("Comments removed. Saved to", output_file)
