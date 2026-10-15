import re

paragraph = input("Enter a paragraph: ")
pincodes = re.findall(r"\b[1-9]\d{5}\b", paragraph)

print("PIN codes:", pincodes)
