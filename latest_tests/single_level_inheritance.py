class Animal:
    def __init__(self, breed, color):
        self.breed = breed
        self.color = color

    def animal_details(self):
        print(f"Animal breed is : {self.breed}")
        print(f"Animal color is : {self.color}")

class Dog(Animal):
    def __init__(self, name, breed, color):
        Animal.__init__(self, breed, color)
        self.name = name

    def dog_details(self):
        super().animal_details()
        print(f"the dog name is : {self.name}")

dog1 = Dog("jooly", "pamerian", "brown")

dog1.dog_details()