class Student:

    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno

    def show(self): #instance method
        print(self.name, self.rollno)

    class Laptop:

        def __init__(self):
            self.brand = 'Lenovo'
            self.ram = '8GB'
            self.core = 'i5'

        def show(self):
            print(self.brand, self.ram, self.core)


s1 = Student('Shilpa',1)  #outer class object creation
s2  = Student('Advaitha',3)

print(s2.name,s1.rollno)

s1.show()  # Accessing outer class methods
s2.show()

i1 = Student.Laptop() # object creation for inner class
i1.show() # Accessing inner class methods