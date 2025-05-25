""" 
Create a Circle class with a class attribute pi = 3.14. Write a class method set_pi() to change the value of pi.
"""

"""
Class method ==> the method where you change the values for class variables without using the class objects
"""

class Circle:
    pi = 3.142
    def __init__(self,radius):
        self.radius = radius

    def area_of_circle(self):
        area = (self.pi) * (self.radius ** 2)
        print (f"area of the circle is {area}")

    @classmethod
    def set_pi(cls,value):
        cls.pi = value
        print(f"value of pi is {cls.pi}")

c1 = Circle(5)
c1.set_pi(3)
c1.area_of_circle()