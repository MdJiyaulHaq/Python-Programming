# f = open("demo.txt")  # this line is same as the line below
f = open("demo.txt", "rt")  # r for read and t for text . which is default.
# Note: Make sure the file exists, or else you will get an error.
print(f.read())

# for a file on different location, full path should be mentioned.
f = open("/home/md/Desktop/Programming/Python-Programming/Python Try Except/text.txt", "r")
print(f.read())

# and don't forget to close the file
# because changes made to the file may not reflect before you close the line
f.close()
