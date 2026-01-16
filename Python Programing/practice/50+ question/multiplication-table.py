# Write a program to print multiplication table of a given number using for loop.
num = int(input("Enter multiplication num:"))
for i in range(1,11):
    print(f"{num} * {i} = {num*i}")
