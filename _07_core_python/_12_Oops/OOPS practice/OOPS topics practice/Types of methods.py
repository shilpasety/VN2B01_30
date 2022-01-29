class Tom:

    School = 'VN2'  # class/static variable

    def __init__(self,m1,m2,m3):
        self.m1 = m1  # Instance variables --self.m2,self.m2,self.m3
        self.m2 = m2
        self.m3 = m3

    '''Instance methods can use both instance variables and class variables'''

    def avg(self):  # instance method, bcz we are using instance variables
        print("School name:",self.School)  # We can use class variables in instance method
        return (self.m1+self.m2+self.m3)/3

    '''Class methods can access class varaiables'''

    @classmethod  # Decorator
    def getschool(cls):
        print("School name in class method:",cls.School)

    @staticmethod # Decorator
    def info():         # Static methods can access class variables
        print("In static method:",Tom.School)

p1 = Tom(12,14,16)  # creating an object p1 -- It automatically insanitizes the init constructor

print(p1.avg()) # calling instance method

Tom.getschool() # calling class method

p1.info() # calling static method