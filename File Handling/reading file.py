f = open("demo.txt", "r")

# if you want to read some specific part
print(f.read(7))  # reads from 0 to 6
f.close()

f = open("demo.txt", "r")

# if you want to read a line
print(f.readline())
print(f.readline())  # this prints another line
f.close()

f = open("demo.txt", "r")
# looping through line to the end of file
for i in f:
    print(i)
    