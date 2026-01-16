# Set basic operations
s = {2,3,4,4,8,5,9,9} # set cannot contain duplicate value so it print one value only once.
print(s)
print(f"length of s is {len(s)}")
print(type(s))

# Example 2
name = {"harsh","aashish","narayan","harsh",12,13,12,12.9,True} # it can contail diffrent data type
print(name)

# access all element using loop.
for value in name:
    print(value)

harry = set()
print(type(harry))
