# Write a program to make a copy of a text file “this. txt”
with open ("text/this.txt")as f:
    content = f.read()
    with open("text/this_copy.txt", "w") as f:
        f.write(content)