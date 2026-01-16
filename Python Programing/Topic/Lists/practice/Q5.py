# WAP to accept marks of 6 students and display them in a stored manner.
marks = input("Enter marks seprated by space:")
marks_list = list(map(int,marks.split()))
print(f"marks of 6 student is {marks_list}")
