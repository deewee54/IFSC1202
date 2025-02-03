classrooma = int(input("Enter Classroom A: "))
classroomb = int(input("Enter Classroom B: "))
classroomc = int(input("Enter Classroom C: "))
from math import ceil
classrooma = ceil(classrooma / 2)
classroomb = ceil(classroomb / 2)
classroomc = ceil(classroomc / 2)
total = classrooma + classroomb + classroomc
print(total)

