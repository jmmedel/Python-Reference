"""

Author: Kagaya john 
Tutorial 22 :   Inheritance

"""




"""
In the example below, the year 2019 should be a variable, and passed into the Student class when creating student objects. To do so, add another parameter in the __init__() function:

Example
Add a year parameter, and pass the correct year when creating objects:
"""
class Person:
    def __init__(self, fname, lname):
     self.firstname = fname
     self.lastname = lname

    def printname(self):
     print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    Person.__init__(self, fname, lname)
    self.graduationyear = year

x = Student("Mike", "Olsen", 2019)
print(x.graduationyear)