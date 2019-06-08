"""

Author: Kagaya john 
Tutorial 24 : Modules  

"""


"""
Use a Module
Now we can use the module we just created, by using the import statement:

Example
Import the module named mymodule, and call the greeting function:

"""


import mymodule

mymodule.greeting("Jonathan")


"""

Example
Import the module named mymodule, and access the person1 dictionary:

"""
a = mymodule.person1["age"]
print(a)

"""

Naming a Module
You can name the module file whatever you like, but it must have the file extension .py

Re-naming a Module
You can create an alias when you import a module, by using the as keyword:

"""

import mymodule as mx

a = mx.person1["age"]
print(a)



"""

Built-in Modules
There are several built-in modules in Python, which you can import whenever you like.

Example
Import and use the platform module:

"""

import platform

x = platform.system()
print(x)



"""


Using the dir() Function
There is a built-in function to list all the function names (or variable names) in a module. The dir() function:

Example
List all the defined names belonging to the platform module:

"""


import platform

x = dir(platform)
print(x)

"""

Import From Module
You can choose to import only parts from a module, by using the from keyword.

"""
from mymodule import person1

print (person1["age"])