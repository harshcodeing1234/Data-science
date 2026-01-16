# Indexing: Accessed element in a list
# Eg:
lst = [1,2,3,4,5]
lst2 = ["a","b","c","d"]
lst3 = [12, 12.45, "orange", True]

print(lst[0]) #Access element
print(type(lst[0])) #check type

print(lst[-1])  # negative indexing
print(type(lst[-1]))

print(lst3[3])
print(type(lst3[3]))

print(lst3[1])
print(type(lst3[1]))

print(lst2[3])
print(type(lst2[3]))

print(lst3[2])
print(type(lst3[2]))
print("\n")

# Accesed all element in a lst
for i in lst:
    print(i)
    print(type(i))
# Accesed all element in a lst2   
for i in lst2:
    print(i)
    print(type(i))

# Accesed all element in a lst3
for i in lst3:
    print(i)
    print(type(i))

# check element in list or not

if 56 in lst:
    print("56 is present in lst")
else:
    print("not present in list")

# list slicing
# Eg:
lst4 = [1, 2, 3, 4, 5,]
print(lst4[1:4])  # Slicing from index 1 to 3

# negative
print(lst4[-4:-1])  # Slicing from index -4 to -2 

# lst[start:stop:step]
lst = [10, 20, 30, 40, 50, 60]
print(lst[::2])
print(lst[1::2])  # Slicing with step of 2
print(lst[1:4:2])  # Slicing with step of 2
