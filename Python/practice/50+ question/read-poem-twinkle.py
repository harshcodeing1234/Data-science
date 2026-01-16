# Write a program to read the text from a given file ‘poems.txt’ and find out whether it contains the word ‘twinkle
f = open("text/poem.txt",'r')
text = f.read()
word = input("Enter word:")
if word in text:
    print(f"The word present {text.count(word)} times in poem.txt file ")
else:
    print("The word do not present in poem.txt")

f.close()
