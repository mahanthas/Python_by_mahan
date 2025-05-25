"""
Create a Book class with title, author, and price attributes. 
Write a class method from_string(cls, book_str) that accepts a string like "Harry Potter;J.K. Rowling;499" 
and creates a Book object.
"""

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = int(price)

    @classmethod
    def from_string(cls,book_str):
        title, author, price = book_str.split(',')
        return cls(title,author,price)

book1 = Book("mahan", "j.k rowling", 500)

book2 = Book.from_string("hello,mahan, 600")

print(book2.title, book2.author, book2.price)