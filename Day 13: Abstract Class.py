#Module of a language are the bone of it
#Importing Abstract method
from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author   
     #code to use abstract method
    @abstractmethod
    def display(): pass

#Write MyBook class
class MyBook(Book):
    def __init__(self, title, author, price):
        #you know this from the the past problem
        super().__init__(title, author)
        self.price = price
    def display(self):
        print ("Title: "+ self.title)
        print ("Author: "+ self.author)
        print ("Price:", self.price)
#function main
title=input()
author=input()
price=int(input())
new_novel=MyBook(title,author,price)
new_novel.display()
