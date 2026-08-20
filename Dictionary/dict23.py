nums23 = [1, 2, 2, 3, 3, 3, 4]
freq23 = {}
for n in nums23:
    freq23[n] = freq23.get(n, 0) + 1
print("Number frequency:", freq23)