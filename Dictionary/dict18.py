dict18_a = {"a": 1, "b": 2, "c": 3}
dict18_b = {"x": 3, "y": 4, "z": 2}
common_values = set(dict18_a.values()) & set(dict18_b.values())
print("Common values:", common_values)