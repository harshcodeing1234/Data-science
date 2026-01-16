# Write a program to generate multiplication tables from 2 to 20 and write it to the
# different files. Place these files in a folder for a 13 – year old.

# with open("table.txt","a")as f:
#     num = int(input("enter the num:"))
#     print("table of",num)
#     f.write(f"Table of {num}\n")
#     for i in range(1,11):
#         f.write(f"{num}*{i}={num * i}\n")
#     f.write("\n")

def genratetable(n):
    table = ""
    for i in range(1,11):
        table+=f"{n}*{i}={n * i}\n"
    with open(f"table/table_{n}.txt","w")as f:
        f.write(table)
for i in range(2,21):
    genratetable(i)


