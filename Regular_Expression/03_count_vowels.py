import re

text = input("Enter a string: ")
vowels = re.findall(r"[aeiouAEIOU]", text)

print("Vowels:", vowels)
print("Total vowels:", len(vowels))
