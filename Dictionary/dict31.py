words31 = ["cat", "dog", "apple", "bat", "banana", "ox"]
length_dict = {}
for word in words31:
    length = len(word)
    if length not in length_dict:
        length_dict[length] = []
    length_dict[length].append(word)
print("Words grouped by length:", length_dict)