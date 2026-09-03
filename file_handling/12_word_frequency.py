
filename = input("Enter filename: ")

with open(filename, "r") as f:
    content = f.read().lower()

words = content.split()
frequency = {}

for word in words:
    word = word.strip(".,!?;:\"'")
    frequency[word] = frequency.get(word, 0) + 1

for word, count in frequency.items():
    print(word, ":", count)
