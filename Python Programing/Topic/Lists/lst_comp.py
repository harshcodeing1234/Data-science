# 
# Syntax:
# List = [Expression(item) for item in iterable if Condition]

lst = [i for i in range(10)]
print(lst)

# List with condition
list = [i for i in range(10) if i % 2 == 0]
print(lst)

# list with all parameter
lst = [i for i in range(0,10,2) ]
print(lst)

# Example 1: Accepts items with the small letter “o” in the new list
names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if "o" in item]
print(namesWith_O)

# Example 2: Accepts items which have more than 4 letters
name = ["harsh", "aashish", "amisha", "sanya", "rosa"]
name_a =[[i for i in name if (len(i) >= 5) ]]
print(name_a)

