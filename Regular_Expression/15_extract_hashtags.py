import re

post = input("Enter a post: ")
hashtags = re.findall(r"#\w+", post)

print("Hashtags:", hashtags)
