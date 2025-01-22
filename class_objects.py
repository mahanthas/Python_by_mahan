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

class office:
    dept = "AIP"
    def __init__(self,name,salary):
        print("Office class constructor")
        self.name = name;
        self.salary = salary;

c1 = office("mahan",250000)
c2 = office("praveen",300000)

print(f"name of collegue {c1.name} and salary is {c1.salary} belongs to dept {office.dept}")
print(f"name of collegue {c2.name} and salary is {c2.salary} belongs to dept {c2.dept}")
#here s1.name and s1.salary are object attributes as it will be differnt for each objects
# where as dept is an class attribute as it same for all the objects
# obj.attr  >>>> class.attr

