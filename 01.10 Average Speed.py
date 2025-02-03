length = int(input("Enter Length of Race in Kilometers: "))
minutes = int(input("Enter Minutes: "))
seconds = int(input("Enter Seconds: "))
miles  = length / 1.61
seconds = seconds / 60
hour = seconds + minutes / 60
mph = miles / hour
print(mph)