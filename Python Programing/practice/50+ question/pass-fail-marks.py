# Program to check pass/fail based on marks

# Take marks of 3 subjects
sub1 = int(input("Enter marks of Subject 1: "))
sub2 = int(input("Enter marks of Subject 2: "))
sub3 = int(input("Enter marks of Subject 3: "))

total = sub1+sub2+sub3
percentage = total / 3

if sub1 < 33 or sub2 < 33 or sub3 <33:
    print("You failed. your marks in below than 33")
elif percentage < 40:
    print(f"You failed. your percentage is below than 40")
else:
    print(f"You are passed your percentage is {percentage:.2f}")
