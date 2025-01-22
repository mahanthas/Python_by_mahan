"""
    Write a Python program to calculate the area of a circle (ask the user for the radius).
    Write a Python program that prints all even numbers from 1 to 20.
"""
radius = int(input("Provide the radius of circle \n"))

PI = 3.145

def area_of_circle(radius):
    area = PI * radius * radius
    print(f"area of circle is: {area}")
    
area_of_circle(radius)

def print_even_number(number):
    for i in range(0,number):
        if(i%2 == 0):
            print(i)

print_even_number(radius)