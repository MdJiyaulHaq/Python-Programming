# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.
x = lambda a: a * 2
print(x(3))

# A lambda function can take any number of arguments
x = lambda l, b: l * b
print(x(2, 5))


# use the lambda function to make a function that always triples the number you send in:
def number(n):
    multiplier = lambda a: a * n
    return multiplier


multiplier = number(3)
print(multiplier(11))



# use the above function to calculate double and triple of a number you send in:
def number(n):
    return lambda a: a * n


double = number(2)
triple = number(3)
print(double(7))
print(triple(7))


