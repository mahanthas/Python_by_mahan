"""
Conditions: if, if-else, if-elif-else
        *if - is used to check whether the condition is true , if true then execute the program
        *if-else - used to check the condition, if condition is true execute if block and skip else part
                                              if condition is false skip if block and execute else part
        *if-elif-else - used to check many conditions , also called as nested if

Loops: for, while
        *for - is used execute the block for given number of times 
        *while - is used to for given number of times , but there should be condition statement inside the code
"""

a = 1234

if(a>1000):
    print(a)

if(a<1000):
    print("a is less than 1000")
elif(1001<a<2000):
    print("a is in between 1001 and 2000",a)
else:
    print("a is not an integer")

b = 0
while(b<10):
    print (b,end=" ")
    b = b + 1

c=5
for i in range(c):
    print(i * "*") 