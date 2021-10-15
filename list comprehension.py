# using list comprehension creating a list having olny string in mylist
myList = ["Md", "is", "learning", "python", "from", "W3", "school"]
newList = []
newlist = [x for x in myList if "o" in x]  # newlist = [expression for item in iterable if condition == True]
print(newlist)
