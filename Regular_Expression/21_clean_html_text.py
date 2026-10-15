import re

text = """<html><body>
<h1>Welcome   to   Python!!!</h1>
<p>Regular   expressions   are   powerful;;; and   useful...</p>
</body></html>"""

text = re.sub(r"<[^>]+>", " ", text)           # remove HTML tags
text = re.sub(r"[^\w\s]", "", text)            # remove punctuation
text = re.sub(r"\s+", " ", text).strip()       # remove extra whitespace

print("Cleaned text:", text)
