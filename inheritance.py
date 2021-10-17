# parent class definition
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
    def __init__(self, profession):
        self.profession = profession

    def printprofession(self):
        print("Software engineers knows Python programming")


s1 = Software("Python")
s1.printprofession()
