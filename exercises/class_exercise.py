"""
    Questions:
            1. Create student class that takes name & marks of 3 subjects as arguments in constructor.
                Then create a method to print the average.
"""

#Question 1
class Student:
    def __init__(self,name,marks_list):
        self.name = name
        self.marks_list = marks_list

    def average(self):
        sum = 0
        for i in self.marks_list:
            sum += i
        print(f"student {self.name} average score is {sum/len(self.marks_list)} ")

s1 = Student("Mahan",[90,99,89])
s1.average()
