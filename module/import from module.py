# we can also import the specific part of module instead of entire module
from MyModule import myList

# xyz = MyModule.myList  # wrong way
xyz = myList
print(xyz)
# Note: When importing using the from keyword, do not use the module name when referring to elements in the module.
# Example: person1["age"], not mymodule.person1["age"]
