
list1 = ["Md", "is", "learning", "python", "from", "W3", "school"]
list2 = ["He", "will", "complete", "it", "soon"]

# join the lists default method
list3 = list1+list2
print(list3)

# concatenate by iteration
for i in list2:
    list1.append(i)
print(list1)

# extend easiest method
list1.extend(list2)
print(list1)
