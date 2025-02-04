#Create a Student class that stores a student's name and scores for three subjects.
#Write an instance method calculate_average() to calculate the average score.

class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def calculate_avg(self):  # this is an instance method 
        subjects = len(self.marks)
        avg = sum(self.marks)/subjects
        print(f"Average marks of the student {self.name} is {avg}")

s1 = Student("Mahan",[10,40,50])
s1.calculate_avg()

"""
Create a Book class that keeps track of the title and author.
Write an instance method display_info() to show book details.
"""

class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author

    def display_info(self):  #Instance method
        print(f"the Book Title is {self.title} and author is {self.author}")

b1 = Book("Where am i", "Mahan")
b1.display_info()