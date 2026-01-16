# WAP to input list of name and print longest name.
name = input("Enter a list of numbers seprated by space:")
name_list = list(map(str,name.split()))
longest_name = max(name_list)
print("longest name is", longest_name)
