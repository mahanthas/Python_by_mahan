class CAR:
    def __init__(self, name, year, color):
        self.name = name
        self.year = year
        self.color = color
        
    def car_details(self):
        print(f"the name of car is: {self.name}\n")
        print(f"the year of manufacture is : {self.year}\n")
        print(f"the color of car is : {self.color}\n")
        
car1 = CAR("cheverlot", 2015, "White")

car1.car_details()