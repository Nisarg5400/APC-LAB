import re

sentence = input("Enter a sentence: ")
words = re.findall(r"\b[Aa]\w*", sentence)

print("Words starting with A/a:", words)
