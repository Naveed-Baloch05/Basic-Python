
'''Exercise 2:
Creating a Python program capable
 of greeting you with Good Morning, 
 Good Afternoon, and Good Evening.
Your program should use the time module 
to get the current hour.
'''


import time
# Get the current hour
current_hour = int(time.strftime('%H'))

# Decide greeting based on hour
if 0 <= current_hour < 12:
    print("Good Morning, Sir 🌅")
elif 12 <= current_hour <17 :
     print("Good Afternon, Sir ☀️")
else: 
     print("Good Evening, Sir 🌙")
          

