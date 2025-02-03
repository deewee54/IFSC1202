''' SIMPLE CONDITIONAL
x = int(input("Enter a value: "))
if x > 0:
    print("Absolute value is",x)
else:
    print("Absolute value is",-x)'''

# Nested Conditionals Cordinate Plane
x = int(input("Enter X value: "))
y = int(input("Enter Y value: "))
if x > 0:
    if y > 0:
        # x is greater than 0, y is greater than 0
        print("Quadrant I")
    else:    
        # x is greater than 0, y is less or equal than 0
        print("Quadrant IV")
else:
    if y > 0:
        # x is less or equal than 0, y is greater than 0
        print("Quadrant II")
    else:    
        # x is less or equal than 0, y is less or equal than 0
        print("Quadrant III")