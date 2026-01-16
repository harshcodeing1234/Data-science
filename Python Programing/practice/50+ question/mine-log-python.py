# Write a program to mine a log file and find out whether it contains ‘python’.
with open("text/log.txt",'r') as f:
    text = f.read()
    if "python" in text:
        print("Yes python is present at",text.find("python"))
    else:
        print("python is not present")