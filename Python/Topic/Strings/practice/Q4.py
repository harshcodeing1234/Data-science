# Check if a string has at least one letter and one number
s = "abc123"

letter = any(char.isalpha() for char in s)
digit = any(char.isdigit() for char in s)

if letter and digit:
    print("String has at least one letter and one number")
else:
    print("String does not have both letter and number")
