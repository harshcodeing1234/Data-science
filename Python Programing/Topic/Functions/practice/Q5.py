# Write a program to greet a user with “Good day” using functions.
import time
def greet():
    current_time = time.strftime('%H:%M %p')

    if current_time < "10:00 AM":
        print("Good day")
    else:
        print(current_time)

greet()
