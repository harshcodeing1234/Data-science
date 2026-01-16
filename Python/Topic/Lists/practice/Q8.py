# WAP to input list of number and print even and odd number.
num = input("Enter a list of numbers seprated by space:")
num_list = list(map(int,num.split()))
for x in num_list:
	if x % 2 == 0:
		print("even")
	else:
		print("odd")
