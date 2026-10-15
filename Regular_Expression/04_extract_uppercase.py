import re

text = input("Enter a string: ")
uppercase = re.findall(r"[A-Z]", text)

print("Uppercase letters:", uppercase)
