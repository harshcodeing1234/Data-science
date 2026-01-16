# Write a program to find out whether a given post is talking about "Harry" or not.

word = input("Enter name:")
post = "A post is a message or content shared by Harry on social media online to inform, express ideas, connect with others, or start conversations."

if word in post:
    print("given post is talkin about word")
else:
    print("given post is not talking about word")
