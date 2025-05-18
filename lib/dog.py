#!/usr/bin/env python3

class Dog:
    def __init__(self, name, breed="Mutt"):
        self.name = name
        self.breed = breed
    
    def print_self(self):
        print(f"Dog name is {self.name}")
        print(f"Dog breed is {self.breed}")

bosco = Dog("Bosco", "universal")

bosco.print_self()