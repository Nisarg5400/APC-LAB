
filename = input("Enter filename: ")

with open(filename, "r") as f:
    content = f.read()

words = content.split()
longest = ""
for word in words:
    if len(word) > len(longest):
        longest = word

print("Longest word:", longest)
