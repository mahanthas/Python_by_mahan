"""
WAP to write a decorator function
"""

def greet(func):
    def wrapper():
        print("Hello, Good Morning!")
        func()
    return wrapper

@greet
def name():
    print("Mahan")

name()

