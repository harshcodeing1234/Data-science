# raising custom error
salary = int(input("Enter salary amount: "))
if not 2000 < salary < 5000:
    raise ValueError("Not a valid salary")


# raising custom error if num is not between 5 and 10 or  i print only quit as a string.
value = input("Enter a num:")

if value == "quit":
    print("quit")
else:
    num = int(value)
    if num < 5 or num > 10:
        raise ValueError("not a valid number")
    else:
        print(num)


