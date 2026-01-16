# Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.

sub1 = float(input("Enter your first subject's mark :"))
sub2 = float(input("Enter your second subject's mark :"))
sub3 = float(input("Enter your third subject's mark :"))

total_marks = sub1 + sub2 + sub3
percentage = (total_marks / 300) * 100
print(percentage)

if (percentage >= 40) and (sub1 >= 33) and (sub2 > 33) and (sub3 > 33):
    print("You have passed the exam")
    print("your percentage is", percentage)
else:
    print("You have failed the exam")
    print("your percentage is", percentage)
