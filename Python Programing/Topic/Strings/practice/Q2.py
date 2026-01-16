# Print even length word in a string
str = "Hello World" 
# i want to print only even word!
if(len(str)) %2 == 0:
    print(str)
elif (len(str)) %2 == 1:
    print(str, end="!")
    print("\n")
