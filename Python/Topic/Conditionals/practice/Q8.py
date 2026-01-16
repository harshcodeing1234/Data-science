# A spam comment is defined as a text containing following keywords: "Make a lot of money", "buy now", "subscribe this", "click this". Write a program to detect these spams.

text = input("Enter text:") 
spams = ['make a lot of money', 'buy now', 'subscribe this', 'click this']

if text in text:
    print("this is spams")
else:
    print("this is not spam")
