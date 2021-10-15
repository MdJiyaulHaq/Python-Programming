
# sort the list into descending order
myList = ["Md", "is", "learning", "python", "from", "W3", "school"]
myList.sort(reverse=True)
print(myList)
# this gives an absurd sorting because the sort method is case sensitive.

# case insensitive sorting the list into descending order
myList = ["Md", "is", "learning", "python", "from", "W3", "school"]
myList.sort(reverse=True, key=str.lower)
print(myList)

