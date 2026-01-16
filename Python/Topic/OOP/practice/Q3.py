# Create a class with a class attribute a; create an object from it and set ‘a’ directly using ‘object.a = 0’. Does this change the class attribute?

class myclass:
    a = 5

obj = myclass()
obj.a=0

print("Object a:", obj.a)         
print("Class a:", myclass.a)

myclass.a = 10

print("Class a after change:", myclass.a)  
print("Object a still:", obj.a)
