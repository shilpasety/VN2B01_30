class Person:
    def __init__(self,name,age):  # we can change the 'self' parameter name but it should be the first parameter
        self.name = name
        self.age = age
    def myfunc(self):  #myfunc is a method
        print("Hey my name is "+self.name)
p1 = Person('Pranaya',1) #p1 is an object
p1.myfunc()