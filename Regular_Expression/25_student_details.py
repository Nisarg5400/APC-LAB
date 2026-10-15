import re

paragraph = "Amit has roll number 101 and scored 85 marks. Priya has roll number 102 and scored 92 marks."

pattern = r"(\w+) has roll number (\d+) and scored (\d+) marks"
students = re.findall(pattern, paragraph)

for name, roll, marks in students:
    print(f"Name: {name}, Roll No: {roll}, Marks: {marks}")
