def sum(a,b):  #user-defined function
    print(a+b)  # builtin function 

sum(10,12)
sum(15,17)
sum(20,18)

add = lambda a,b:a+b  #lambda functions
print(add(9,8),end=" ")

#recursive functions
def factorial(n):
    if(n==0):
        return 1
    fact = n * factorial(n-1) #here we call function inside function
    return fact

print("\n",factorial(6))

#Generator Functions
def generate_squares(n):
    for i in range(n+1):
        squares = i*i
        yield squares

for num in generate_squares(10):
    print(num)

#Decorator Functions
def decorator(func):
    def wrapper(args):
        print("i am decorator")
        func(args)
        print("End of decorator")
    return wrapper

@decorator
def greet(name):
    print(f"Hi {name} Good Morning!!")

greet("mahan")