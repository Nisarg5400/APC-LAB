
filename = input("Enter filename: ")
search_word = input("Enter word to search: ")

count = 0
line_numbers = []

with open(filename, "r") as f:
    for line_no, line in enumerate(f, start=1):
        words = line.split()
        if search_word in words:
            count += words.count(search_word)
            line_numbers.append(line_no)

print("Occurrences:", count)
print("Found on lines:", line_numbers)
