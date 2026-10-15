import re

text = input("Enter filenames separated by spaces: ")
extensions = re.findall(r"\.(\w+)\b", text)

print("File extensions:", extensions)
