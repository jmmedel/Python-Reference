"""

Author: Kagaya john 
Tutorial 26 :  JSON

"""

"""

You can convert Python objects of the following types, into JSON strings:

dict
list
tuple
string
int
float
True
False
None
Example
Convert Python objects into JSON strings, and print the values:

"""

import json

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))
