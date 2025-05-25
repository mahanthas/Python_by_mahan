"""
Property Method ==> Decorator used to define a method as property
                    it can be accessed like an attribute
                Benefit: Add additional logic when read, write, or delete attributes
                gives you getter setter and deleter method

                this is used when we want to access the private attributes of class outside the class
"""

class Rectangle:
    def __init__(self, width, height):
        self._width=width
        self._height=height
 
    @property
    def width(self):
        return f"width is {self._width}cm"

    @property
    def height(self):
        return f"height is {self._height}cm"

    @width.setter
    def width(self,width):
        if(width > 0):
            self._width = width
        else:
            print(f"width cant be below 0")
    
    @height.setter
    def height(self,height):
        if(height > 0):
            self._height = height
        else:
            print(f"height cant be below 0")

rectangle1 = Rectangle(3, 4)

rectangle1.width = 10
rectangle1.height = -1

print(rectangle1.width)
print(rectangle1.height)


# def factorial(num):
#     if(num==0 or num==1):
#         fact = 1
#         return fact
#     fact = num * factorial(num -1)
#     return fact
    
# fact_value = factorial(5)
# print(fact_value)