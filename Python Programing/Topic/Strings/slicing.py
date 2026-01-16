# 
s = "Harsh kumar"

print(s[1:4])  

print(s[:3])   

print(s[3:])   

print(s[::-1])

s = "Harsh"

# Trying to change the first character raises an error
# s[0] = 'I'  # Uncommenting this line will cause a TypeError

# Instead, create a new string
s = "G" + s[1:]
print(s)

# length of a string
s = "Harsh"
print(len(s))

nm = "Harry"
print(nm[-4:-2])