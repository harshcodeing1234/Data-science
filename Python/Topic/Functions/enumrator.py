# enumrator function.
# Eg;

name = ['Harsh','Ravi','kurnal','sushant']

for n,i in enumerate(name):
    print(n,i)
print()
# Changing the start index
fruits = ['mango','banana','apple','orange']

for index,fruit in enumerate(fruits ,start=1):
    print(f"{index}:{fruit}")