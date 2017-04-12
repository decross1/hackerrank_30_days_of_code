## Hackerrank: Day 13 of 30 Days of Code
from abc import ABCMeta, abstractmethod


class Book:
    __metaclass__ = ABCMeta

    def __init__(self, title, author):
        self.title = title
        self.author = author

    @abstractmethod
    def display():
        pass

        # Write MyBook class


class MyBook(Book):
    def __init__(self, title, author, price):
        Book.__init__(self, title, author)
        self.price = str(price)

    def display(self):
        print("Title: " + self.title)
        print("Author: " + self.author)
        print("Price: " + self.price)


title = 'The Alchemist'
author = 'Paulo Coelho'
price = 248
new_novel = MyBook(title, author, price)
new_novel.display()