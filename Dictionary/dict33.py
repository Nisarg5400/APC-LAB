string33 = "swiss"
char_count33 = {}
for ch in string33:
    char_count33[ch] = char_count33.get(ch, 0) + 1
for ch in string33:
    if char_count33[ch] == 1:
        print("First character occurring only once:", ch)
        break