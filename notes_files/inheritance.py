# Single level Inheritance
class Car:
    @staticmethod
    def start():
        print("Car started")
    @staticmethod
    def stop():
        print("car stopped")

class Toyotacar(Car):
    def __init__(self,name):
        self.name = name

c1 = Toyotacar("Innova")
c1.start()
print(c1.name)
c1.stop()

# Multi-level Inheritance
class Fortuner(Toyotacar):
    def __inti__(self,type):
        self.type = type

class Innova(Fortuner):
    def __init__(self,color):
        self.color = color

innova1 = Innova("black")
innova1.name = "Etios"
print(innova1.name,innova1.color)

fr = Fortuner("electric")
fr.type = "Prius"
print(fr.name,fr.type)

# Multiple Inheritance
class Carcost():
    def __init__(self,cost):
        self.cost = cost 

    def add_fuel(self,fuel):
        self.fuel = fuel
        print(self.fuel," Fuel has been added to car")

class Priuscar(Car,Carcost):
    def __init__(self, model):
        self.model = model

pc = Priuscar("1999")
pc.cost = 250000
pc.start()
print(pc.model,pc.cost)
pc.stop()

# Super Method
class Owncar(Carcost):
    def __init__(self,owner,cost):
        self.owner = owner
        super().__init__(cost)

own = Owncar("Mahan",250000000)
print(own.cost)