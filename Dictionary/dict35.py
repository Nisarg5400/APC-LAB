paragraph = input("Enter a paragraph: ")
words35 = paragraph.split()
length_count = {}
for word in words35:
    length = len(word)
    length_count[length] = length_count.get(length, 0) + 1
print("Word length frequency:", length_count)