"""
    Questions:
            1. Define a circle class to create with radius r using the constructor.
                define an Area() method of the class which calculates the area of the circle.
                define a perimeter() method of the class which allows you to calculate the perimeter of the circle.

            2. Define a Employee class with attributes role,department and salary.This class also have the 
                showDetails() method.
                Create an Engineer class that inherits properties from Employee and has additional attributes:
                name and age

            3. Create a class called Oder which stores item and its price.
                use Dunder function __gt__() to convey that:
                order1 > order2 if price of order1 > price of order2

"""

#Question 1
PI = 3.145
class Circle:
    def __init__(self,radius):
        self.radius = radius

    def Area(self):
        area = (PI * self.radius * self.radius)
        return area
    
    def perimeter(self):
        perimeter = (2 * PI * self.radius)
        return perimeter
    
c1 = Circle(20)
print(c1.Area())
print(c1.perimeter())


#Question 2
class Employee:
    def __init__(self,role,department,salary):
        self.role = role
        self.department = department
        self.salary = salary

    def showDetails(self):
        print("Employee role is ",self.role,"and department is ",self.department,"and salary is ",self.salary)

class Engineer(Employee):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        super().__init__("Engineer","AIP1",2600000)


emp1 = Engineer("Mahan",26)
# emp1.role = "Engineer"
# emp1.department = "AIP1"
# emp1.salary = 2600000
emp1.showDetails()

#Question 3 
class Order:
    def __init__(self,item,price):
        self.item = item
        self.price = price

    def __gt__(self,ord2):
        if(self.price > ord2.price):
            print(self.item ," > ", ord2.item)
        else:
            print(ord2.item ," > ", self.item)
ord1 = Order("sugar", 45)
ord2 = Order("tea",60)

ord1>ord2