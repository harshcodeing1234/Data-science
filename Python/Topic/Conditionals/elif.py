# elif Statement
age = 25

if age <= 12:
    print("Child.")
elif age <= 19:
    print("Teenager.")
elif age <= 35:
    print("Young adult.")
else:
    print("Adult.")

# input from user.
age = int(input('Enter your age:'))
if age <= 12:
    print("Child")
elif age <= 19:
    print("Teenager.")
elif age <= 35:
    print("Young adult.")
else:
    print("Adult.")

# 
price = int(input("Enter price:"))
budget = int(input("Enter your budget:"))
add_budget = price - budget

if (price<=budget):
    print("You can buy this product")
elif(price-budget > 0):
    print(f"You need to add {add_budget} more money")
else:
    print("you have no budget")
    