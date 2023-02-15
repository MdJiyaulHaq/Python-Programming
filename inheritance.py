# # parent class definition
# class Engineer:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname
#
#     def printname(self):
#         print(self.firstname, self.lastname)
#
#
# e1 = Engineer("Muhammad", "Ali")
# e1.printname()
#
#
# # child class
# class Software(Engineer):
#     def __init__(self, fname, lname, profession):  # the moment you call __init__ function in the child class,
#         # the __init__of parent class is not derived'''
#         self.profession = profession
#         self.firstname = fname
#         self.lastname = lname
#
#     def professionalisation(self):
#         print(self.firstname, self.lastname, self.profession)
#
#
# s1 = Software("Programmer", "Boy", "Python")
# s1.professionalisation()





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
    # To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:
    def __init__(self, fname, lname):
        Engineer.__init__(self, fname, lname)  # that's it, too simple


s1 = Software("Programmer", "Boy")
s1.printname()
