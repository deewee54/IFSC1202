import math

class Triangle: 
    def __init__(self, s1, s2, s3):
        self.s1 = float(s1)
        self.s2 = float(s2)
        self.s3 = float(s3)

    def type(self):
        if self.s1 == self.s2 == self.s3:
            return "Equilateral"
        elif self.s1 == self.s2 or self.s2 == self.s3 or self.s1 == self.s3:
            return "Isoceles"
        else:
            return "Scalene"
        
    def perimeter(self):
        return self.s1 + self.s2 + self.s3
    
    def area(self):
        s = self.perimeter() / 2 
        return math.sqrt(s * (s - self.s1) * (s - self.s2) * (s - self.s3))
    
    def angles(self):
        a, b, c = self.s1, self.s2, self.s3 
        angle1 = math.acos((b**2 + c**2 - a**2) / (2 * b * c))
        angle2 = math.acos((a**2 + c**2 - b**2) / (2 * a * c))
        angle3 = math.acos((a**2 + b**2 - c**2) / (2 * a * b))
        return [math.degrees(angle1), math.degrees(angle2), math.degrees(angle3)]
    
TriangleList = []

with open("Exam Three Triangles.txt", "r") as file:
    for line in file: 
        sides = line.strip().split(",")
        triangle = Triangle(*sides)
        TriangleList.append(triangle)

print(f"{'Type':>12} {'Side 1':>10} {'Side 2':>10} {'Side 3':>10} {'Perimeter':>10} {'Area':>10} {'Angle 1':>10} {'Angle 2':>10} {'Angle 3':>10}")

for tri in TriangleList: 
    angles = tri.angles()
    print(f"{tri.type():>12} {tri.s1:10.3f} {tri.s2:10.3f} {tri.s3:10.3f} {tri.perimeter():10.3f} {tri.area():10.3f} {angles[0]:10.3f} {angles[1]:10.3f} {angles[2]:10.3f}")