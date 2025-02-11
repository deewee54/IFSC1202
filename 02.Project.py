import math 
from math import asin
from math import sin
from math import cos
from math import pi
print("Great Circle Calculator")
r = float(input("Enter Radius of Sphere: "))
y1 = float(input("Starting Point - Enter Latitude: "))
x1 = float(input("Starting Point - Enter Longitude: "))
y2 = float(input("Ending Point - Enter Latitude: "))
x2 = float(input("Ending Point - Enter Longitude: "))
x1 = x1 * pi / 180
x2 = x2 * pi / 180
y1 = y1 * pi / 180
y2 = y2 * pi / 180
sinx1 = sin(x1)
sinx2 = sin(x2)
cosx1 = cos(x1)
cosx2 = cos(x2)
cosy1y2 = cos(y1 - y2)
#print(x1,x2,y1,y2)
#print(sinx1,sinx2,cosx1,cosx2,cosy1y2)
first = sinx1 * sinx2
second = cosx1 * cosx2 * cosy1y2
arcsin = asin(first + second)
d = r * arcsin
d = round(d,2)
print("The Great Circle Distance is", d)

