print("First Timestamp")
firsthour = int(input("Enter Hours: "))
firstminutes = int(input("Enter Minutes: "))
firstseconds = int(input("Enter Seconds: "))
print("Second Timestamp")
secondhour = int(input("Enter Hours: "))
secondminutes = int(input("Enter Minutes: "))
secondseconds = int(input("Enter Seconds: "))
firsthour = firsthour * 3600
firstminutes = firstminutes * 60
firsttimestamp = firsthour + firstminutes + firstseconds
secondhour = secondhour * 3600
secondminutes = secondminutes * 60
secondtimestamp = secondhour + secondminutes + secondseconds
answer  = secondtimestamp - firsttimestamp
print(answer)