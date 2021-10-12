
# looping through the list using for loop
myList =[23, "Md", "python", True]
for i in myList:
    print(i)

# looping using index numbers
myList = [23, "Md", "python", True]
for i in range(len(myList)):
    print(myList[i])

# loop using while loop
myList = [23, "Md", "python", True]
i=0
while i < len(myList):
    print(myList[i])
    i=i+1

# comprensive looping
myList = [23, "Md", "python", True]
[print(i) for i in myList]
