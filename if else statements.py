# normal way
a = 12
b = 30
if a < b:
    print("a is less than b")
else:
    print("a is greater than b")

# short hand
a = 12
b = 30
print("a is less than b") if a < b else print("a is greater than b")

# short hand for three conditions
a = 12
b = 30
print("a is less than b") if a < b else print("a is equal to b") if a == b else print("a is greater than b")

# if you have nothing to evaluate but also want to use if statement
# This is too funny but it is possible.
# note: this doesn't throw an error

a = 12
b = 30
if a == b:
    pass
else:
    pass
