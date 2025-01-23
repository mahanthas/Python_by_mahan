class Mahan:
    def __init__(self,name,age):
        self.name = name
        self.age = age

m1 = Mahan("mahan",26)
m2 = Mahan("mahan",26)
del m1.name
del m1
#print(m1.age)
print(m2.name,m2.age)


class Car:
    __model = "sedan"

    def __cartype(self,type):
        self.type == type
        print("car type is ",self.type)

    def cardetails(self,name,cost,type):
        self.name = name
        self.cost = cost
        self.type = type
        print(self.name)
        print(self.cost)
        self.__cartype(self.type)

c1 = Car()
"""
print(c1.__model) # will throw error
c1.__cartype() # will throw error as we are trying to acces private member of class
"""
print(c1.cardetails("audi",2500000,"sedan"))