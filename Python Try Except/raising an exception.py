a = int(input("input a number:"))
b = int(input("input a divisor:"))
print(a)
print(b)
if b == 0:
    raise Exception("Divisible by 0 is not allowed.")
else:
    result = a / b
    print(result)

hello = "Md"
if type(hello) is str:
    raise TypeError("sorry! only integers allowed.")
