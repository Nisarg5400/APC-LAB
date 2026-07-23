

sub1 = float(input("Enter marks of Subject 1: "))
sub2 = float(input("Enter marks of Subject 2: "))
sub3 = float(input("Enter marks of Subject 3: "))

total = sub1 + sub2 + sub3
percentage = total / 3

print("Percentage =", percentage)

if percentage > 90:
    print("Grade: Excellent")
elif percentage >= 80:
    print("Grade: Very Good")
elif percentage >= 70:
    print("Grade: Good")
elif percentage >= 60:
    print("Grade: Average")
