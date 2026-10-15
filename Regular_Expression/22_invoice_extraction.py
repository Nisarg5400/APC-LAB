import re

invoice = """
Invoice No: INV-2024-001
Date: 15-03-2024
Item: Laptop        Amount: Rs. 55,000.00
Item: Mouse         Amount: Rs. 500.50
Total: Rs. 55,500.50
"""

invoice_numbers = re.findall(r"INV-\d{4}-\d{3}", invoice)
dates = re.findall(r"\d{2}-\d{2}-\d{4}", invoice)
amounts = re.findall(r"Rs\.\s?[\d,]+\.\d{2}", invoice)

print("Invoice numbers:", invoice_numbers)
print("Dates:", dates)
print("Amounts:", amounts)
