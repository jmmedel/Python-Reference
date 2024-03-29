"""

Author: Kagaya john 
Tutorial 22 :   Inheritance

"""


"""
Example
Use the Student class to create an object, and then execute the printname method:
"""

class Person:
    def __init__(self, fname, lname):
     self.firstname = fname
     self.lastname = lname

    def printname(self):
     print(self.firstname, self.lastname)

class Student(Person):
  pass

x = Student("Mike", "Olsen")
x.printname()