

ch = input("Enter an alphabet: ").lower()

if len(ch) == 1 and ch.isalpha():
    if ch in ['a', 'e', 'i', 'o', 'u']:
        print(ch, "is a Vowel.")
    else:
        print(ch, "is a Consonant.")
else:
    print("Invalid input! Please enter a single alphabet.")