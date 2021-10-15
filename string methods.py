string = "we surely belong to Allah and to him we shall return"
print(string.capitalize())  # capitalize first character of string
print(string.upper())  # upper case all character of string
print(string.lower())  # lower case all character of string
print(string.casefold())  # lower case all character of string
print(string.center(120))  # moves the string to the right by 120 px
print(string.center(120, "*"))
# moves the string to the right by 120 px and fill the empty space by the character you provide
print(string.count("allah", 0, 20))
# counts the no. of times "Allah" appears in the string. NOte: case sensitive, returns 0 for allah. searches from
# index 0 to 20

price = 34
apple = "buy an apple for only {price:.4f} rupees."
print(apple.format(
    price=35))  # Insert the price inside the placeholder, the price should be in fixed point, two-decimal format:

# there are many more methods in python , we will learn and use it later.
