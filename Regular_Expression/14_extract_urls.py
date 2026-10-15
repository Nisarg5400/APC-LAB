import re

text = input("Enter text: ")
urls = re.findall(r"https?://[^\s]+", text)

print("URLs found:", urls)
