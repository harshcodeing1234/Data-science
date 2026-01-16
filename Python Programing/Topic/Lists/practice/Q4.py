# WAP to input a list of number and print longest and smallesrt number
num = input("Enter a list of numbers seprated by space:")
num_list = list(map(int,num.split()))
max = max(num_list)
min = min(num_list)
print("max number is",max)
print("min number is",min)
