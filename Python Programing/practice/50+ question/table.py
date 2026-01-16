n = int(input("Enter num:"))

print(f"table of {n}")
for i in range(1,51):
    table = f"{n}*{i} = {n*i}"
    print(table)


with open(f"table.txt",'a+') as f:
        f.write(f"table of {n}\n:{table}")
        

