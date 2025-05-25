"""
Decorator ==> A function that extends the behaviour of another function
              without modifing the base function
              pass the base function as an argument to decorator
            
            adding some more functionality without changeing base function
            ex: @add_sprinkels
                get_icecream(vanilla)
"""
def add_sprinkels(func):
    def wrapper(*args, **kwargs):
        print("** added sprinkels **")
        func(*args, **kwargs)
    return wrapper

@add_sprinkels
def get_icecream(flavor):
    print(f"here is your {flavor} icecream ")

get_icecream("vanilla")P