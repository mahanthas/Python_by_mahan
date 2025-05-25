"""
    1. Write a function that takes a list of numbers and returns their sum using *args.
    2. Create a class Car with attributes brand and speed, and a method describe that returns the car details.    
"""
class Car:
    def __init__(self,brand,speed):
        self.brand = brand
        self.speed = speed

    def car_details(self):
        print(f"the car brand is {self.brand} and its speed is {self.speed}")

c1 = Car("Maruthi", 200)
c1.car_details()


def list_nums(*args):
    result = sum(args)
    print(result)

list1 = [1,2,3,5,10]
set1 = (9,10,9)
list_nums(*list1)
list_nums(*set1)
