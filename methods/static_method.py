"""
Create a Calculator class with static methods add(a, b), subtract(a, b), multiply(a, b), and divide(a, b).
"""

"""
static method ==> a method that actually belong to the class not to the object from that class

Best Utility functions that donot need access to class objects
"""

class Calculator:
    @staticmethod  
    def add(a,b):
        print(f"sum : {a+b}")

    @staticmethod
    def subtract(a,b):
        print(f"subtract : {a-b}")

    @staticmethod
    def multiply(a,b):
        print(f"multiply : {a*b}")

    @staticmethod
    def divide(a,b):
        print(f"division : {a/b}")

c1 = Calculator
c1.add(5,3)
c1.subtract(5,3)
c1.multiply(5,3)
c1.divide(6,3)

"""
Write a Utility class with a static method is_even(number) that checks if a number is even.
"""

class Utility:
    @staticmethod
    def is_even(a):
        if(a % 2 == 0):
            print(f"given number {a} is even")
        else:
            print(f"Given number {a} is odd")

Utility.is_even(8)
Utility.is_even(9)