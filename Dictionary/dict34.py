string34 = "swiss"
char_count34 = {}
for ch in string34:
    char_count34[ch] = char_count34.get(ch, 0) + 1
for ch in string34:
    if char_count34[ch] > 1:
        print("First character occurring more than once:", ch)
        break