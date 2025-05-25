"""
WAP prints the patterns 

1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""

def pattern1():
    for i in range(1,10):
        for j in range(1,i+1):
            print(j, end=" ")
        print("")
pattern1()

"""
1
2 3
4 5 6
7 8 9 10
11 12 13 14
"""
def pattern2():
    for i in range(1,15):
        