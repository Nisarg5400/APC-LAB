
filename = input("Enter filename: ")

with open(filename, "r") as file:
    content = file.read().lower()

vowels = 0
consonants = 0
for ch in content:
    if ch.isalpha():
        if ch in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("Vowels:", vowels)
print("Consonants:", consonants)
