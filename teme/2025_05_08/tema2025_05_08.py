
# Sa se defineasca clasa Circle cu proprietatea radius, si metodele circumferences, area.
# Sa se defineasca clasa Rectangle cu proprietatile l1, l2, si metodele circumferences, area.
# Sa se defineasca clasa Triangle cu proprietatile l1, l2, l3, si metodele circumferences, area.

# Formula of Heron's formula is used to find the area of a triangle when the lengths of all three sides are known. The formula is given by:
#
# $$ \text{Area} = \sqrt{s(s-a)(s-b)(s-c)} $$
#
# where s is the semi-perimeter of the triangle, calculated as:
# $$ s = \frac{a + b + c}{2} $$
# Here, a, b, and c are the lengths of the sides of the triangle.
# This formula was derived by Heron of Alexandria around 62 CE.

import math

class Circle:

    def __init__(self, radius):
        self.radius = radius

    def circumferences(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * self.radius * self.radius

class Rectangle:

    def __init__(self, l1, l2):
        self.l1 = l1
        self.l2 = l2

    def circumferences(self):
        return 2 * (self.l1 + self.l2)

    def area(self):
        return self.l1 * self.l2

class Triangle:

    def __init__(self, l1, l2, l3):
        self.l1 = l1
        self.l2 = l2
        self.l3 = l3

    def circumferences(self):
        return self.l1 + self.l2 + self.l3

    def area(self):
        self.s = self.circumferences()/2
        self.area = math.sqrt(self.s * (self.s - self.l1) * (self.s - self.l2) * (self.s - self.l3))
        return self.area

print("\nTestare clasa Circle:")
radius = float(input("Raza cercului tău: "))
myCircle = Circle(radius)
print(f"Circumferința cercului este: {myCircle.circumferences()}.")
print(f"Aria cercului este: {myCircle.area()}.")

print("\nTestare clasa Rectangle:")
l1R = float(input("O latură a dreptunghiului tău: "))
l2R = float(input("Cealaltă latură a dreptunghiului tău: "))
myRectangle = Rectangle(l1R, l2R)
print(f"Circumferința dreptunghiului este: {myRectangle.circumferences()}.")
print(f"Aria dreptunghiului este: {myRectangle.area()}.")

print("\nTestare clasa Triangle:")
l1T = float(input("Prima latură a triunghiului tău: "))
l2T = float(input("A doua latură a triunghiului tău: "))
l3T = float(input("A treia latură a triunghiului tău: "))
if ( l1T + l2T > l3T and l1T + l3T > l2T and l2T + l3T > l1T):
    myTriangle = Triangle(l1T, l2T, l3T)
    print(f"Circumferința triunghiului este: {myTriangle.circumferences()}.")
    print(f"Aria triunghiului este: {myTriangle.area()}.")
else:
    print("Cele 3 numere nu pot forma laturile unui triunghi!")
