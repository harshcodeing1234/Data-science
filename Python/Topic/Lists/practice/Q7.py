# WAP to store seven fruits in a list enterd by the user.
fruits = input("Enter fruits names seprated by spaces:")
fruits_list = list(map(str,fruits.split()))
print("Fruit list is:",fruits_list)
