'''
What is MRO? Method Resolution Order

If two classes have the same method name, and another class is inheriting both the classes
When we create an object for that child class, when we try accessing the method(Different classes habe the same name)
it follows Left to Right order and displays only left side method

'''

class A:

    def feature1(self):
        print('In A feature')

class B:

    def feature1(self):
        print('In B feature')

class C(B,A):

    def __init__(self):
        print("In C init")

p3 = C()
p3.feature1()
