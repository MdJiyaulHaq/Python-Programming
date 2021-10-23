f = open("demo.txt", "a")  # this will open the file in append mode
# f = open("demo.txt", "w")  # this will open the file in write mode
# remember: "w" mode will overwrite the existing content.

f.write("\nThis sentence was added by write mode.")
f.close()

f = open("demo.txt", "r")
print(f.read())

