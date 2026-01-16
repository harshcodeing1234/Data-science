# Write a program to find two number either 'a' is larger or 'b is larger
a = int(input("Enter your first number:"))
b = int(input("Enter your second number:"))

if a > b and a!=b:
    print("'a' is larger")
elif b > a and b!=a:
    print("b is larger")
else:
    print("a and b are equal")
