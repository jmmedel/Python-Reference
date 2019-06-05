"""

Author: Kagaya john 
Tutorial 2 :  Variables
 
"""

"""
Creating Variables
Unlike other programming languages, Python has no command for declaring a variable.

A variable is created the moment you first assign a value to it.
"""

x = 5
y = "John"
print(x)
print(y)

#Variables do not need to be declared with any particular type and can even change type after they have been set.

x = 4 # x is of type int
x = "Sally" # x is now of type str
print(x)

"""
Variable Names
A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)

"""


"""
Output Variables
The Python print statement is often used to output variables.

To combine both text and a variable, Python uses the + character:

"""

x = "awesome"
print("Python is " + x)


#You can also use the + character to add a variable to another variable:
x = "Python is "
y = "awesome"
z =  x + y
print(z)

#For numbers, the + character works as a mathematical operator:
x = 5
y = 10
print(x + y)
