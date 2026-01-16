# 
num = int(input("Enter number:"))
match num:
    case 1:
        print("one")
    case 2:
        print("two")
    case 3:
        print("Three")
    case _:
        print("Other number")
