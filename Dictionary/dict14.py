ch_feq = input("Enter a string: ")
char_freq = {}
for ch in ch_feq:
    char_freq[ch] = char_freq.get(ch, 0) + 1
print("Character frequency:", char_freq)