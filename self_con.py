"""
The Python default constructor is a simple constructor which
doesn’t accept any arguments. Its definition has only one
argument which is a reference to the instance being constructed.
"""
class Test:

    # default constructor
    def __init__(self):
        self.msg = "Default constructor"

    # a method for printing data members
    def display(self):
        print(self.msg)


# creating object
obj = Test()
obj.display()


#  Output:  Default constructor
