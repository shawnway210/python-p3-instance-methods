#!/usr/bin/env python3

class Dog:
    def __init__(self, name=""):
        self._name = name

    def sit(self):
        print("The dog is sitting.")

    def bark(self):
        print("Woof!")

my_dog = Dog("Fido")
my_dog.bark()

    
    
