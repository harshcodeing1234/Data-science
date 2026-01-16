# 4. Write a program to sum a list with 4 numbers.
num = input("Enter num:")
sum_list = list(map(int,num.split()))

print(f"sum of list = {sum(sum_list)}")