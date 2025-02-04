#Create a base class Animal with subclasses Dog and Cat. Each subclass should have a speak() method.

class Complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img

    def show_number(self):
        print(f"{self.real} i + {self.img} j")

    def __add__(self,other):
        newreal = self.real + other.real
        newimg = self.img + other.img
        return Complex(newreal,newimg)

c1 = Complex(5,6)
c2 = Complex(3,2)
c1.show_number()
c2.show_number()
c3 = c2+c1
c3.show_number()