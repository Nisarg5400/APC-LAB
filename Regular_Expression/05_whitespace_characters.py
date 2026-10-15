import re

text = "Hello World\tPython\nRegex Programs"
print("Text:", repr(text))

print("Spaces:", len(re.findall(" ", text)))
print("Tabs:", len(re.findall(r"\t", text)))
print("Newlines:", len(re.findall(r"\n", text)))
