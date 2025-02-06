# Functions allow code reusability and modular programming.

#every function starts with def
def greet(name):
    print(f"Hello! {name}")
    
greet("Mahan")

#Functions can be parameterized with default value but which can be override
def sum(a, b=300):
    sum = a+b
    print(sum)
    
sum(20) # o/p : 320

sum(30,50) # o/p : 80

#