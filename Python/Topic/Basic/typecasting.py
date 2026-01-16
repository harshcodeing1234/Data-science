# typecasting
a = "10"
b = int(a) #string convert to integer
print(b)
print(type(a))
print(type(b))

# 
a = ['10', '20','30','40',]

b = tuple(a) # list converts to tupple
print(b)
print(type(a))
print(type(b))

# 
a = 55.45
b = int(a)
print(b) # float convert into int
print(type(a))
print(type(b))

#
a = "12"
b = "17"

print(int(a)+int(b)) # convert string to int
print(type(a),type(b))
print(type((int(a))),type(int(b)))

