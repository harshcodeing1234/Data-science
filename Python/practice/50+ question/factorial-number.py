# Write a program to calculate the factorial of a given number using for loop.
n = int(input("Enter a num:"))

i = 1
fact = 1
while i <=n:
    fact = fact*i
    i = i+1
print(f"factorial of {n} is {fact}")