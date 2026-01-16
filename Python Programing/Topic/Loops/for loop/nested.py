# For loop nested example
names = ["Harsh","kunal","neha","palak"]

for element in names:
    print(element)
    if element == "palak":
        print("Her special for me")
    for i in element:
        print(i)


# Nested For Loops in Python
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)
