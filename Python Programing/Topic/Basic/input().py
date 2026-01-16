# input() function

# Taking input as string
color = input("What color is rose?: ")
print(color)

# Taking input as int
# Typecasting to int
n = int(input("How many roses?: "))
print(n)

# Taking input as float
# Typecasting to float
price = float(input("Price of each rose?: "))
print(price)
print(f"price of total rose={n*price}")

# Exersise 1: Taking the Name and Age of the user as input and printing it
name = input("Please Enter Your Name: ")

age = input("Please Enter Your Age: ")

print("Name & Age: ", name, age)

# 2.takin two integers from user and printing it
num1 = int(input("Enter first num:"))
num2 = int(input("Enter second num:"))
print(f"{num1}+{num2}={num1+num2}")

# 3.taking two list as input and appending it
list1 = list(input("Enter list:"))
list2 = list(input("Enter list:"))
for i in list2:
    list1.append(i)
    print(list1)
print(f"final list{list1}")

# Write a python program to find remainder when a number is divided by 2.
num = int(input("enter num:"))
rem = num%2
print(rem)

# Write a python program to find an average of two numbers entered by the user.
num1 = int(input("Enter first num:"))
num2 = int(input("Enter second num:"))
sum = num1+num2
average = sum/2
print("average is:", average)

# Write a python program to calculate the square of a number entered by the user
num = int(input("Enter num:"))
square = num*num
print("square is:",square) 


