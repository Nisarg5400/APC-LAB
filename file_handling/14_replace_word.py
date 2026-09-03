
filename = input("Enter filename: ")
old_word = input("Enter word to replace: ")
new_word = input("Enter replacement word: ")

with open(filename, "r") as f:
    content = f.read()

content = content.replace(old_word, new_word)

output_file = input("Enter output filename (can be same file): ")
with open(output_file, "w") as f:
    f.write(content)

print("Replacement done. Saved to", output_file)
