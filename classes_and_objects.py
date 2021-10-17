# defining a class
class MyClass:
    a = 3


obj1 = MyClass()
print(obj1.a)


# defining a class and using init function to initialise the name and id
class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id


employee1 = Employee("HariOm", 3922)
# Note: The __init__() function is called automatically every time the class is being used to create a new object.
print(employee1.name)
print(employee1.id)


# object methods
# self parameter is not compulsory. we can use any thing at that place
class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def greet(self):
        print("hello Mr." + self.name)


employee1 = Employee("HariOm", 3922)
employee1.greet()


# an object or its properties using del keyword
class Emp:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def greet(self):
        print("hello Mr." + self.name)


del Employee.id
del Emp
employee1 = Emp("HariOm", 3922)
employee1.greet()
