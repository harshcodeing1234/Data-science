# THE BREAK STATEMENT:break’ is used to come out of the loop when encountered. It instructs the program to exit the loop now.

for i in range (0,80):
    print(i) # this will print 0,1,2 and 3
    if i==3:
        break

# with while loop
i = 0
while i < 5: # print "Harry" – 5 times!
    print("Harry")
    i = i + 1
    if i == 3:
        break 


# continue:
for i in range(4):
    print("printing")
    if i == 2: # if i is 2, the iteration is skipped
        continue
    print(i)
print()
# with while loop
# Prints all letters except 'e' and 's'
i = 0
a = 'geeksforgeeks'

while i < len(a):
    if a[i] == 'e' or a[i] == 's':
        i += 1
        continue
        
    print(a[i])
    i += 1


# PASS STATEMENT: pass is a null statement in python.
l = [1,7,8]
for item in l:
    pass 