"""

Author: Kagaya john 
Tutorial 22 :   Iterators

"""


"""
Example
Strings are also iterable objects, containing a sequence of characters:
"""

mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))