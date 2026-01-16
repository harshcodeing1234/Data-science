# file handling:

# open  a file / reading a file 
f = open(r"C:\Users\shali\OneDrive\Desktop\vs code\python\python topic\file i,o.py", 'r')
print(f)
text = f.read()
print(text)
f.close()

# rb' → Read (binary mode)
f = open(r"C:\Users\shali\OneDrive\Desktop\harsh album\Chhath puja\1730381278860.jpg", "rb")
data = f.read()
print(data[:10])  # first 10 bytes
f.close()

# 'r+' → Read & Write (text mode)
f = open(r"C:\Users\shali\OneDrive\Desktop\vs code\100 days of python\practice\file handling\data.txt", "r+")
print(f.read())   # read file
f.write(" Hello harsh")  # overwrites from start
print(f.read())
f.close()

# data = f.readline() # reads one line at a time
f = open(r"C:\Users\shali\OneDrive\Desktop\vs code\python\python topic\file i,o.py", 'r') # read data
data = f.readline() # line 1
print(data)
data = f.readline() # line 2
print(data)
f.close()


# With syntax:
with open("data.txt","r") as f:
    data = f.read()
    print(data)