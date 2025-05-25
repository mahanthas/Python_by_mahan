"""
WAP to print the pyramid of *

     *
    ***
   *****
    ***
     *

for 5 iterations
0 -> 4 spaces 1 star
1 -> 3 spaces 2 star 1 star
2 -> 2 spaces 3 star 2 star
3 -> 1 spaces 4 star 3 star
4 -> 0 spaces 5 star 4 star
"""

def print_half_pyramid(n):
    for i in range(n):
        for j in range(i,n):
            print(" ",end="")
        for j in range(i+1):
            print("*",end="")
        for j in range(i):
            print("*",end="")
        print("")

print_half_pyramid(5)

def print_full_pyramid(n):
    cnt = n//2
    scnt = 1
    for i in range(cnt+1):
        print(cnt*" " + "*"*scnt)
        scnt += 2
        cnt -= 1
    scnt = n - 2
    cnt = 1
    for i in range(n//2):
        print(cnt*" " + "*"*scnt)
        scnt -=2
        cnt +=1

    
print_full_pyramid(10)