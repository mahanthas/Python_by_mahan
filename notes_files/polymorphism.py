#Polymorphism is mainly for operator overloading 
class Complex:
    def __init__(self,real,imag):
        self.real =real
        self.imag = imag

    def showNumber(self):
        print(self.real,"i +",self.imag,"j")

    def __add__(self,num2): #dunder function to do operator overload 
        newreal = self.real + num2.real
        newimag = self.imag + num2.imag
        return Complex(newreal,newimag)

    def __sub__(self,num2): #dunder function to do operator overload 
        newreal = self.real - num2.real
        newimag = self.imag - num2.imag
        return Complex(newreal,newimag)

num1 = Complex(1,5)
num2 = Complex(3,3)

num1.showNumber()
num2.showNumber()
num3 = num1 + num2
num3.showNumber()
num4 = num2 -num1
num4.showNumber()

a = 10
b=10
print(a+b)