# Creating an iterator that will iterate from 1 to 5
class Numbers:
    def __init__(self):
        self.a = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.a <= 5:
            x = self.a
            self.a = self.a + 1
            return x
        else:
            raise StopIteration


MyNum = Numbers()

# one way of printing the values
print(next(MyNum))
print(next(MyNum))
print(next(MyNum))

# the other way of printing the values
for i in MyNum:
    print(i)
