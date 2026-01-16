# A lambda function is a small anonymous function.

# Syntax:lambda arguments : expression

x = lambda a, b: print(a*b)
x(4,5)

# lambda vs def function
# Using lambda
sq = lambda x: x ** 2
print(sq(3))

# Using def
def sqdef(x):
    return x ** 2
print(sqdef(3))

# Lambda with List Comprehension
li = [lambda arg=x: arg * 10 for x in range(1, 5)]
for i in li:
    print(i())

# Lambda with if-else
check = lambda x: "even" if x%2==0 else "odd"
print(check(3))


