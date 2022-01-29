'''
super() keyword in Inheritance
when we create an object for the child class, if that class have (explicit) init constructor, it calls
child class init automatically...
If init is not there in child class, then it prints the parent class constructor
If both the classes have init constructors then we have to give super() keyword to call the parent class init

'''

class A:

    def __init__(self):
        print("In parent class init")

    def feature1(self):
        print("Parent feature1")

class B(A):

    def __init__(self):
        super().__init__() # If init is present in both the classes, then we have to give like this
        print("In child class init")

    def feature1(self):
        print("Child feature2")

p2 = B()

