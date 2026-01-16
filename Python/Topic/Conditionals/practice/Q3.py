# WAP to find the greatest of four number enterd by user
num1 = int(input("Enter your first number :"))
num2 = int(input("Enter your second number :"))
num3 = int(input("Enter your third number :"))
num4 = int(input("Enter your fourth number :"))

if num1 >= num2 and num1 >= num3 and num1 >= num4:
    print ("The greatest of the four numbers is :", num1)
elif num2 >= num1 and num2 >= num3 and num2 >= num4:
    print ("The greatest of the four numbers is :", num2)
elif  num3 >= num1 and num3 >= num2 and num3 >= num4:
    print("The greatest of the four numbers is :", num3)
else:
    print("The greatest of the four numbers is :",num4)
