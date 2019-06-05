
"""
Python Conditions
Python Conditions and If statements
Python supports the usual logical conditions from mathematics:

Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b
These conditions can be used in several ways, most commonly in "if statements" and loops.

An "if statement" is written by using the if keyword.

Example
If statement:"""

a = 33
b = 200
if b > a: print("b is greater than a")

"""
In this example we use two variables, a and b, which are used as part of the if statement to test whether b is greater than a. As a is 33, and b is 200, we know that 200 is greater than 33, and so we print to screen that "b is greater than a"."""

"""
Indentation
Python relies on indentation, using whitespace, to define scope in the code. Other programming languages often use curly-brackets for this purpose."""

"""
Example
Statements on new lines MUST use indentations:"""

a = 33
b = 200
if b > a:
  print("b is greater than a")


  """Example
If statement, without indentation:

a = 33
b = 200
if b > a:
print("b is greater than a") # you will get an error"""


