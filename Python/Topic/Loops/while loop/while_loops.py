# 
i = 0
while (i <=10):
    print(i)
    i=i+1 

# 
age = int(input("Enter your age:"))
while (age > 18):
    age = int(input("You are enough to vote. Please enter your age again:"))
    print(age)
    if (age < 18):
        break
print("done with your age")

# Infinite while Loop in Python
age = 28

# the test condition is always True
while age > 19:
    print('Infinite Loop')
i = 1
while i<=10:
    print(5*i)
    i = i+1
    if i == 5:
        break
else:
    print("something ellse")
