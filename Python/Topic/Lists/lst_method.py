# list method:

# 1.list.sort()
# This method sorts the list in ascending order. The original list is updated

colors = ["voilet", "indigo", "blue", "green"]
colors.sort()
print(colors)

num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.sort()
print(num)

# What if you want to print the list in descending order?
# We must give reverse=True as a parameter in the sort method.
num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.sort(reverse=True)
print(num)

# reverse()
num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.reverse()
print(num)

# index()
num = [4,2,5,3,6,1,2,1,3,2,8,9,7]
print(num.index(3))

# count()
num = [4,2,5,3,6,1,2,1,3,2,8,9,7]
print(num.count(3))

# copy()
colors = ["voilet", "green", "indigo", "blue"]
newlist = colors.copy()
print(colors)
print(newlist)

# append()
colors = ["voilet", "indigo", "blue"]
colors.append("green")
print(colors)

# insert()
colors = ["voilet", "indigo", "blue"]
#           [0]        [1]      [2]

colors.insert(1, "green")   #inserts item at index 1
# updated list: colors = ["voilet", "green", "indigo", "blue"]
#       indexs              [0]       [1]       [2]      [3]

print(colors)

# extend()
#add a list to a list
colors = ["voilet", "indigo", "blue"]
rainbow = ["green", "yellow", "orange", "red"]
colors.extend(rainbow)
print(colors)

# Concatenating two lists:
colors = ["voilet", "indigo", "blue", "green"]
colors2 = ["yellow", "orange", "red"]
print(colors + colors2)