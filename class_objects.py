class Student:
    name = "Mahan"
    age = 26

s1 = Student()
print(s1.name,s1.age)

class Car:
    def __init__(self,carname,caryear): #here self is the keyword to define that it belongs to the class
        print("Car class constructor is called")
        self.name=carname
        self.year=caryear

c1 = Car("TATA",2019)
c2 = Car("AUDI",2020)
print(c1.name,c1.year)
print(c2.name,c2.year)