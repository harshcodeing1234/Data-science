def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def devide(a,b):
    return a/b
def calculator():
    while True:
        print("choose your operation:")
        print("1.Add")
        print("2.Subtract:")
        print("3.Multiply:")
        print("4.devide:")

        choice = input("Enter your choice 1/2/3/4:")
        if choice in ['1','2','3','4']:
            num1 = float(input("Enter your first num:"))
            num2 = float(input("Enter your second num:"))

            if choice =='1':
                print(f"{num1}+{num2}={add(num1,num2)}")
            elif choice =='2':
                print(f"{num1}-{num2}={subtract(num1,num2)}")
            elif choice =='3':
                print(f"{num1}*{num2}={multiply(num1,num2)}")
            elif choice =='4':
                print(f"{num1}/{num2}={devide(num1,num2)}")
        else:
            print("Invalid Input")
        next_calculation = input("DO you want to next calculation? (yes/no:)")
        if next_calculation.lower() != 'yes':
            break

if __name__ == "__main__":
    calculator()




    



    
    
