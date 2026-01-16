# append mode 
f = open("data.txt", "a")
f.write("\nExtra line")
f.close()

# 'a+' → Append & Read (text mode)
f = open("data.txt", "a+")
f.write("\nMore text")
f.seek(0)
print(f.read())
f.close()


# with syntax
with open(r"demo.txt","a") as f:
    data = f.write("\nhello sir")
    
