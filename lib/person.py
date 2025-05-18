#!/usr/bin/env python3

class Person:
    def __init__(self, name):
        self.name = name
        
    def print_details(self):
        print("My name is", self.name)
        

person1 = Person("Boru")
person1.print_details()