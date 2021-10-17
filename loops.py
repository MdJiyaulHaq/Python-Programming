# else in a while statement
i = 5
while i < 9:
    print(i)
    i = i + 1
else:
    print("i is no longer less than 9")

# nested loop
# every fruit is healthy but cherry is not tasty to me
compliment = ["healthy", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in compliment:
    for y in fruits:
        if x == "tasty" and y == "cherry":
            break
        print(x, y)
