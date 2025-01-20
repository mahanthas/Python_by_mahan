print("Hello World")

a = 12345
name = "Mahan"
is_genius = False

print(name)
print(float(a)) #explicit conversion 
print("mahan" + str(is_genius))

b = 1234
c = 17.589

sum = b+c  #implicit conversion  here python converts lower data type to larger data type
print((sum))

#Global variable, we take name as global variable here

def func():
    name = "swamy" # here we change the variable only inside this function
    print(name)
    
func()
print(f"name after calling the function :  {name}")

#if we want to change the global variable use the keyword global
def func1():
    global name
    name = "SWAMY"
    print(name)
    
func1()
print(f"name after calling the function with global variable : {name}")