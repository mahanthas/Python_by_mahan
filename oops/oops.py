#Create a Person class with attributes like name, age, and methods to display the person's details.

class Person:
    name = ""
    age = 0
    def __init__(self):
        pass

    def set_name(self,name,age):
        self.name = name
        self.age = age


    def display(self):
        print(f"the person name is : {self.name} and age {self.age}")

    def __add__(self,other):
        

#p1 = Person("Mahan",26)
p2 = Person()
p2.name = "Sharath"
p2.age = 30
p2.set_name(p2.name,p2.age)

#p1.display()
p2.display()