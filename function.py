# defining a function
def greet(name="Guest"):
    print("hello " + name)  # calling the function


greet("Md")


# greet()  # this will throw an error .

# To avoid this error, default value should be passed while defining the function


# defining another function
def area(l, b):
    return l * b
    print("This line never gonna execute because of the return.")


print(area(3, 4))  # calling the function

# error handling
# try and except

try:
    age = input("enter your age: ")
    salary = input("enter your salary:")
    print(int(age))
    print(int(salary))
    ratio = int(salary) / int(age)
except ZeroDivisionError:
    print("age cannot be 0.")
except ValueError:
    print("invalid input.")


# arbitrary argument
# when you don't know how many args you are going to pass
def greet(*names):
    print("hello " + names[3])  # calling the function


print("Md", "Harry", "Arjun", "Shankar")


# arbitrary keyword argument
def greet(name1, name2, name3, name4):
    print("hello " + name4)  # calling the function


greet(name4="Md", name2="Harry", name3="Arjun", name1="Shankar")


# passing list as an argument into the function
def greet(name):
    for x in name:
        print("hello " + x)  # calling the function


names = ["Md", "Harry", "Arjun", "Shankar"]
greet(names)

# recursive function
factorial = 1
print("What factorial do you want to calculate:")
n = int(input())
for i in range(n):
    factorial = factorial * (i + 1)

print(f"factorial of {n} is {factorial}:")
