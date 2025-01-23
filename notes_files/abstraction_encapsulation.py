#ABSTRACTION
class CAR:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False
    def start_car(self):
        self.clutch = True
        self.acc = True
        print("Your Car is started ... ")

car1 = CAR()
car1.start_car()
#here we dont see the objects assigning to true or false outside the class , we just start the car 
#and notice whether the car is started or not 


#Encapsulation
class Student:
    name = "mahan" #data
    def hello(self): #method
        print("hello")

s1 = Student()
print(s1.name)
s1.hello()

#here we are encapsuled the data and method in a class , this is called encapsulation 