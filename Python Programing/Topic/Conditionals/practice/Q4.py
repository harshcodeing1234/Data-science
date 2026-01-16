# Write a program which finds out whether a given name is present in a list or not.

name = input("Enter name ensure only first letter is captail:")

name_list = ['Harsh','Amit', 'Rahul', 'Navnit','Shali', 'Sakshi', 'kunal', 'Prakash', 'Abhishek']
if name in name_list:
    print("name is present in name_list")
else:
    print("name is not present in name_list")
