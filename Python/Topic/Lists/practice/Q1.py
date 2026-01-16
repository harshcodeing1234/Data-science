# WAP to input list and print the average
num = input("Enter a list of numbers seprated by space:")
num_list = list(map(int,num.split()))
avrage = sum(num_list)/len(num_list)
print("average is",avrage)
