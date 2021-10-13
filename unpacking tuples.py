
# when no. of variables matches the no. of items in the tuple
myTuple = ("Md", "is", "learning", "python", "from", "W3", "school")
(a, b, c, d, e, f, g) = myTuple
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)

# when no. of variables is less than the no. of items in the tuple
# and * is at the last, the remaining ie e  will form a list
myTuple = ("Md", "is", "learning", "python", "from", "W3", "school")
(a, b, c, d, *e) = myTuple
print(a)
print(b)
print(c)
print(d)
print(e)

# when no. of variables is less than the no. of items in the tuple
# and * is in the middle, the remaining ie b will form a list
myTuple = ("Md", "is", "learning", "python", "from", "W3", "school")
(a, *b, c, d, e) = myTuple
print(a)
print(b)
print(c)
print(d)
print(e)


