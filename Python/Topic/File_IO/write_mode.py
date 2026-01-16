# write mode

f = open("hello.txt", 'w')
f.write("This is my personal file: \n Hello \n Good morning Everyone")
f.close()

# 'w+' → Write & Read (text mode)
f = open("data.txt", "w+")
f.write("New data")
f.seek(0)
print(f.read())  # New data
f.close()

# with syntax
with open("python.txt","w") as f:
    data = f.write("Hello, this is a test file.")
