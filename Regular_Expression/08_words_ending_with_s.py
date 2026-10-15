import re

sentence = input("Enter a sentence: ")
words = re.findall(r"\b\w*s\b", sentence)

print("Words ending with s:", words)
