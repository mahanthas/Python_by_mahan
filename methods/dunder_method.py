"""
Create a Rectangle class with width and height attributes.
Override the __eq__() method to compare two rectangles by their area.
"""

class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def area_of_rectangle(self):
        area = self.width * self.height
        print(f"area of the given rectangle is {area}")
        return area

    def __eq__(self, other):
        if (self.area_of_rectangle() == other.area_of_rectangle()):
            print("rectangle areas are equal")
        else:
            print("rectangle areas are not equal")

r1 = Rectangle(10,20)
r2 = Rectangle(30,10)

r1 == r2

"""
Create a Fraction class with numerator and denominator attributes.
Override the __add__() method to add two fractions.
"""
class Fraction:
    def __init__(self,numerator,denominator):
        self.numerator = numerator
        self.denominator = denominator

    def show_fraction(self):
        print(f"{self.numerator} / {self.denominator}")

    def __add__(self,other):
        numer = self.numerator + other.numerator
        denom = self.denominator + other.denominator
        return Fraction(numer,denom)
    
f1 = Fraction(2,3)
f2 = Fraction(4,5)
f1.show_fraction()
f2.show_fraction()
f3 = f1 + f2
f3.show_fraction()