# Exeption handling:
# using else
try:
    a = int(input("Enter A num:"))
    res = 100/a
except ZeroDivisionError:
    print("Divide by zero")
except ValueError:
    print("enter valid input!")
except TypeError:
    print("type error")

else:
    print(f"result = {res}")


# using multiple except
a = input("Enter the number: ")
print(f"Multiplication table of {a} is: ")
try:
  for i in range(1, 11):
    print(f"{int(a)} X {i} = {int(a)*i}")
except:
  print("Invalid  Input!")

print("Some imp lines of code")
print("End of program")


# using other type of error
try:
    num = int(input("Enter an integer: "))
    a = [6, 3]
    print(a[num])
except ValueError:
    print("Number entered is not an integer.")
    
except IndexError:
  print("Index Error")


# /finaly keyboard:
try:
    num = int(input("Enter a num:"))
    a = ["harsh", 12, "kumar", 12.98, True]
    result = a[num]
except IndexError:
    print("list index out of range")
except ValueError:
    print("Please enter a valid integer.")
else:
    print(f"Selected element: {result}")
finally:
    print("code completion")

