import re

code = '''x = 10  # store value
print("Hello # not a comment")
# full line comment
y = 20  # another comment
'''

comments = re.findall(r"#.*", code)
print("Comments found:")
for c in comments:
    print(c)


