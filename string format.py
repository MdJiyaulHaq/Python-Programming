# the below example is the formatted string
age1 = 21
age2 = 20
version = 2
str = "I am {} years old. I was {} years old in 2020. I want to buy FZ version {:.1f}"
print(str.format(age1, age2, version))

# to avoid absurd results, you can even put index into the curly braces
age1 = 21
age2 = 20
version = 2
str = "I am {2} years old. I was {0} years old in 2020. I want to buy FZ version {1:.1f}"
print(str.format(age2, version, age1))  # the index should follow the order of formatted one
# remember that same index can be used for any number of time

# even this is the right way
s = f"I am {age1} years old. I was {age2} years old in 2020. I want to buy FZ version {int(version):.1f} "
print(s.format(age1="21", age2="20", version="2"))  # the index should follow the order of formatted one
