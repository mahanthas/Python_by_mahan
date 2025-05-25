#here child class inherits from more than one Parent Class

class A:
    def __init__(self, name):
        self.name = name

class B:
    def __init__(self, age):
        self.age = age

class C(B, A):
    def __init__(self, name, age, salary):
        A.__init__(self, name)
        B.__init__(self, age)
        self.salary = salary

    def details(self):
        print(f"name : {self.name}")
        print(f"age : {self.age}")
        print(f"salary : {self.salary}")

c1 = C("Mahan", 26, 20000)
c1.details()
