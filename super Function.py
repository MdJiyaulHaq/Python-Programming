class Engineer:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


e1 = Engineer("Muhammad", "Ali")
e1.printname()


# child class
class Software(Engineer):
    def __init__(self, fname, lname, year):
        # super function inherits all the functions of the parent class
        super().__init__(self, fname, lname)
        self.gradyear = year
        # we can directly insert another property to the class student

    def printsoftware(self):
        print(self.firstname, self.lastname, self.gradyear)


s1 = Software("Programmer", "Boy", 2024)
s1.printname()
s1.printsoftware()
