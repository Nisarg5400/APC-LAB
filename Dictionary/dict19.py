dict19 = {"a": 1, "b": 2, "c": 1, "d": 3, "e": 2}
seen_values = set()
result19 = {}
for key, value in dict19.items():
    if value not in seen_values:
        result19[key] = value
        seen_values.add(value)
print("Dictionary after removing duplicate values:", result19)