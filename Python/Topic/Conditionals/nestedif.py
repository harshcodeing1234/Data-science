# Nested if..else Conditional Statements
age = 70
is_member = True

if age >= 60:
    if is_member:
        print("30% senior discount!")
    else:
        print("20% senior discount.")
else:
    print("Not eligible for a senior discount.")

# 
marks = int(input("Enter marks:"))
if marks >=90:
    if marks >95:
        print("topper")
    else:
        print("A+ grade")
elif marks >=80:  
        print("A grade")
else:
    if marks >= 60:
        print("B grade")
    else:
        print("C grade") 
