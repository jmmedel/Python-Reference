"""

Author: Kagaya john 
Tutorial 21 :   Classes Objects

"""

"""

Object Methods
Objects can also contain methods. Methods in objects are functions that belongs to the object.

Let us create a method in the Person class:

Example
Insert a function that prints a greeting, and execute it on the p1 object:

"""

class Person:
    def __init__(self, name, age):
     self.name = name
     self.age = age
    def myfunc(self):
     print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

"""
Note: The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
"""