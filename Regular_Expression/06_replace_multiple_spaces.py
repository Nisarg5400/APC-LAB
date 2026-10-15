import re

text = input("Enter text with extra spaces: ")
result = re.sub(r" +", " ", text)

print("Result:", result)
