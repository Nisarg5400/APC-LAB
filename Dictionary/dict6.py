emp_dict = {101: "Amit", 102: "Riya", 103: "Sam"}
search_id = int(input("Enter employee ID to check: "))
if search_id in emp_dict:
    print("Employee found:", emp_dict[search_id])
else:
    print("Employee ID does not exist")