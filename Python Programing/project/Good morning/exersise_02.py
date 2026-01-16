# create a python program to capable you with good morning, good afternoon, good evening and good night. your time module should use time module to get the current hour.



import time
timestamp = int(time.strftime("%H"))
# print("timestamp is", timestamp)
if timestamp < 12:
    print("Good Morning!")
elif timestamp > 12 and timestamp < 16:
    print("Good Afternoon!")
elif timestamp >16 and timestamp < 19: 
    print("Good Evening!")
else:
    print("Good Night!")