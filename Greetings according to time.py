a="#Programme name=Good morning sir!#"
print(a.center(50))
import time
timestamp = time.strftime("%H:%M:%S", time.localtime())
if timestamp < "12:00:00":
    print("Good morning sir!")
elif timestamp < "18:00:00":
    print("Good afternoon sir!")
else:
    print("Good evening sir!")