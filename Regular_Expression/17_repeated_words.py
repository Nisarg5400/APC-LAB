import re

sentence = input("Enter a sentence: ")
repeated = re.findall(r"\b(\w+)\s+\1\b", sentence, re.IGNORECASE)

print("Repeated words:", repeated)
