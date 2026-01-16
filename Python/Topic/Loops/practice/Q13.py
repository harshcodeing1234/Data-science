# Print fibonacci series up to 10 terms
i = 0
a , b = 0 , 1

while i < 10:
    print(a)
    a, b = b, a + b
    i = i + 1
