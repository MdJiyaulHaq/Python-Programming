#removing whitespaces from start and/or end of the string
string = "   We surely belong to Allah and to him we shall return. "
print(string.strip())


# splitting the strings into sub strings
string = "We surely belong to Allah and to him we shall return."
print(string.split())

# formatting string
year =2024
no_of_degrees = 2
work_at = "xyz company"
salary = 78600
string = "I will graduate from Pokhara University in {}. I will have {} degrees in my hand. After graduation i will work in {} with the minimum salary of Rs.{}"
print(string.format(year,no_of_degrees,work_at,salary))

# alternatively, if you want to format by index
no_of_degrees = 2
salary = 78600
year =2024
work_at = "xyz company"
string = "I will graduate from Pokhara University in {0}. I will have {2} degrees in my hand. After graduation i will work in {1} with the minimum salary of Rs.{3}"
print(string.format(year,work_at,no_of_degrees,salary))#index of formated values should be used. 
