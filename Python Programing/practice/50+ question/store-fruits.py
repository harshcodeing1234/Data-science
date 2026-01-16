# 1. Write a program to store seven fruits in a list entered by the user.
fruits = input("Enter list seprated by spaces:")
fruits_list = list(map(str,fruits.split()))
print(f"Fruits = {fruits_list}")