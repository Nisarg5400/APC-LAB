contacts = {"Amit": "9876543210", "Rehan": "9123456780"}

# Add contact
contacts["Soham"] = "9988776655"

# Search contact
search_name28 = "Rehan"
if search_name28 in contacts:
    print(search_name28, "number:", contacts[search_name28])

# Update contact
contacts["Amit"] = "9000000000"

# Delete contact
contacts.pop("Soham")

# Display all contacts
print("All contacts:", contacts)