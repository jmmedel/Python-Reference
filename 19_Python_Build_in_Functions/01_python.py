"""

Author: Kagaya john 
Tutorial 19 :  build in Function  

"""

"""
Python Built in Functions
Python has a set of built-in functions.

Function	Description
abs()	Returns the absolute value of a number
all()	Returns True if all items in an iterable object are true
any()	Returns True if any item in an iterable object is true
ascii()	Returns a readable version of an object. Replaces none-ascii characters with escape character
bin()	Returns the binary version of a number
bool()	Returns the boolean value of the specified object
bytearray()	Returns an array of bytes
bytes()	Returns a bytes object
callable()	Returns True if the specified object is callable, otherwise False
chr()	Returns a character from the specified Unicode code.
classmethod()	Converts a method into a class method
compile()	Returns the specified source as an object, ready to be executed
complex()	Returns a complex number
delattr()	Deletes the specified attribute (property or method) from the specified object
dict()	Returns a dictionary (Array)
dir()	Returns a list of the specified object's properties and methods
divmod()	Returns the quotient and the remainder when argument1 is divided by argument2
enumerate()	Takes a collection (e.g a tuple) and returns it as an enumerate object
eval()	Evaluates and executes an expression
exec()	Executes the specified code (or object)
filter()	Use a filter function to exclude items in an iterable object
float()	Returns a floating point number
format()	Formats a specified value
frozenset()	Returns a frozenset object
getattr()	Returns the value of the specified attribute (property or method)
globals()	Returns the current global symbol table as a dictionary
hasattr()	Returns True if the specified object has the specified attribute (property/method)
hash()	Returns the hash value of a specified object
help()	Executes the built-in help system
hex()	Converts a number into a hexadecimal value
id()	Returns the id of an object
input()	Allowing user input
int()	Returns an integer number
isinstance()	Returns True if a specified object is an instance of a specified object
issubclass()	Returns True if a specified class is a subclass of a specified object
iter()	Returns an iterator object
len()	Returns the length of an object
list()	Returns a list
locals()	Returns an updated dictionary of the current local symbol table
map()	Returns the specified iterator with the specified function applied to each item
max()	Returns the largest item in an iterable
memoryview()	Returns a memory view object
min()	Returns the smallest item in an iterable
next()	Goes to the next item in an iterable
object()	Returns a new object
oct()	Converts a number into an octal
open()	Opens a file and returns a file object
ord()	Convert an integer representing the unicode of the specified character
pow()	Returns the value of x to the power of y
print()	Prints to the standard output device
property()	Gets, sets, deletes a property
range()	Returns a sequence of numbers, starting from 0 and increments by 1 (by default)
repr()	Returns a readable version of an object
reversed()	Returns a reversed iterator
round()	Rounds a numbers
set()	Returns a new set object
setattr()	Sets an attribute (property/method) of an object
slice()	Returns a slice object
sorted()	Returns a sorted list
@staticmethod()	Converts a method into a static method
str()	Returns a string object
sum()	Sums the items of an iterator
tuple()	Returns a tuple
type()	Returns the type of an object
vars()	Returns the __dict__ peroperty of an object
zip()	Returns an iterator, from two or more iterators"""



x = abs(-7.25)

mylist = [True, True, True]
x = all(mylist)

mylist = [False, True, False]
x = any(mylist)

x = ascii("My name is Ståle")

x = bin(36)

x = bool(1)

x = bytearray(4)

x = bytes(4)

def x():
      a = 5

print(callable(x))

x = chr(97)

x = compile('print(55)', 'test', 'eval')
exec(x)

x = complex(3, 5)

class Person:
  name = "John"
  age = 36
  country = "Norway"

delattr(Person, 'age')

x = dict(name = "John", age = 36, country = "Norway")


class Person:
  name = "John"
  age = 36
  country = "Norway"

print(dir(Person))

x = divmod(5, 2)


x = ('apple', 'banana', 'cherry')
y = enumerate(x)

x = 'print(55)'
eval(x)

x = 'name = "John"\nprint(name)'
exec(x)


ages = [5, 12, 17, 18, 24, 32]

def myFunc(x):
  if x < 18:
    return False
  else:
    return True

adults = filter(myFunc, ages)

for x in adults:
  print(x)

x = float(3)

x = format(0.5, '%')

mylist = ['apple', 'banana', 'cherry']
x = frozenset(mylist)


class Person:
  name = "John"
  age = 36
  country = "Norway"

x = getattr(Person, 'age')


x = globals()
print(x)




class Person:
  name = "John"
  age = 36
  country = "Norway"

x = hasattr(Person, 'age')

x = hex(255)

x = ('apple', 'banana', 'cherry')
y = id(x)


print('Enter your name:')
x = input()
print('Hello, ' + x)

x = int(3.5)

x = isinstance(5, int)


class myAge:
      age = 36

class myObj(myAge):
  name = "John"
  age = myAge

x = issubclass(myObj, myAge)

x = iter(["apple", "banana", "cherry"])
print(next(x))
print(next(x))
print(next(x))

mylist = ["apple", "banana", "cherry"]
x = len(mylist)

x = list(('apple', 'banana', 'cherry'))

x = locals()
print(x)


def myfunc(n):
      return len(n)

x = map(myfunc, ('apple', 'banana', 'cherry'))

x = max(5, 10)


x = memoryview(b"Hello")

print(x)

#return the Unicode of the first character
print(x[0])

#return the Unicode of the second character
print(x[1])

x = min(5, 10)

mylist = iter(["apple", "banana", "cherry"])
x = next(mylist)
print(x)
x = next(mylist)
print(x)
x = next(mylist)
print(x)

x = object()

x = oct(12)

f = open("demofile.txt", "r")
print(f.read())

x = ord("h")

x = pow(4, 3)

print("Hello World")

x = range(6)
for n in x:
  print(n)

alph = ["a", "b", "c", "d"]
ralph = reversed(alph)
for x in ralph:
  print(x)

x = round(5.76543, 2)
print(x)

x = set(('apple', 'banana', 'cherry'))

class Person:
  name = "John"
  age = 36
  country = "Norway"

setattr(Person, 'age', 40)


a = ("a", "b", "c", "d", "e", "f", "g", "h")
x = slice(2)
print(a[x])

a = ("b", "g", "a", "d", "f", "c", "h", "e")
x = sorted(a)
print(x)

x = str(3.5)


a = (1, 2, 3, 4, 5)
x = sum(a)

x = tuple(('apple', 'banana', 'cherry'))


a = ('apple', 'banana', 'cherry')
b = "Hello World"
c = 33

x = type(a)
y = type(b)
z = type(c)

class Person:
  name = "John"
  age = 36
  country = "norway"

x = vars(Person)

a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica")

x = zip(a, b)
