nums32 = [2, 7, 11, 15, 4]
target = 9
seen32 = {}
for num in nums32:
    complement = target - num
    if complement in seen32:
        print("Pair found:", complement, "and", num)
        break
    seen32[num] = True