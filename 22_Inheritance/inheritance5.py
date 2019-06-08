"""

Author: Kagaya john 
Tutorial 22 :   Inheritance

"""


"""

Add Properties
Example
Add a property called graduationyear to the Student class:
"""

class Person:
    def __init__(self, fname, lname):
     self.firstname = fname
     self.lastname = lname

    def printname(self):
     print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)
    self.graduationyear = 2019

x = Student("Mike", "Olsen")
print(x.graduationyear)
