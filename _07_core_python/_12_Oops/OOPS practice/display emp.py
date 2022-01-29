'''Display each employee information'''
class Employee:

    def __init__(self):   #instance method
        self.name = 'Shilpa'  #instance variables
        self.empid = 30
        self.sal = 50000

    def display(self):
        return self.name, self.empid, self.sal

obj1  = Employee()
print("Emp1:",obj1.display())


obj2 = Employee()
obj2.name = 'Pranaya'
d = obj2.display()
print("Emp2:",d)

