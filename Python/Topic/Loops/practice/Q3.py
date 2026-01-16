# Search a number x in tuple
x = int(input("Enter number:"))
num = (1,4,9,16,25,36,49,64,81,100)

for i in num:
    if i == x:
        print("number found",x)
        break
    else:
        print("number not found")
