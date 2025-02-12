import math 
from math import acos
from math import sin
from math import cos
from math import pi
print("Great Circle Calculator")
r = float(input("Enter Radius of Sphere: "))
x1 = float(input("Starting Point - Enter Latitude: ")) * pi /180.0
y1 = float(input("Starting Point - Enter Longitude: ")) * pi /180.0
x2 = float(input("Ending Point - Enter Latitude: ")) * pi /180.0
y2 = float(input("Ending Point - Enter Longitude: ")) * pi /180.0
d = r * acos(sin(x1)*sin(x2)+cos(x1)*cos(x2)*cos(y1-y2))
print("The Great Circle Distance is", d)

