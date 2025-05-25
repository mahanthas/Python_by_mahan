# program to write the pattern of stars 
"""
*****
 *** 
  *
"""

def pattern_triangle(num):
    for i in range(1, num+1):
        for j in range(1, i):
            print("*",end=" ")
        print()

def reverse_triangle(num):
    for i in range(num, 0, -1):
        # for j in range(i):
        print("*" * i)
    print()

def middle_triangle(num):
    for i in range(num,0,-2):
        for j in range(i):
            print("*",end=" ")
        print()

#middle_triangle(5)
reverse_triangle(5)
#pattern_triangle(5)

