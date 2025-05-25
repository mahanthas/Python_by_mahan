import copy
lst1 = [[1, 2], [3, 4]]
lst2 = copy.copy(lst1)       # Shallow copy
lst3 = copy.deepcopy(lst1)

print(f"{lst2}")
print(f"{lst3}")

class Person:
    # name = ""
    # age = 0
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        print(f"name of persion is : {self.name} and age is {self.age}")

p1 = Person("mahan",26)
p1.display()