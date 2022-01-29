class Myclass:  #class name must start with capital letter
    x=10

p1 = Myclass() #p1 is an object
print(p1.x)
print()
print('------------------init() function-----------------------')

class Person:
    def __init__(self,name,age): #name, age are attributes whereas self is predefined parameter
        self.name = name #self.name & self.age are instance attributes
        self.age = age   #name, age are local variables

p1 = Person('Shilpa',26) # object creation
print(p1.name, p1.age)
print(p1)



