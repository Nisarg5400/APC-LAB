import re

references = """
Smith, J. (2021). Deep Learning Basics. doi:10.1000/xyz123. Contact: smith@univ.edu
Rao, A. (2019). Data Mining. https://example.com/paper1 DOI: 10.1016/j.abc.2019.05.001
Lee, K. (2023). AI Ethics. Email: lee.k@research.org URL: http://research.org/ai
"""

dois = re.findall(r"10\.\d{4,9}/[^\s]*[^\s.,;]", references)
years = re.findall(r"\((\d{4})\)", references)
emails = re.findall(r"[\w.+-]+@[\w-]+(?:\.[\w-]+)+", references)
urls = re.findall(r"https?://[^\s]+", references)

print("DOIs:", dois)
print("Years:", years)
print("Emails:", emails)
print("URLs:", urls)
