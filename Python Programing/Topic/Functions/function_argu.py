# FUNCTIONS WITH ARGUMENTS AND RETURN VALUES.
def greet(name):
    gr = "Hello " + name
    return gr # return value
name = greet("Harsh") #arguments
print(name)

name2 = greet("Shali")
print(name2)

# or
def greet(name,age):
    gr = "I am " + name + " and my age is",age
    print(gr)

greet('Harsh',18) # calling the function
greet('Shali',20)

# defult argument
def add(a=3,b=2):
    sum = a+b
    print(sum)

add()
add(6) # 'a' value was change now value is 6
add(6,7) # 'b' value was change now value is 7

# keyboard arguments
add(a=6,b=8) # 'a' and 'b' values were changed now their values are 6 and 8

# variable length arguments
def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum+i
    print(f"sum of the given number is {sum}")
average(4,3,9)
