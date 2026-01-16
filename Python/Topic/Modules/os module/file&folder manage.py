# file and folder manegment
# List all files & folders
import os
print(os.listdir("."))  # Current folder
folders = os.listdir(r"C:\Users\shali\OneDrive\Desktop")
for folder in folders:
    print(folder)


# create folder
try:
    if (not os.path.exists("data")):
        os.mkdir ("data")
except FileExistsError:
    print("file already exist")

# if i want create 100 folder in data folder
try:
    for i in range (1,101):
        os.mkdir(f"data/Day{i}/main.py")
        
except FileExistsError:
    print("file already exist")
except FileNotFoundError:
    print("file not found")


# to removes folder
try:
    for i in range (1,101):
        os.rmdir(f"data/Day{i}/main.py")
        
except FileExistsError:
    print("file already exist")
except FileNotFoundError:
    print("file not found")


# Rename folder name
try:
    for i in range (1,101):
        os.rename(f"data/DAY {i}",f"data/day {i}")
except FileExistsError:
    print("file not found")
except FileNotFoundError:
    print("file not found")


# Delete a file
try:
    os.remove(f"data/day 1")
except FileNotFoundError:
    print("file not found ")
except:
    if PermissionError:
        os.rmdir(f"data/day 1")










