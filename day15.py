#Assignment practice program of if-else
# Compare the current time with different ranges
import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)

if( timestamp == '07:06:34'):
    print("Good Morning")
elif( '12:00:00' <= timestamp < '17:00:00'):
    print("Good Afternoon")
elif ('17:00:00' <= timestamp < '19:00:00'):
    print("Good Late Afternoon")
else:
    print("Good Evening")
