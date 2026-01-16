# Write a program to input eight numbers from the user and display all the unique numbers (once).
nums = input("Enter 8 num seprated by spaces:")
num_set = (map(int,nums.split()))

unique_num = set(num_set)
print(f"All numbers = {nums}")
print(f"uniaue number = {unique_num}")