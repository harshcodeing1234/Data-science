# WAP to input a list of number and print the square of each number.
num = input("Enter a list of numbers seprated by space:")
num_list = list(map(int,num.split()))
square = [x**2 for x in num_list]
print("square is", square)
