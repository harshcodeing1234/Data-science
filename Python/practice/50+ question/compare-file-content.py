# Write a program to find out whether a file is identical & matches the content of
# another file.

file1 = input("Enter file name:")
file2 = input("Enter file name:")
with open(file1, "r", encoding="utf-8") as f:
    content1 = f.read()
with open(file2, "r", encoding="utf-8") as f:
    content2 = f.read()

if content1 == content2:
    print("Yes both file is identical")
else:
    print("No files are not identical")