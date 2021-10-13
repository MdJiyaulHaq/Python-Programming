
# tuple with only 1 item is a bit trickier to define
tuple = ("Md")  # this is equal to  tuple= "md"  ie declaring string
print(tuple)
print(type(tuple))
# output is "str"

tuple = ("Md",)
print(tuple)
print(type(tuple))
# output is "tuple"


# tuple constructor is created as shown below.
myTuple = tuple(("Md", "is", "learning", "python", "from", "W3", "school"))  # constuctor defned
print(myTuple)

