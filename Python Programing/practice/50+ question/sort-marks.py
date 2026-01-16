# Write a program to accept marks of 6 students and display them in a sorted manner.
marks = input("Enter marks seprrated by spaces:")
marks_list = list(map(int,marks.split()))
print(f"marks = {marks_list}")