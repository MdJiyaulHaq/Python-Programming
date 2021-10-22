import json

# Parse JSON - Convert from JSON to Python

student = '{"name":"Md","study":"Pokhara University","gpa":"3.02"}'
s = json.loads(student)
print(s["gpa"])  # this is converted to a python dict.

# convert back to json
t = json.dumps(s)
print(t)

# You can convert Python objects of the following types, into JSON strings:
#
print(json.dumps({"name": "Md", "study": "Pokhara University", "gpa": "3.02"}))  # dict
print(json.dumps(["apple", "orange", "lemon"]))  # list
print(json.dumps((3, 7)))  # tuple
print(json.dumps("My name is Md"))  # string
print(json.dumps(786))  # int
print(json.dumps(786.92))  # float
print(json.dumps(True))  # True
print(json.dumps(False))  # False
print(json.dumps(None))  # None


"""
When you convert from Python to JSON, Python objects are converted into the JSON (JavaScript) equivalent:
Python 	JSON
dict 	Object
list 	Array
tuple 	Array
str 	String
int 	Number
float 	Number
True 	true
False 	false
None 	null
"""


