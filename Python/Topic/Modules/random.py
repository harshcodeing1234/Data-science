# # importing built in module random
import random 

# printing random integer between 0 and 5
print(random.randint(0, 5))  

# print random floating point number between 0 and 1
print(random.random())  

# random number between 0 and 100
print(random.random() * 100)  

# using choice function in random module for choosing  a random element from a set such as a list.
List = [1, 4, True, 800, "python", 27, "hello"]
print(random.choice(List)) 